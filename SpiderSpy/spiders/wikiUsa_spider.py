import scrapy


class WikiSpider(scrapy.Spider):
    name = "wikiusa_spider"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_companies_of_the_United_States_by_state"]
    base_url = 'https://en.wikipedia.org'
    custom_settings = {
        'DEPTH_LIMIT': 3
    }

    def parse(self, response, **kargs):
        companies_pages = response.xpath("//div/ul/li/a")
        for company_page in companies_pages:
            yield response.follow(url=company_page, callback=self.parse_company_page)

        states_links = response.xpath("//div[@role='note']/a")
        for state_link in states_links:
            yield response.follow(url=state_link, callback=self.parse_li_list())
            yield response.follow(url=state_link, callback=self.parse_company_table)


    def parse_company_table(self, response):
        table = response.xpath("//table/caption/following-sibling::tbody/tr")
        for row in table:

            name = row.xpath(".//td[1]/a/text()").get()
            industry = row.xpath(".//td[2]/text()").get()
            headquarters = row.xpath(".//td[4]/a/text()").get()
            founded = row.xpath(".//td[5]/text()").get()

            if type(name) is str:
                yield {
                    'Name': name,
                    'Industry': industry,
                    'Headquarters': headquarters,
                    'Founded': founded
                }


    def parse_company_page(self, response):
        info_box = response.xpath("//table[@class='infobox vcard']")
        name = info_box.xpath(".//text()").get()
        industry = info_box.xpath(".//tbody/tr[3]/td/a/text()").get()
        headquarters = info_box.xpath(".//tbody/tr[5]/td/a/text()").get()
        founded = info_box.xpath(".//tbody/td[4]/text()").get()

        if type(name) is str:
            yield {
                'Name': name,
                'Industry': industry,
                'Headquarters': headquarters,
                'Founded': founded
            }


