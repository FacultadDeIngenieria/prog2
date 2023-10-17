limit = 10
multiples = [2, 3]

list_of_numbers = range(0, limit)

# def is_multiple_of(multiples: List[int]) ->

filtered_list_of_numbers = list(filter(lambda x: is_multiple_of(x, multiples), list_of_numbers))

def is_multiple_of(x: int, multiples: List[int]) -> bool:
    booleans = map(lambda x: x % multiples == 0, multiples)
    return reduce(lambda x, y: x or y, booleans)
