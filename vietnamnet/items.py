# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class VietnamnetItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    field = Field()
    subfield = Field()
    title = Field()
    posttime = Field()
    articlelead = Field()
    content = Field()
    imageurl = Field()
    tags = Field()

    # Housekeeping fields
    url = Field()
    project = Field()
    spider = Field()
    server = Field()
    date = Field()

