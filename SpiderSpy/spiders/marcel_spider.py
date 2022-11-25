import scrapy


class KaggleSpider(scrapy.Spider):
    name = "marcel_spider"
    start_urls = ['https://companiesmarketcap.com/']

    def parse(self, response, **kargs):
        all_tr_companies = response.xpath("//tbody/tr")
        print(all_tr_companies)
        for company in all_tr_companies:
            name = company.xpath(".//div[@class='company-name']/text()").get()
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
