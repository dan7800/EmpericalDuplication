import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'

    def start_requests(self):
        urls = ['http://quotes.toscrape.com/page/1/',
                'http://quotes.toscrape.com/page/2/'
                ]
        for u in urls:
            yield scrapy.Request(url=u, callback=self.parse)

    def parse(self, response):
        page = response.url.split('/')[-2]
        file_name = 'quotes-%s.html' % page
        with open(file_name, 'wb') as f:
            f.write(response.body)
        self.log('Saved file  %s' % file_name)

