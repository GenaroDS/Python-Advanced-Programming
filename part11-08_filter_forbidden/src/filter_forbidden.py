# WRITE YOUR SOLUTION HERE:
def filter_forbidden(string: str, forbidden: str):
    result = "".join([character for character in string if character not in forbidden])
    return result

