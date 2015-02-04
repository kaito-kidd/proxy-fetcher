# coding: utf8

"""代理采集器
"""

import re
import socket
import urllib2

from config import (
    PROXY_SITES, PROXY_DEST, UA,
    PROXY_REGX, FETCH_TIMEOUT
)


class Fetcher(object):

    """代理采集器
    """

    def __init__(self, proxy_dest=PROXY_DEST):
        self.proxy_dest = proxy_dest
        self.fetch_sites = PROXY_SITES
        self.timeout = FETCH_TIMEOUT

    def fetch(self):
        """采集代理
        """
        for site in self.fetch_sites:
            request = urllib2.Request(site)
            request.add_header("User-Agent", UA)
            try:
                print "fetch proxy from %s" % site
                response = urllib2.urlopen(
                    request, timeout=self.timeout).read()
                proxies = re.findall(PROXY_REGX, response)

            except (urllib2.URLError, socket.error) as exc:
                print "fetch %s failed: %s" % (site, str(exc))
                proxies = []
            else:
                print "%s proxies from %s" % (len(proxies), site)
            self.output(proxies)

    def output(self, proxies):
        """输出
        @proxies, list, 代理列表
        """
        if not proxies:
            return
        for proxy in proxies:
            with open(self.proxy_dest, "a") as fpt:
                fpt.write("%s\n" % proxy)


def main():
    """ main """
    Fetcher().fetch()


if __name__ == "__main__":
    main()
