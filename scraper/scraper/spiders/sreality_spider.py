import scrapy
import json

class SrealitySpider(scrapy.Spider):
    name = 'sreality_spider'
    allowed_domains = ['sreality.cz']
    start_urls = ['https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=20']
    count = 0

    def parse(self, response):
        data = json.loads(response.text)
        for item in data['_embedded']['estates']:
            yield {
                'title': item['name'],
                'image_url': item['_links']['images'][0]['href']
            }
            self.count += 1
            if self.count >= 500:
                return  # Stop spider after scraping 500 items

        # Code that handles pagination
        if self.count < 500:
            current_page = response.meta.get('page', 1)
            next_page = current_page + 1
            next_page_url = f"https://www.sreality.cz/api/cs/v2/estates?category_main_cb=1&category_type_cb=1&per_page=20&page={next_page}"
            yield scrapy.Request(next_page_url, callback=self.parse, meta={'page': next_page})

