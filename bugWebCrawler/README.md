# bugs_crawler
Script to crawl bug reports out of different projects.

### How to run
1. Follow the installation instructions for [Scrapy](https://docs.scrapy.org/en/latest/intro/install.html) framework.
2. Update the paths for the keys `PROXY_LIST, USER_AGENT_LIST, EXCLUDE_NODES_KEYWORDS` in the `settings.py` file.
3. Remove the `DEVELOPMENT` line in each spider and uncomment the `PRODUCTIOIN` to scrap multiple items instead of one.

