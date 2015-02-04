# coding: utf8

"""代理测试器
"""

import re

from config import (
    PROXY_DEST, PROXY_GOOD_DEST, TEST_TIMEOUT,
    TEST_URL, CHECK_MARK
)


class Tester(object):
    """代理测试器
    """

    def __init__(self, input_file=PROXY_DEST, output_file=PROXY_GOOD_DEST,
                 timeout=TEST_TIMEOUT, test_url=TEST_URL,
                 check_mark=CHECK_MARK):
        self.input_file = input_file
        self.output_file = output_file
        self.timeout = timeout
        self.test_url = test_url
        self.check_mark = check_mark

        self.good_proxies = set()
        self.bad_proxies = set()

        self.all_proxies = self.load_proxies(self.input_file)

    def load_proxies(self, filename):
        """从文件加载代理,过滤

        @filename, str, 代理文件
        """
        proxy_list = set()
        with open(filename) as fip:
            for line in fip:
                proxy = line.strip()
                if not self.check_proxy(proxy):
                    continue
                proxy_list.add(proxy)
        return proxy_list

    def check_proxy(self, proxy):
        """校验代理

        @proxy, str, 单个代理
        """
        regx = r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}):(\d{1,5})"
        m = re.match(regx, proxy)
        items = m.groups()
        try:
            for i in range(4):
                if not 0 < int(items[i]) < 255:
                    return False
                if not int(items[4]) < 65536:
                    return False
        except ValueError:
            return False
        return True
