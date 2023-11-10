import scrapy


class QuotesSpider(scrapy.Spider):
    name = "eshop_spider"
    start_urls = ["https://www.varle.lt/ispardavimas/"]

    def parse(self, response):
        for item in response.css("div.GRID_ITEM"):
            yield {
                "name": item.css("div.product-info div.product-title a::text").get(),
                "category": item.css("div.spec-shortcuts ul li a span::text").get(),
            }


# scrapy crawl eshop_spider -o output.json
