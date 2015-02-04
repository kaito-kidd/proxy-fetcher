# coding: utf8

"""配置
"""

# 采集的站点
PROXY_SITES = [
    'http://proxy.ipcn.org/proxylist2.html',
    'http://www.rmccurdy.com/scripts/proxy/good.txt',
    'http://wapland.org/proxy/proxy.txt',
    'http://best-proxy.ru/feed',
    'http://www.proxylists.net/?HTTP',
    'http://www.scrapeboxproxies.net/',
    'http://uks.pl.ua/script/getproxy.php?last',
    'http://checkerproxy.net/all_proxy',
    'http://ab57.ru/downloads/proxyold.txt',
    'http://www.freeproxy.ru/download/lists/goodproxy.txt',
    'http://www.proxylists.net/http_highanon.txt',
    'http://www.atomintersoft.com/high_anonymity_elite_proxy_list',
    'http://www.atomintersoft.com/transparent_proxy_list',
    'http://www.atomintersoft.com/anonymous_proxy_list',
    'http://www.proxy4free.info/',
    'http://tools.rosinstrument.com/proxy/plab100.xml',
]

# User-Agent
UA = (
    "Mozilla/5.0 (Windows NT 6.3; WOW64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/40.0.2214.93 Safari/537.36"
)

# 代理正则
PROXY_REGX = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{2,4}"

# 采集超时时间
FETCH_TIMEOUT = 10

# 代理输出位置
PROXY_DEST = "proxy_list.txt"

# 测试URL
TEST_URL = "http://www.163.com"

# 163的校验标识
CHECK_MARK = "netease.com"

# 测试代理超时时间
TEST_TIMEOUT = 30

# 可用代理输出位置
PROXY_GOOD_DEST = "good_proxy_list.txt"
