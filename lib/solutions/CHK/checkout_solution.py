from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    product_prices: dict[str: int] = {
        "A": 50,
        "B": 30,
        "C": 20,
        "D": 15
    }

    special_offer_prices: dict[str: tuple[int, int]] = {
        "A": (3, 130),
        "B": (2, 45)
    }

    if not all(product in product_prices for product in skus):
        return -1

    product_counts = Counter(skus)

    total_price: int = 0
    for product, count in product_counts.items():
        if product in special_offer_prices:
            offer_count, offer_price = special_offer_prices[product]
            number_of_offer = count // offer_count
            remainder = count % offer_count
            total_price += 







