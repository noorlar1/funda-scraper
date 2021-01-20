import json


def generate_url():
    # TODO: Structure this method better and do some cleanup

    with open("config.json", "r") as f:
        config = json.loads(f.read())

    if config['listing_type'] in ['for_rent', 'rent', 'huur']:
        listing_type = 'huur'
    else:
        listing_type = 'koop'

    city = config['city'].replace(' ', '-').lower()

    only_available = "beschikbaar" if config['only_available'] else ""

    minimum_price = config['minimum_price']
    maximum_price = config['maximum_price']
    if maximum_price:
        price = f"{minimum_price}-{maximum_price}"
    else:
        price = f"{minimum_price}+"

    extra_search_range = f"+{config['extra_search_range'] or 0}km"

    minimum_house_size = config['minimum_house_size']
    maximum_house_size = config['maximum_house_size']
    if maximum_house_size and maximum_house_size > 0:
        house_size = f"{minimum_house_size}-{maximum_house_size}-woonopp"
    else:
        house_size = f"{minimum_house_size}+woonopp"

    minimum_plot_size = config['minimum_plot_size']
    maximum_plot_size = config['maximum_plot_size']
    if maximum_plot_size and maximum_plot_size > 0:
        plot_size = f"{minimum_plot_size}-{maximum_plot_size}-perceelopp"
    else:
        plot_size = f"{minimum_plot_size}+perceelopp"

    minimum_rooms = config['minimum_rooms']
    maximum_rooms = config['maximum_rooms']
    if maximum_rooms and maximum_rooms > 0:
        rooms = f"{minimum_rooms}-{maximum_rooms}-kamers"
    else:
        rooms = f"{minimum_rooms}+kamers"

    minimum_bedrooms = config['minimum_bedrooms']
    maximum_bedrooms = config['maximum_bedrooms']
    if maximum_bedrooms and maximum_bedrooms > 0:
        rooms = f"{minimum_bedrooms}-{maximum_bedrooms}-slaapkamers"
    else:
        rooms = f"{minimum_bedrooms}+slaapkamers"

    type_of_house = config['type_of_house'] or ""

    return f"https://www.funda.nl/{listing_type}/{city}/{price}/{extra_search_range}/{house_size}/{plot_size}/{rooms}/{type_of_house}/{only_available}/"
