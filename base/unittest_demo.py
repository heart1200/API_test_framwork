import os
import sys
import HTMLTestRunner
import unittest
import json
from unittest import mock
from mock_data import mock_data_func

from request_method import RunMain


class TestMethod(unittest.TestCase):
    # @classmethod
    # def setUpClass(cls):
    #     print('classSetUp')
    #
    # @classmethod
    # def tearDownClass(cls):
    #     print('classTearDown')

    def setUp(self):
        print('setUP is running')
        self.run = RunMain()

    def tearDown(self):
        print('tearDown is running')

    def test_01(self):
        # globals()关键字为全局变量，目的是为了使得用例之间有关联而设定的
        # globals()['id'] = '1000'
        print('Starting to 1 case')
        url = 'http://www.imooc.com/activity/redpacketinfo'
        data = {
            'marking': 'redpacket2021'
        }
        res = self.run.run_main(url, 'post', data)
        result = json.loads(res)
        self.assertEqual(result['errorCode'], 1000, 'FAIL')

    def test_02(self):
        print('Starting to 2 case')
        url = 'http://www.imooc.com/common/adver-getadver'
        res = self.run.run_main(url, 'get')
        result = json.loads(res)
        self.assertEqual(result['result'], 0, 'FAIL')

    def test_03(self):
        print('Starting to 3 case')
        url = 'http://coding.imooc.com/api/cate'
        data = {
            'timestamp': '1554213141535',
            'uid': '5051540',
            'uuid': '123123123123',
            'secret': 'werwewerwert',
            'token': '17f5148f2d2ca10bdbb850dd0ab2171a',
            'cid': '0',
            'errorCode': 1007
        }
        # mock_data = mock.Mock(return_value=data)
        # self.run.run_main = mock_data
        # res = self.run.run_main(url, 'post', data)
        # res = mock_data.return_value
        # result = json.loads(res)
        res = mock_data_func(self.run.run_main, url, 'post', data, data)
        self.assertEqual(res['errorCode'], 1007, 'FAIL')


if __name__ == '__main__':
    # unittest.main()
    # https://www.cnblogs.com/yoyoketang/p/7523409.html
    filePath = "../Reports/test.html"
    fp = open(filePath, 'wb')
    suite = unittest.TestSuite()
    suite.addTest(TestMethod('test_01'))
    suite.addTest(TestMethod('test_02'))
    suite.addTest(TestMethod('test_03'))
    # unittest.TextTestRunner.run(suite)
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="Test report")
    runner.run(suite)

