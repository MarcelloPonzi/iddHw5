import scrapy
import scrapy.http
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class WikiSpider(scrapy.Spider):
    name = "wiki_spider"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_companies_of_the_European_Union"]
    base_url = 'https://en.wikipedia.org'
    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    def parse(self, response, **kargs):
        for next_page in response.xpath("//div[@role='note'][1]/a/@href"):
            yield response.follow(next_page, self.parse)

        for company in response.xpath('.//tbody'):
            name = company.xpath(".//tr/td[1]/text()").get()
            industry = company.xpath(".//tr/td[2]/text()").get()
            sector = company.xpath(".//tr/td[3]/text()").get()
            headquarters = company.xpath(".//tr/td[4]/text()").get()
            founded = company.xpath(".//tr/td[5]/text()").get()
            yield {
                'Name': name,
                'Industry': industry,
                'Sector': sector,
                'Headquarters': headquarters,
                'Founded': founded
            }




