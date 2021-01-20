import scrapy


class BasicHouseItem(scrapy.Item):
    url = scrapy.Field()
    address = scrapy.Field()
    zipcode = scrapy.Field()
    price = scrapy.Field()
    house_size = scrapy.Field()
    plot_size = scrapy.Field()
    rooms = scrapy.Field()
    image = scrapy.Field()
