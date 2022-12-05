import scrapy


class WikiSpider(scrapy.Spider):
    name = "wiki_spider"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_companies_of_the_European_Union"]
    base_url = 'https://en.wikipedia.org'
    custom_settings = {
        'DEPTH_LIMIT': 1
    }

    def parse(self, response, **kargs):
        countries_links = response.xpath("//div[@role='note']/a")
        for country_link in countries_links:
            yield response.follow(url=country_link, callback=self.parse_company)

    def parse_company(self, response):
        table = response.xpath("//tbody[1]/tr")
        for row in table:
            name = row.xpath(".//td[1]/a/text()").get()
            industry = row.xpath(".//td[2]/text()").get()
            sector = row.xpath(".//td[3]/text()").get()
            headquarters = row.xpath(".//td[4]/a/text()").get()
            founded = row.xpath(".//td[5]/text()").get()
            if type(name) is str:
                yield {
                    'Name': name.strip(),
                    'Industry': industry.strip(),
                    'Sector': sector.strip(),
                    'Headquarters': headquarters.strip(),
                    'Founded': founded.strip()
                }


