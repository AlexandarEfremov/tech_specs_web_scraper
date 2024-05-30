# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DesktopBgItem(scrapy.Item):
    processor = scrapy.Field()
    gpu = scrapy.Field()
    motherboard = scrapy.Field()
    ram = scrapy.Field()

