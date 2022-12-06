import time

import scrapy
import scrapy.statscollectors
from ..statistiche import Statistiche


class WikiSpider(scrapy.Spider):
    name = "wikiusa_spider"
    allowed_domains = ["wikipedia.org"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_companies_of_the_United_States_by_state"]
    base_url = 'https://en.wikipedia.org'
    custom_settings = {
        'DEPTH_LIMIT': 3
    }
    stats = Statistiche()

    def parse(self, response, **kargs):

        f = open("link trovati.txt", "w")

        """Prende i link alle pagine di compagnie direttamente sulla sorgente"""
        companies_pages = response.xpath("//div[@class='mw-parser-output']/ul/li/a")
        num_pagine = 0
        for company_page in companies_pages:
            num_pagine = num_pagine + 1
            self.stats.inc_request()
            yield response.follow(url=company_page, callback=self.parse_company_page)


        """Prende i link alle liste di compagnie dei singoli stati"""
        states_links = response.xpath("//div[@role='note']/a")
        link_stati = 0
        for state_link in states_links:
            link_stati = link_stati + 1
            self.stats.inc_request()
            yield response.follow(url=state_link, callback=self.parse_li_list)
            yield response.follow(url=state_link, callback=self.parse_company_table)
        f.write("pagine compagnie: " + str(num_pagine) + "\n" + "link stati: " + str(link_stati))
        f.close()

    def parse_li_list(self, response):
        companies_pages = response.xpath("//div[@class='mw-parser-output']/ul/li/a")
        for company_page in companies_pages:
            self.stats.inc_request()
            yield response.follow(url=company_page, callback=self.parse_company_page)

    def parse_company_table(self, response):
        table = response.xpath("//table/caption/following-sibling::tbody/tr")
        for row in table:
            name = row.xpath(".//td[1]/a/text()").get()
            industry = row.xpath(".//td[2]/text()").get()
            headquarters = row.xpath(".//td[4]/a/text()").get()
            founded = row.xpath(".//td[5]/text()").get()
            if type(name) is str:
                self.stats.hitted()
                yield {
                    'Name': name,
                    'Industry': industry,
                    'Headquarters': headquarters,
                    'Founded': founded
                }
        self.stats.reset_hit()
        self.stats.print_stats()


    def parse_company_page(self, response):
        info_box = response.xpath("//table[@class='infobox vcard']")
        name = info_box.xpath(".//text()").get()
        industry = info_box.xpath(".//tbody/tr/th[text()='Industry']/following-sibling::td/text()").get()
        headquarters = info_box.xpath(".//tbody/tr/th[text()='Headquarters']/following-sibling::td/a/text()").get()
        founded = info_box.xpath(".//tbody/tr/th[text()='Founded']/following-sibling::td/text()").get()

        if type(name) is str:
            self.stats.hitted()
            yield {
                'Name': name,
                'Industry': industry,
                'Headquarters': headquarters,
                'Founded': founded
            }
        self.stats.reset_hit()
        self.stats.print_stats()

