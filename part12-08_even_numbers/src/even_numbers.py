def even_numbers(beginning: int, maximum: int):
    current = beginning
    if current % 2 != 0:
        current += 1
    while current <= maximum:
        yield current
        current += 2
