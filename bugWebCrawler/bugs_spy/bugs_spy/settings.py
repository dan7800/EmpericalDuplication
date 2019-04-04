# -*- coding: utf-8 -*-

# Scrapy settings for bugs_spy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bugs_spy'

SPIDER_MODULES = ['bugs_spy.spiders']
NEWSPIDER_MODULE = 'bugs_spy.spiders'

RETRY_TIMES = 3
RETRY_HTTP_CODES = [429, 500, 503, 504, 400, 403, 404, 405, 408]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bugs_spy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bugs_spy.middlewares.BugsSpySpiderMiddleware': 543,
#}


# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
   'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
   'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
   'scrapy_proxies.RandomProxy': 100,
   'bugs_spy.middlewares.RotateUserAgentMiddleware': 400,
   'bugs_spy.middlewares.BugsSpyDownloaderMiddleware': 543,
   'bugs_spy.middlewares.TooManyRequestsRetryMiddleware': 543,
}
DOWNLOAD_HANDLERS = {
    'file': 'scrapy.core.downloader.handlers.file.FileDownloadHandler',
    'http': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
    'https': 'scrapy.core.downloader.handlers.http.HttpDownloadHandler',
    's3': 'scrapy.core.downloader.handlers.s3.S3DownloadHandler',
}
# Proxy mode
# 0 = Every requests have different proxy
# 1 = Take only one proxy from the list and assign it to every requests
# 2 = Put a custom proxy to use in the settings
PROXY_MODE = 0

# If proxy mode is 2 uncomment this sentence :
#CUSTOM_PROXY = "http://host1:port"

# Proxy list containing entries like
# http://host1:port
# http://username:password@host2:port
# http://host3:port
# ...
PROXY_LIST = '/Users/virginiapujols/PycharmProjects/bug_web_crawler/bugs_spy/bugs_spy/proxy_list.txt'
# PROXY_LIST = '/home/vp2532/bug_crawler/bugs_crawler/bugs_spy/bugs_spy/proxy_list.txt'

# User agent list containing entries like
# Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1
# ...
USER_AGENT_LIST = '/Users/virginiapujols/PycharmProjects/bug_web_crawler/bugs_spy/bugs_spy/user_agent_list.txt'
# USER_AGENT_LIST = '/home/vp2532/bug_crawler/bugs_crawler/bugs_spy/bugs_spy/user_agent_list.txt'

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'bugs_spy.pipelines.BugsSpyPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Custom setting keys
EXCLUDE_NODES_KEYWORDS = '/Users/virginiapujols/PycharmProjects/bug_web_crawler/bugs_spy/bugs_spy/exclude_nodes_list.txt'
# EXCLUDE_NODES_KEYWORDS = '/home/vp2532/bug_crawler/bugs_crawler/bugs_spy/bugs_spy/exclude_nodes_list.txt'

MOZILLA_DETAIL_URL = 'https://bugzilla.mozilla.org/show_bug.cgi?id={}&ctype=xml'
MOZILLA_SEARCH_URL = 'http://bugzilla.mozilla.org/buglist.cgi?chfieldfrom={}&chfieldto={}&chfield=%5BBug%20creation%5D&limit=0'

ECLIPSE_DETAIL_URL = 'http://bugs.eclipse.org/bugs/show_bug.cgi?id={}&ctype=xml'
ECLIPSE_SEARCH_URL = 'http://bugs.eclipse.org/bugs/buglist.cgi?chfieldfrom={}&chfieldto={}&chfield=%5BBug%20creation%5D&limit=0'

OPEN_OFFICE_DETAIL_URL = 'http://bz.apache.org/ooo/show_bug.cgi?id={}&ctype=xml'
OPEN_OFFICE_SEARCH_URL = 'http://bz.apache.org/ooo/buglist.cgi?chfieldfrom={}&chfieldto={}&chfield=%5BBug%20creation%5D&limit=0'

ANDROID_DETAIL_URL = 'https://bugzilla.mozilla.org/show_bug.cgi?id={}&ctype=xml'
ANDROID_SEARCH_URL = 'https://issuetracker.google.com/issues?q=created:2019-03-01..2019-03-02%20type:bug'
