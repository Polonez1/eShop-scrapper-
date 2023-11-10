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
                "price_eur": item.css(
                    "div.price-container div.price-tag span span::text"
                ).get(),
                "price_cnt": item.css(
                    "div.price-container div.price-tag span sup::text"
                ).get(),
                "discount": item.css(
                    "div.price-container div.discount-line span::text"
                ).get(),
                "categories": categories,
            }

        all_links = response.css("li.wide a.for-desktop::attr(href)").getall()

        if len(all_links) >= 2 and "/ispardavimas/?p=" in all_links[1]:
            next_page = all_links[1]

        if next_page is not None:
            full_url = response.urljoin(next_page)
            yield response.follow(full_url, self.parse)


# scrapy crawl eshop_spider -o output_discount.json
#
