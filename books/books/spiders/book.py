import scrapy

from books.items import BooksItem

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["atticbooks.co.ke"]
    start_urls = ["https://atticbooks.co.ke/category/non-fiction-books?p=70"]

    def parse(self, response):

        bop = response.css("h3.product-title")

        if not bop:
            print("No books found")
            return

        for book in response.css("div.card-body"):
            item = BooksItem()
            item["title"] = book.css("h3 > a::text").get()
            item["price"] = book.css("div > div > span > span::text").get()
            yield item
        
        cp = response.url.split("p=")[-1]
        np = int(cp) + 1
        npu = f"https://atticbooks.co.ke/category/non-fiction-books?p={np}"
        
        yield scrapy.Request(url=npu, callback=self.parse, dont_filter=True)
