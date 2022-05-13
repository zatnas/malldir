import unittest

from quill_mall_parser import QuillMallParser
from storelist import StoreList

class TestQuillMallParser(unittest.TestCase):
    def setUp(self):
        self.mall_directory = QuillMallParser()

    def test_quill_mall_parser_api_valid(self):
        r = self.mall_directory.fetch_stores()
        self.assertEqual(r.status_code, 200)

    def test_quill_mall_parser_api_parse(self):
        s = self.mall_directory.fetch_stores()
        r = self.mall_directory.parse_api(s)
        self.assertIsInstance(r, StoreList)


if __name__ == "__main__":
    unittest.main()