import scrapy
from ..items import BasicHouseItem
from ..utils import generate_url


class FundaListingsSpider(scrapy.Spider):
    name = 'funda_listings'
    allowed_domains = ["https://www.funda.nl/"]

    def start_requests(self):
        return [scrapy.FormRequest(generate_url())]

    def parse(self, response):
        result_blocks = response.css("ol.search-results")
        for result_block in result_blocks:
            results = result_block.css("li.search-result")

            for result in results:
                url = result.css("div.search-result__header-title-col a::attr(href)").get()
                address = result.css("h2.search-result__header-title::text").get().strip()
                zipcode = result.css("h4.search-result__header-subtitle::text").get().strip()
                price = result.css("span.search-result-price::text").get()
                properties = result.css(".search-result-kenmerken")
                house_size = properties.css("span[title*='Gebruiksoppervlakte wonen']::text").get()
                plot_size = properties.css("span[title*='Perceeloppervlakte']::text").get()
                rooms = properties.css("li::text")[-1].get()
                image = result.css(".search-result-image img::attr(src)").get()

                items = BasicHouseItem()
                items['url'] = f"https://www.funda.nl/{url}"
                items['address'] = address
                items['zipcode'] = zipcode
                items['price'] = price
                items['house_size'] = house_size
                items['plot_size'] = plot_size
                items['rooms'] = rooms
                items['image'] = image

                yield items
