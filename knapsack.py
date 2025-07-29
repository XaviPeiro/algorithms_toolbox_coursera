"""
Knapsack

Take the maximum value given:
- set of items with different values.
- A limit weight you can bear

e.g.:
1
---
A : 1, 10kg, 100$
B : 1, 15kg, 300$
C : 1, 20kg, 202$

limit 35kgs => B+C
$$$
2
---
A: 25, 6kg, 100$
B: 15, 4kg, 70$

limit 9kgs => 2*B
$$$
"""


def knapsack(limit: int, items: dict) -> dict:
    valid_options = []
    for item_name, values in items.items():
        if values["weight"] <= limit and values["number"] > 0:
            for valid_option in valid_options:
                if values["number"] > 0:
                    if valid_option["remaining_space"] - values["weight"] >= 0:
                        valid_option["items"] |= {
                            item_name: valid_option["items"].get(item_name, 0)+1
                        }  # merging -> O(n)
                        valid_option["value"] += 
                        values["number"] -= 1


            valid_options.append({
                "items": {item_name: 1},
                "remaining_space": limit-values["weight"],
                "value": values["value"]
            })
            items[item_name]["number"] -= 1

    biggest = float("-inf")
    for valid_option in valid_options:
        max(biggest, )


if __name__ == '__main__':
    items = {
        "A": {"value": 100, "weight": 10, "number": 1},
        "B": {"value": 300, "weight": 15, "number": 1},
        "C": {"value": 202, "weight": 20, "number": 1},
    }
    assert knapsack(limit=9, items=items) == {"B": 1, "C": 1}
    items = {
        "A": {"value": 100, "weight": 6, "number": 25},
        "B": {"value": 70, "weight": 4, "number": 15}
    }
    assert knapsack(limit=9, items=items) == {"B": 2}
