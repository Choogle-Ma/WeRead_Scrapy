import scrapy, logging,  json
import time
from weread.items import WereadItem
from weread.category import noval_category

hosturl = "https://weread.qq.com/"


class weread_spider(scrapy.Spider):
    name = "category"
    allowed_domains = ["weread.qq.com"]

    def start_requests(self):
        url_root = "https://weread.qq.com/web/bookListInCategory/"
        requests = []

        category_list = []
        for i in noval_category:
            category_list_t = noval_category[i]
            category_list.extend(category_list_t)

        for category in category_list:
            url_t = url_root + str(category)
            request = scrapy.Request(url=url_t, callback=self.parse, meta={'category': category})
            requests.append(request)

        return requests

    def parse(self, response):
        # logging.info(response.text)
        item = WereadItem()
        item['category'] = response.meta['category']

        data = json.loads(response.text)
        item['books'] = data['books']
        item['synckey'] = data['synckey']
        item['hasMore'] = data['hasMore']
        item['totalCount'] = data['totalCount']

        # item.synckey =
        # t_ajax = response.xpath("//ul[@id='list_videos_common_videos_list_sort_list']/li[last()]").extract()
        # item['ajax'] = t_ajax

        # t = response.body
        # logging.info(t)

        yield item
