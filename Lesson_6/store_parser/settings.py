# Scrapy settings for store_parser project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'store_parser'
IMAGES_STORE = 'photos'

SPIDER_MODULES = ['store_parser.spider']
NEWSPIDER_MODULE = 'store_parser.spider'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 8

LOG_ENABLED = True
LOG_LEVEL = 'DEBUG'

# MONGO_URI = 'mongodb://localhost:27017'
# MONGO_DB = 'castorama'

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#    'Сookie': 'u=2tcs9xca.uiltr4.1u896yyeung50; luri=moskva; buyer_location_id=637640; sx=H4sIAAAAAAAC%2F0zMUVLDIBAG4Lvscx%2BWLfxkcxvIglTTtANR62Ryd5%2Bc8QLfQfA%2BiU2TTLBgtcQsqbLJlUWlQmg%2B6Itm2p%2FtbvLMoz%2FY3Tpe493XR%2Fpst213rtOFCs0OAcExqz8vBACLRVSFBnhoiblc1WLgZYmmf%2FLk89tYBwcJL7f6vt%2B%2FP7a28o%2FbRmr1n8wRivP8DQAA%2F%2F9sVr7TtQAAAA%3D%3D; abp=0; SEARCH_HISTORY_IDS=4; _ym_uid=16564118521050838944; _ym_d=1656411852; _ym_isad=2; _gcl_au=1.1.20969656.1656411852; _ga_9E363E7BES=GS1.1.1656423690.3.1.1656423691.59; _ga=GA1.1.…0%7C1656423694208; buyer_laas_location=637640; _buzz_fpc=JTdCJTIycGF0aCUyMiUzQSUyMiUyRiUyMiUyQyUyMmRvbWFpbiUyMiUzQSUyMi53d3cuYXZpdG8ucnUlMjIlMkMlMjJleHBpcmVzJTIyJTNBJTIyV2VkJTJDJTIwMjglMjBKdW4lMjAyMDIzJTIwMTMlM0EwMSUzQTQwJTIwR01UJTIyJTJDJTIyU2FtZVNpdGUlMjIlM0ElMjJMYXglMjIlMkMlMjJ2YWx1ZSUyMiUzQSUyMiU3QiU1QyUyMnZhbHVlJTVDJTIyJTNBJTVDJTIyNmVlMTRkZmYwNmU5YzFkNGU3MTUwYzcwOTY3ODc0MjclNUMlMjIlMkMlNUMlMjJmcGpzRm9ybWF0JTVDJTIyJTNBdHJ1ZSU3RCUyMiU3RA==; v=1656422801; dfp_group=63; _ym_visorc=b; _dc_gtm_UA-2546784-1=1'
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'store_parser.middlewares.StoreParserSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'store_parser.middlewares.StoreParserDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'store_parser.pipelines.StoreParserPipeline': 300,
   'store_parser.pipelines.StorePhotosPipeline': 200
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 3
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = True

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
