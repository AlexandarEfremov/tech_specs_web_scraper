from typing import Any
import re
import scrapy
from scrapy.http import Response

from desktop_bg.desktop_bg.items import DesktopBgItem


class DesktopSpiderSpider(scrapy.Spider):
    name = "desktop_spider"
    allowed_domains = ["desktop.bg"]
    start_urls = ["https://desktop.bg/computers-all"]

    def parse(self, response: Response, **kwargs: Any) -> Any:
        item = DesktopBgItem()

        all_articles = response.css('li[id^="product"]')
        for pc in all_articles:
            list_of_specs = pc.css('ul li::text').getall()
            processor, gpu, motherboard, ram = list_of_specs[0], list_of_specs[1], list_of_specs[2], list_of_specs[3]

            match = re.search(r'от (.*?) до', ram)
            if match:
                ram = match.group(1)

            item["processor"] = processor
            item["gpu"] = gpu
            item["motherboard"] = motherboard
            item["ram"] = ram

            yield item

        next_page = response.css('li.next-page a::attr(href)').get()

        if next_page is not None:
            next_page_url = 'https://desktop.bg/' + next_page
            yield response.follow(next_page_url, callback=self.parse)

