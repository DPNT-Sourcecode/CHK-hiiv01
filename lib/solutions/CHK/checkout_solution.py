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
        "B": [(2, 45)]
    }

    if not all(product in product_prices for product in skus):
        return -1

    product_counts = Counter(skus)

    total_price: int = 0

    for product, count in product_counts.items():
        if product in product_offers:
            remaining_product_count = count
            for offer_quantity_required, offer_price in sorted(product_offers[product], reverse=True):
                offers_applicable = count // offer_quantity_required
                product_count = count % offer_quantity_required
                remaining_product_count -= remaining_product_count - product_count
                total_price += offers_applicable * offer_price
            total_price += remaining_product_count * product_prices[product]
        else:
            total_price += count * product_prices[product]

    number_free_b = min(product_counts.get("E", 0) // 2, product_counts.get("B", 0))
    total_price -= number_free_b * product_prices.get("B", 0)

    return total_price
