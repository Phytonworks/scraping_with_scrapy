import scrapy


class RwidSpider(scrapy.Spider):
    name = 'rwid'
    allowed_domains = ['https://id.carousell.com']
    #mulai scrapy
    start_urls = ['http://https://id.carousell.com/']

    def parse(self, response):
        yield {'title': response.css('title::text').get()}

    #1 ambil semua data
        detail_products = response.css('div', attrs={'class': 'D_kH'})
        for detail in detail_products:
            href = detail.attrs
            yield response.follow(href, callback + self.parse_detail)

    yield {'title': response.css('title::text').get()}

def parse_detail(self, response):
    yield {'title': response.css('title::text').get()}