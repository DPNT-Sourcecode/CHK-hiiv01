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

    combination_purchase_prices = {
        "A": [(5, 200), (3, 130)],
        "B": [(2, 45)]
    }

    bogof_offers = {
        "E": (2, "B")
    }

    if not all(product in product_prices for product in skus):
        return -1

    product_counts = Counter(skus)

    for product, (required_quantity, free_item) in bogof_offers.items():
        if product in product_counts:
            number_of_free_items = product_counts[product] // required_quantity


    total_price: int = 0

    for product, count in product_counts.items():
        if product in combination_purchase_prices:
            offer_count, offer_price = combination_purchase_prices[product]
            number_of_offers = count // offer_count
            remainder = count % offer_count
            total_price += number_of_offers * offer_price
            total_price += remainder * product_prices[product]
        else:
            total_price += count * product_prices[product]
    return total_price





