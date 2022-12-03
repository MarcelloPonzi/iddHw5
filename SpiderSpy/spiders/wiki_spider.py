import scrapy
import scrapy.http
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class WikiSpider(scrapy.Spider):
    name = "wiki_spider"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/Lists_of_companies"]



    def parse(self, response, **kargs):
        for link in response.xpath("//div/ul/li/a"):

            url = link.xpath(".//@href").get()
            url2 = 'https://en.wikipedia.org' + url
            yield {
                "link": url2
            }

# def parse_func(self, response):
#     for link in response.xpath('//h3/a'):
#         url = link.xpath('.//@href').get()
#         final_url = self.base_url + url.replace('../..', '')
#         yield {
#             "link": final_url
#         }



