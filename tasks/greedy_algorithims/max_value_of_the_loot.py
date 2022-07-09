

def max_value_loot(prods_count: int, bag_items_capacity: int, prods: list) -> float:

    u_value_d: dict = {}
    for entry in prods:
        prod_value = entry[0]
        prod_count = entry[1]
        u_value: float = prod_value/prod_count
        u_value_d[u_value] = u_value_d.get(u_value, 0) + int(prod_count)

    u_value_d = dict(sorted(u_value_d.items(), reverse=True))
    res_value: int = 0
    for val, n in u_value_d.items():
        if bag_items_capacity == 0:
            break
        spaces_to_fill = min(bag_items_capacity, n)
        res_value += spaces_to_fill * val
        bag_items_capacity -= spaces_to_fill

    return round(res_value, ndigits=4)


if __name__ == "__main__":
    x = ""
    prods_count: [int, None] = None
    bag_items_capacity: [int, None] = None
    prods = []
    try:
        for line in iter(input, x):
            if (prods_count, bag_items_capacity) == (None, None):
                prods_count, bag_items_capacity = map(int, line.split())
            else:
                value, units = map(int, line.split())
                prods.append((value, units))
    except EOFError:
        ...

    res = max_value_loot(
            prods_count=prods_count,
            bag_items_capacity=bag_items_capacity,
            prods=prods
        )

    print(res)
