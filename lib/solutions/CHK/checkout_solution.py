from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    product_prices = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15,
        "E": 40
    }

    product_offers = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)],
        "E": [(2, "B")]
    }

    if not all(product in product_prices for product in skus):
        return -1

    product_counts = Counter(skus)

    total_price: int = 0

    for product, count in product_counts.items():
        product_price = product_prices[product]
        if product in product_offers:
            offers = product_offers[product]
            for offer in offers:
                offer_count, offer_value = offer
                while count >= offer_count:
                    count -= offer_count
                    if isinstance(offer_value, int):
                        total_price += offer_value
                    elif offer_value in product_counts and product_counts[offer_value] > 0:
                        product_counts[offer_value] -= 1
                    else:
                        break
            total_price += count * product_price
        else:
            total_price += count * product_prices[product]
    return total_price

