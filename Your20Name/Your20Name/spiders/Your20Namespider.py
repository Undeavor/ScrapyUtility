import scrapy


class Your20NamespiderSpider(scrapy.Spider):
    name = 'Your20Namespider'
    allowed_domains = ['s22.anime-sama.fr']
    start_urls = ['https://s22.anime-sama.fr/s1/scans/Your%20Name/1/']

    def parse(self, response):
        for i in range(9):
            if i!=0:
                tome_url = "https://s22.anime-sama.fr/s1/scans/Your%20Name/" + str(i) + "/"
                yield response.follow(tome_url) 
                for image_url in response.css('a::attr(href)').getall(): #magnifique code
                    yield {'image_urls': [response.urljoin(image_url)]}  #magnifique code
            else:
                pass


