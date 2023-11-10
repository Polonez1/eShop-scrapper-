import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response):
        for quote in response.css("span.tag-item"):
            yield {
                "text": quote.css("a.tag::text").get(),
                # "author": quote.css("span small.author::text").get(),
                # "tags": quote.css("div.tags a.tag::text").getall(),
            }

        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)


# Uruchom Spidera

# scrapy crawl quotes -o output.json
# scrapy crawl quotes -o output.csv -L DEBUG
