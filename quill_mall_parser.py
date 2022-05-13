import requests
import re
import pprint

from store import Store
from storelist import StoreList

QUILL_CITY_MALL_HOSTNAME = "www.quillcitymall.com.my"

class QuillMallParser:
    def __init__(self):
        pass

    def fetch_stores(self) -> requests.Response:
        return requests.get(f"https://{QUILL_CITY_MALL_HOSTNAME}/wp-admin/admin-ajax.php?id=fm_sec&post_id=2391&slug=stores&canonical_url=https%3A%2F%2Fwww.quillcitymall.com.my%2Fstores%2F&posts_per_page=100&page=0&offset=0&post_type=stores&repeater=template_5&seo_start_page=1&preloaded=false&preloaded_amount=0&taxonomy=store_category&taxonomy_operator=IN&order=ASC&orderby=title&post_status=publish,%20future&action=alm_get_posts&query_type=standard",
        params={
            "id": "fm_sec",
            "post_id": 2391,
            "slug": "stores",
            "canonical_url": "https://www.quillcitymall.com.my/stores/",
            "posts_per_page": 999,
            "page": 0,
            "offset": 0,
            "post_type": "stores",
            "repeater": "template_5",
            "seo_start_page": 1,
            "preloaded": False,
            "preloaded_amount": 0,
            "taxonomy": "store_category",
            "taxonomy_operator": "IN",
            "order": "ASC",
            "orderby": "title",
            "post_status": "publish, future",
            "action": "alm_get_posts",
            "query_type": "standard",
        })

    def parse_api(self, r: requests.Response):
        r_json = r.json()
        html_store_list = r_json["html"]
        html_store_list_re = re.compile(r'''
        <div.class="fm_div">
        .*?"(?P<page_url>.*?)".*?
        <div.class="fm_image".*?url
        .*?'(?P<image_url>.*?)'.*?
        <div.class="fm_content".*?
        <h3>(?P<name>.*?)</h3>.*?
        <p>(?P<location>.*?)</p>.*?
        </div>.*?</div>
        ''',
        re.DOTALL | re.VERBOSE)
        stores = []
        for x in html_store_list_re.finditer(html_store_list):
            stores += [Store(**x.groupdict())]
        return StoreList(
            stores=stores,
        )

if __name__ == "__main__":
    qmp = QuillMallParser()
    r = qmp.fetch_stores()
    qmp.parse_api(r)
    pass