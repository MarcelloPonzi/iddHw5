import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
        'https://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response, **kargs):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.xpath("//span[@class='text']/text()").get(),
                'author': quote.xpath("//small/text()").get(),
                'tags': quote.xpath("//div/a/text()").getall(),
            }
