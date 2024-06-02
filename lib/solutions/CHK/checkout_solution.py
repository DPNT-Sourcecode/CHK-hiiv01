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
        "E": [(2, 0)]
    }

    if not all(product in product_prices for product in skus):
        return -1

    product_counts = Counter(skus)

    total_price: int = 0

    for product, count in product_counts.items():
        if product in product_offers:
            for 
            offer_quantity_required, offer_price = product_offers[product]
            offers_applicable = count // offer_quantity_required
            remaining_products = count % offer_quantity_required
            total_price += offers_applicable * offer_price
            total_price += remaining_products * product_prices[product]
        else:
            total_price += count * product_prices[product]
    return total_price

