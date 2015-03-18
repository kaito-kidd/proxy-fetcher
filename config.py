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
TEST_TIMEOUT = 5

# 可用代理输出位置
PROXY_GOOD_DEST = "good_proxy_list.txt"

# referer list
REFERER_LIST = [
    "http://www.google.com/",
    "http://www.bing.com/",
    "http://www.baidu.com/",
]

# User-Agent list
USER_AGENT_LIST = [
    'Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
    'Microsoft Internet Explorer/4.0b1 (Windows 95)',
    'Opera/8.00 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
    'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
]

# 测试代理线程池大小
POOL_SIZE = 30
