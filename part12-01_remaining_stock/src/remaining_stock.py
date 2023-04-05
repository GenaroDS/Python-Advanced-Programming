# Write your solution here:
def sort_by_remaining_stock(items: list):
    # helper function defined within the function
    def order_by_price(item: tuple):
        return item[2]

    return sorted(items, key=order_by_price)

