import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MarketCapSpider(scrapy.Spider):
    name = "marketCap_spider"
    allowed_domains = ["companiesmarketcap.com"]
    start_urls = [f'https://companiesmarketcap.com/page/{i}' for i in range(1, 11)]

    def parse(self, response, **kargs):
        all_tr_companies = response.xpath("//tbody/tr")
        for company in all_tr_companies:
            name = company.xpath("normalize-space(.//div[@class='company-name']/text())").get()
            codice = company.xpath(".//div[@class='company-code']/text()").get()
            pricecap = company.xpath("./td[3]/text()").get()
            price = company.xpath(".//td[4]/text()").get()
            country = company.xpath(".//td[last()]/span/text()").get()
            yield {
                'name': name,
                'codice': codice,
                'pricecap': pricecap,
                'price': price,
                'country': country
            }
