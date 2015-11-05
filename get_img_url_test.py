#测试用例
import unittest
import re
from re_query_url import *

class Test_get_url(unittest.TestCase):
	def setUp(self):
		self.p = get_img_url1('http://www.baidu.com')
		self.q = get_img_url2('http://www.sina.com')
	def test_init(self):
		self.assertTrue(isinstance(self.p,list))
		self.assertTrue(isinstance(self.q,list))
        def test_if_img(self):
                d = ['jpg','png','gif','jpeg']
                for i in self.p:
                        res = re.match(r'(.+)\.(.*)',i).group(2)
                        self.assertTrue(res in d)
                for j in self.q:
                        res = re.match(r'(.+)\.(.*)',j).group(2)
                        self.assertTrue(res in d)
	def test_attr(self):
		self.p.append('test')
		self.assertEqual(self.p[-1],'test')
		self.assertTrue('test' in self.p)
		self.q.append('test')
		self.assertEqual(self.q[-1],'test')
		self.assertTrue('test' in self.q)
	def test_error(self):
		with self.assertRaises(requests.exceptions.MissingSchema):
			get_img_url1('www.baidu.com')
			get_img_url2('www.sina.com')


if __name__=='__main__':
	unittest.main()
