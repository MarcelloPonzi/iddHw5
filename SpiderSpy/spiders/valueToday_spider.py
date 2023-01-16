import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class ValueTodaySpider(scrapy.Spider):
    name = "valueToday_spider"
    allowed_domains = ["value.today"]
    start_urls = [f'https://www.value.today/' \
                  f'?title=&field_company_category_primary_target_id&field_headquarters_of_company_target_id=' \
                  f'All&field_company_website_uri=&field_market_value_jan072022_value=&page={i}'
                  for i in range(0, 1068)]

    def parse(self, response, **kargs):
        all_tr_companies = response.xpath("//div[contains(@class,'group-header')]")
        for company in all_tr_companies:
            name = company.xpath(".//div[1]/h1/a/text()").get()
            world_rank = company.xpath(".//div[2]/div[2]/text()").get()
            marketCap = company.xpath(".//div[5]/div[2]/text()").get()
            marketValue = company.xpath(".//div[3]/div[2]/text()").get()
            CEO = company.xpath("parent::*/div[3]/div[3]/div[2]/div/a/text()").get()
            country = company.xpath("parent::*/div[2]/div/div[2]/div/a/text()").get()
            yield {
                'name': name,
                'world_rank': world_rank,
                'marketValue': marketValue,
                'marketCap': marketCap,
                'CEO': CEO,
                'country': country
            }
