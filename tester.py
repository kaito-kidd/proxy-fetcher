# coding: utf8

"""代理测试器
"""

import re
import urllib2
import random
import time
import threading

from thread_pool.pool import Pool

from config import (
    PROXY_DEST, PROXY_GOOD_DEST, TEST_TIMEOUT,
    TEST_URL, CHECK_MARK, USER_AGENT_LIST, REFERER_LIST,
    POOL_SIZE
)

# proxy compile
REGX = r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3}):(\d{1,5})"
PROXY_RE = re.compile(REGX)

# good, bad flag
GOOD_STATUS = 1
BAD_STATUS = 0


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

        self.lock = threading.Lock()

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

    @staticmethod
    def check_proxy(proxy):
        """校验代理

        @proxy, str, 单个代理
        """
        m = PROXY_RE.match(proxy)
        items = m.groups()
        try:
            for i in range(4):
                if not 0 < int(items[i]) < 255:
                    return False
                if not int(items[4]) < 65536:
                    return False
        except (ValueError, IndexError):
            return False
        return True

    def do_test(self, proxy):
        """测试代理

        @proxy, str, 单个代理
        """
        # build
        proxy_handler = urllib2.ProxyHandler({"http": proxy})
        opener = urllib2.build_opener(proxy_handler, urllib2.HTTPHandler)
        opener.addheaders = [
            ("User-Agent", random.choice(USER_AGENT_LIST)),
            ("Referer", random.choice(REFERER_LIST))
        ]
        urllib2.install_opener(opener)
        start = time.time()
        try:
            # fetch
            response = urllib2.urlopen(self.test_url, timeout=self.timeout)
            status_code = response.code
            content = response.read(3000)
        except:
            self.bad_proxies.add(proxy)
            self.log(BAD_STATUS, proxy, time.time() - start)
            return
        speed = time.time() - start
        # content test & log, output
        if self.content_test(status_code, content):
            self.good_proxies.add(proxy)
            self.log(GOOD_STATUS, proxy, speed)
            self.good_output(proxy, speed)
        else:
            self.bad_proxies.add(proxy)
            self.log(BAD_STATUS, proxy, speed)

    def content_test(self, status_code, content):
        """内容检测

        @status_code, int, 相应状态码
        @content, str, 相应正文
        """
        if status_code != 200:
            return False
        if self.check_mark not in content:
            return False
        return True

    def log(self, status, proxy, speed):
        """log

        @status, int, 1: good, 0: bad
        @proxy, str, proxy
        @speed, float, 速度
        """
        with self.lock:
            msg = "%s [%d/%d/%d] %s time: %f" \
                % ("[OK]" if status else "[ERROR]",
                   len(self.good_proxies), len(self.bad_proxies),
                   len(self.all_proxies), proxy, speed)
            print(msg)

    def good_output(self, proxy, speed):
        """output

        @proxy, str, proxy
        @speed, float, 速度
        """
        with self.lock:
            with open(self.output_file, "a") as fop:
                fop.write("%s|%s\n" % (proxy, speed))


def main():
    """ main """
    tester = Tester()
    pool = Pool(size=POOL_SIZE)
    pool.add_tasks(
        [(tester.do_test, (proxy,)) for proxy in tester.all_proxies])
    pool.run()


if __name__ == "__main__":
    main()
