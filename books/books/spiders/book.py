import scrapy

from books.items import BooksItem

class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["amazon.sg"]
    start_urls = ["https://www.amazon.sg/s?k=books&page=1"]

    #initializing the spider with keyword
    def __init__(self, keyword="books", *args, **kwargs):
        super(BookSpider, self).__init__(*args, **kwargs)
        self.keyword = keyword
        self.start_urls = [f"https://www.amazon.sg/s?k={keyword}&page=1"]

    def parse(self, response):

        #check if there are no results
        no_results = response.css("span.a-size-medium.a-color-base::text").get()
        if no_results and "No results for" in no_results:
            self.log("No results found, stopping the crawl.")
            return

        bop = response.css("div[role='listitem']")

        if not bop:
            print("No books found")
            return

        #extracting the book details using css selectors while validating them
        for book in response.css("div.a-section"):
            item = BooksItem()
            item["imgurl"] = book.css("img.s-image::attr(src)").get()
            if not item["imgurl"]:
                continue
            item["title"] = book.css("div[data-cy='title-recipe'] span::text").get()
            if not item["title"]:
                continue
            item["price"] = book.css("span.a-price-whole::text").get()
            if not item["price"]:
                continue
            rating = book.css("i[data-cy='reviews-ratings-slot'] span::text").get()
            if rating:
                item["rating"] = rating.split(" ")[0]
            else:
                continue
            item["url"] = response.url
            if all(field in item for field in ["title", "price", "imgurl"]):
                yield item
        
        #extracting the next page url and calling the parse function recursively
        cp = response.url.split("page=")[-1]
        np = int(cp) + 1
        npu = f"https://www.amazon.sg/s?k=books&page={np}"
        
        yield scrapy.Request(url=npu, callback=self.parse, dont_filter=True)
