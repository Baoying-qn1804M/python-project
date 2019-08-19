import scrapy


class NewSpider(scrapy.Spider):
    name = "new_spider"

    start_urls = ['http://172.18.58.238/photography/']
    #start_urls = ['https://www.parents.com/baby/health/cough/decoding-babys-cough/']

    def parse(self, response):
        # save out the reference webpage code
        yield {'Referene Webpage': response.text}

        # Image selector
        xpath_selector = '//img'
        for x in response.xpath(xpath_selector):
            newsel = '@src'

            img_link = x.xpath(newsel).extract_first()

            if img_link.endswith('.jpg') or img_link.endswith('.jpeg'):
                yield {
                    'Image Link': img_link
                }
                #the IF is only save jpg relevant pictures, dh other thing
                #yield = generate output
        # Recursively search through all page links for images on those links
        page_selector = '.next a ::attr(href)'
        next_page = response.css(page_selector).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
            )
