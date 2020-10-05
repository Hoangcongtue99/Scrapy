import datetime
from urllib.parse import urlparse, urljoin
import socket
import scrapy

from scrapy.loader.processors import MapCompose, Join
from scrapy.loader import ItemLoader

from vietnamnet.items import VietnamnetItem
from scrapy.http import Request


class BasicSpider(scrapy.Spider):
    name = 'test'
    allowed_domains = ['vietnamnet.vn']
    start_urls = [
        "https://vietnamnet.vn/vn/thoi-su/"]
    ''',
        'https://vietnamnet.vn/vn/kinh-doanh/',
        'https://vietnamnet.vn/vn/giai-tri/',
        'https://vietnamnet.vn/vn/the-gioi/',
        'https://vietnamnet.vn/vn/giao-duc/',
        'https://vietnamnet.vn/vn/doi-song/'
        'https://vietnamnet.vn/vn/phap-luat/',
        'https://vietnamnet.vn/vn/the-thao/',
        'https://vietnamnet.vn/vn/cong-nghe/',
        'https://vietnamnet.vn/vn/suc-khoe/',
        'https://vietnamnet.vn/vn/bat-dong-san/',
        'https://vietnamnet.vn/vn/ban-doc/',
        'https://vietnamnet.vn/vn/tuanvietnam/',
        'https://vietnamnet.vn/vn/oto-xe-may/',
        'https://vietnamnet.vn/vn/goc-nhin-thang/',
        'https://vietnamnet.vn/vn/hotface/',
        'https://vietnamnet.vn/vn/ban-tron-truc-tuyen/'
    ]
    '''

    def parse(self, response):
        # Create the loader using the response
        l = ItemLoader(item=VietnamnetItem(), response=response)

        # Load fields using XPath expressions
        l.add_value('field', response.css('.top-cate-head-title').xpath('.//text()').extract())
        l.add_value('subfield', response.css('.top-cate-head-subcate-child').xpath('./a/@title').extract())
        l.add_value('title', response.xpath('//h1/text()').extract())
        l.add_value('posttime', response.css('.ArticleDate').xpath('./text()').extract(),Join('\n'),MapCompose(lambda i: i.replace('\xa0',' '), lambda i: " ".join(i.split())))
        l.add_value('articlelead', response.css('.ArticleLead').xpath('.//text()').extract())
        l.add_value('content', response.css('.ArticleLead').xpath('./following-sibling::p/text()').extract(),Join('\n'),MapCompose(lambda i: i.replace('\xa0',' ')))
        l.add_value('imageurl', response.css('.ArticleLead').xpath('./following-sibling::table//img/@src').extract())
        l.add_value('tags', response.css('.tagBoxTitle').xpath('./parent::*/following-sibling::*//text()').extract())

        # Housekeeping fields
        l.add_value('url', response.url)
        l.add_value('project', self.settings.get('BOT_NAME'))
        l.add_value('spider', self.name)
        l.add_value('server', socket.gethostname())
        l.add_value('date', datetime.datetime.now())

        return l.load_item()
