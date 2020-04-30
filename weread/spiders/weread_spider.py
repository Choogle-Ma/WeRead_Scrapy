import scrapy, logging
import time
from weread.items import WereadItem

hosturl = "https://weread.qq.com/"


class weread_spider(scrapy.Spider):
    name = "weread"
    allowed_domains = ["qq.com"]

    def start_requests(self):
        url_100000 = "https://weread.qq.com/web/bookListInCategory/100000"
        requests = []

        for i in range(1, 21):

            request = scrapy.Request(url=mostpopular_url,  callback=self.parse)
            requests.append(request)
            # time.sleep(0.5)
        return requests

    def parse(self, response):
        item = FeichaiItem()
        video_name = []
        content = {}

        # t_ajax = response.xpath("//ul[@id='list_videos_common_videos_list_sort_list']/li[last()]").extract()
        # item['ajax'] = t_ajax

        # t = response.body
        # logging.info(t)

        # r = response.xpath("//strong[@class='title']/text()").extract()
        # logging.info(r)

        links = response.xpath("//a[@target='_blank']/@href").extract()
        # logging.info(links)
        names = response.xpath("//a[@target='_blank']/@title").extract()
        # logging.info(names)

        # data = response.xpath("//div[@id='list_videos_common_videos_list_items']/div[@class='item']").extract()

        # logging.info(len(links))

        for i in range(0, len(links)):
            # logging.info(names[i])
            # logging.info(links[i])
            content[names[i]] = hosturl + links[i]
        item['content'] = content

        yield item
