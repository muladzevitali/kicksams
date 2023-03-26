import logging
from datetime import datetime

import scrapy
from django.db.utils import IntegrityError
from scrapy_djangoitem import DjangoItem

from apps.news.models import News


class NewsItem(DjangoItem):
    django_model = News


class UANewsSpider(scrapy.Spider):
    name = 'ua_news'
    allowed_domains = ['112ua.tv']
    start_urls = ['https://112ua.tv/rsslist']
    __date_format = '%a, %d %b %Y %H:%M:%S %z'

    def __init__(self, name='UANewsSpider', **kwargs):
        logger = logging.getLogger('ua_news_spider')
        logger.setLevel(logging.CRITICAL)

        super().__init__(name, **kwargs)

    def parse(self, response, **kwargs):
        rss_feeds = response.xpath('//div[@class="statpage-content"]/p/a/@href').extract()
        for rss_feed in rss_feeds:
            yield scrapy.Request(rss_feed, callback=self.parse_rss_page)

    def parse_rss_page(self, request):
        items = request.xpath('//item')

        for item in items:
            news_item = NewsItem()
            news_item['title'] = item.xpath('./title/text()').extract_first()
            news_item['url'] = item.xpath('./link/text()').extract_first()
            news_item['category'] = item.xpath('./category/text()').extract_first()
            news_item['image_url'] = item.xpath('./enclosure/@url').extract_first()
            published_at = item.xpath('./pubDate/text()').extract_first()
            published_at = _ru_to_en_date_text(published_at)
            if published_at:
                news_item['published_at'] = datetime.strptime(published_at, self.__date_format)
            try:
                news_item.save()
            except IntegrityError:
                continue
