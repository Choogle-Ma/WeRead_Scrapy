import scrapy, logging,  json
import time
from weread.items import WereadItem
from weread.category import noval_category

hosturl = "https://weread.qq.com/"


class weread_spider(scrapy.Spider):
    name = "category"
    allowed_domains = ["weread.qq.com"]

    def start_requests(self):
        url_100000 = "https://weread.qq.com/web/bookListInCategory/"
        requests = []

        for i in range(1, 2):
            url_t = url_100000 + '?maxIndex=' + str(20*i)
            request = scrapy.Request(url=url_t,  callback=self.parse)
            requests.append(request)
            # time.sleep(0.5)
        return requests

    def parse(self, response):
        # logging.info(response.text)
        item = WereadItem()
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
