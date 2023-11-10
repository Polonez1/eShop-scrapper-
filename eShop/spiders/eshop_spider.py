import scrapy


class QuotesSpider(scrapy.Spider):
    name = "eshop_spider"
    start_urls = ["https://www.varle.lt/ispardavimas/"]

    def parse(self, response):
        for item in response.css("div.GRID_ITEM"):
            categories = {}
            for li in item.css("div.spec-shortcuts ul li"):
                cat = li.css("::text").get()
                name = li.css("a span::text").get()
                categories[cat] = name

            yield {
                "name": item.css("div.product-info div.product-title a::text").get(),
                "categories": categories,
            }


# scrapy crawl eshop_spider -o output.json
