# funda-scraper
Scrape dutch real estate website funda

## How to use the scraper
1. Clone the repository
2. run `pip install -r requirements.txt` (you'll need at least python 3.6)
3. Edit the config.json (See [config](###config) for more information)
4. Run `scrapy crawl funda_listings -o output.csv` to get a CSV of outputs on the first page of Funda. 
4. (optional) Alternatively you can save it as a json, xml or a bunch of other extensions by simply changing the extension. See: https://docs.scrapy.org/en/latest/topics/feed-exports.html for more information


### config.json
In the config.json you can edit the search parameters. Here are they in detail:

- `listing_type`: Either `"for_sale"` or `"for_rent"`
- `city`: Either `"heel-nederland"` for all of the Netherlands or a city
- `only_available`: Either `true` or `false`, whether you want to see available houses only, or also include reserved and sold houses
- `extra_search_range`: An integer representing the extra distance (in kilometers) from your chosen city you want to search for houses
- `minimum_price`: An integer to specify the minimum sale (or rent) price of the house
- `maximum_price`: An integer to specify the maximum sale (or rent) price of the house. If it's `0` or `null` it will have no maximum
- `minimum_house_size`: An integer to specify the minimum house size (in m²)
- `maximum_house_size`: An integer to specify the maximum house size (in m²). If it's `0` or `null` it will have no maximum
- `minimum_plot_size`: An integer to specify the minimum plot size (in m²)
- `maximum_plot_size`: An integer to specify the maximum plot size (in m²). If it's `0` or `null` it will have no maximum
- `minimum_rooms`: An integer to specify the minimum number of rooms.
- `maximum_rooms`: An integer to specify the maximum number of rooms. If it's `0` or `null` it will have no maximum
- `minimum_bedrooms`: An integer to specify the minimum number of bedrooms
- `maximum_bedrooms`: An integer to specify the maximum number of bedrooms. If it's `0` or `null` it will have no maximum
- `type_of_house`: The type of house you are searching. If it's `null` it will search for all types. This is usually `woonhuis` (house) or `appartement` (apartment) but can be either of the following: 
- - `woonhuis` (house)
  - `appartement` (apartment)
  - `parkeergelegenheid` (parking space)
  - `bouwgrond` (land)
  - `opslagruimte` (storage space)
  - `berging` (storage, but in someone's house)
  - `ligplaats` (berth)
  - `onderstuk` (substructure)


## TODO's
This project is a work in progress. It will currently run, but I have a bunch of extra features planned

- Notify user when new listing is available
- Go multiple pages deep
- Scrape more detailed information of a listing (more pictures, VVE, year of construction, detailed layout etc.)
- Data analysis
