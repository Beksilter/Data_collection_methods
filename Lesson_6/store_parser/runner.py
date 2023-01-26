import os
import sys
sys.path.append(os.path.join(os.getcwd(), '..'))

from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from store_parser.spider.castorama import CastoramaSpider


if __name__ == '__main__':
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)

    # Можно передавать параметры в url. Все что после "?" в url записывается в url_args.
    runner.crawl(
        CastoramaSpider,
        url_args={
            'q': 'шкаф',
            'bm_tip_produkta': 'шкаф зеркальный для ванной'
        }
    )

    reactor.run()
