import scrapy


class BasicHouseItem(scrapy.Item):
    address = scrapy.Field()
    zipcode = scrapy.Field()
    price = scrapy.Field()
    house_size = scrapy.Field()
    plot_size = scrapy.Field()
    rooms = scrapy.Field()
    url = scrapy.Field()
    image = scrapy.Field()
    funda_id = scrapy.Field()
