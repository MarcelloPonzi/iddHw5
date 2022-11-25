import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MarketCapSpider(scrapy.Spider):
    name = "marketCap_spider"
    allowed_domains = ["companiesmarketcap.com"]
    start_urls = [f'https://companiesmarketcap.com/page/{i}' for i in range(1, 10)]

    def parse(self, response, **kargs):
        for company in response.xpath("//tbody/tr"):
            yield {
                'nome': company.css(".company-name::text").get(),
                'pricecap': company.css("td.td-right::text").get()

            }
