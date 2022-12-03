import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

class DisfoldSpider(scrapy.Spider):
    name = "disfoldSpider"
    allowed_domains = ["disfold"]
    start_urls = [f'https://disfold.com/world/companies/?page={i}'
                  for i in range(1, 21)]

    def parse(self, response, **kargs):
        all_tr_companies = response.xpath("//tbody/tr")
        for company in all_tr_companies:
            name = company.xpath(".//td[2]/a/text()").get()
            marketCap = company.xpath("normalize-space(.//td[3]/a/text())").get()
            stock = company.xpath("normalize-space(.//td[4]/a/text())").get()
            sector = company.xpath("normalize-space(.//td[6]/a/text()[2])").get()
            industry = company.xpath("normalize-space(.//td[7]/a/text()[2])").get()
            country = company.xpath("normalize-space(.//td[5]/a/text()[2])").get()
            yield {
                'name': name,
                'marketCap': marketCap,
                'stock': stock,
                'sector': sector,
                'industry': industry,
                'country': country
            }