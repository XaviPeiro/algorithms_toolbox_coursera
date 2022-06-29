from tasks.greedy_algorithims import money_change, max_value_loot


def test_money_change():
    assert money_change(11) == 2
    assert money_change(10) == 1
    assert money_change(0) == 0
    assert money_change(21) == 3
    assert money_change(3) == 3
    assert money_change(8) == 4


def test_max_value_of_loot():
    items_store_1 = {
        60: 20,
        100: 50,
        120: 30
    }
    items_store_2 = {
        500: 30,
    }
    assert max_value_loot(prods_count=3, bag_items_capacity=50, prods=items_store_1) == 180.0
    assert max_value_loot(prods_count=3, bag_items_capacity=30, prods=items_store_1) == 120.0
    assert max_value_loot(prods_count=1, bag_items_capacity=10, prods=items_store_2) == 166.6667

