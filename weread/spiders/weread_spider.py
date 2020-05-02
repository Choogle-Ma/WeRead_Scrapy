import scrapy, logging,  json
import time
from weread.items import WereadItem
from weread.category import CATEGORY_COUNT

hosturl = "https://weread.qq.com/"


class weread_spider(scrapy.Spider):
    name = "weread"
    allowed_domains = ["weread.qq.com"]

    def start_requests(self):
        url_root = "https://weread.qq.com/web/bookListInCategory/"
        requests = []

        for category in CATEGORY_COUNT:
            totalcount = CATEGORY_COUNT[category]
            page = totalcount//20 + 1
            for i in range(1, page):
                maxindex = 20 * i
                url_t = url_root + str(category) + '?maxIndex=' + str(maxindex)
                request = scrapy.Request(url=url_t, callback=self.parse, meta={'category': category, 'index': maxindex})
                requests.append(request)

        return requests

    def parse(self, response):
        # logging.info(response.text)
        item = WereadItem()
        item['category'] = response.meta['category']
        item['index'] = response.meta['index']

        data = json.loads(response.text)
        item['books'] = data['books']
        item['synckey'] = data['synckey']
        item['hasMore'] = data['hasMore']
        item['totalCount'] = data['totalCount']

        yield item
