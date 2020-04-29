import scrapy, logging
import time
from weread.items import WereadItem

hosturl = "https://weread.qq.com/"


class weread_spider(scrapy.Spider):
    name = "weread"
    allowed_domains = ["qq.com"]

    def start_requests(self):
        vip_url = "http://fcww14.com/categories/058ed3f9acd0842ef11c4b6a25ebdb5b/"
        ajax_url = "http://fcww14.com/categories/058ed3f9acd0842ef11c4b6a25ebdb5b/?mode=async&function=get_block&block_id=list_videos_common_videos_list&sort_by=most_favourited&_=1511968509508"
        requests = []
        native_url = "http://fcww14.com/categories/27f8a5c9ce83cbfa7b70fc5c9a73a082/"
        mostpopular_url = "http://fcww14.com/most-popular/"

        for i in range(1, 21):
            if i < 10:
                formdata_t = {
                    "mode": "async",
                    "function": "get_block",
                    "block_id": "list_videos_common_videos_list",
                    # "sort_by": "most_favourited",
                    "sort_by": "video_viewed",
                    "from": "0"+str(i),
                    "_": "1512570459528"
                }
            else:
                formdata_t = {
                    "mode": "async",
                    "function": "get_block",
                    "block_id": "list_videos_common_videos_list",
                    # "sort_by": "most_favourited",
                    "sort_by": "video_viewed",
                    "from": str(i),
                    "_": "1512570459528"
                }
            request = scrapy.FormRequest(url=mostpopular_url, formdata=formdata_t, callback=self.parse)
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