# Write your solution here
def search(products: list, criterion: callable):
    result = []
    for product in products:
        if criterion(product):
            result.append(product)
    return result


