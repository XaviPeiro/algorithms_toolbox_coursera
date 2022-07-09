from tasks.greedy_algorithims.collecting_signatures import collecting_signatures
from tasks.greedy_algorithims.fuel_car import less_travels_fuel_car
from tasks.greedy_algorithims.max_ad_revenue import max_ad_revenue
from tasks.greedy_algorithims.max_value_of_the_loot import max_value_loot
from tasks.greedy_algorithims.money_change import money_change


def test_money_change():
    assert money_change(11) == 2
    assert money_change(10) == 1
    assert money_change(0) == 0
    assert money_change(21) == 3
    assert money_change(3) == 3
    assert money_change(8) == 4


def test_max_value_of_loot():
    items_store_1 = [
        (60, 20),
        (100, 50),
        (120, 30)
    ]
    items_store_2 = [
        (500, 30)
    ]
    assert max_value_loot(prods_count=3, bag_items_capacity=50, prods=items_store_1) == 180.0
    assert max_value_loot(prods_count=3, bag_items_capacity=30, prods=items_store_1) == 120.0
    assert max_value_loot(prods_count=1, bag_items_capacity=10, prods=items_store_2) == 166.6667


def test_car_fueling():
    assert less_travels_fuel_car(10, 3, [1, 2, 5, 9]) == -1
    assert less_travels_fuel_car(950, 400, [200, 375, 550, 750]) == 2
    assert less_travels_fuel_car(200, 250, [100, 150]) == 0
    assert less_travels_fuel_car(500, 200, [100, 200, 300, 400]) == 2


def test_max_ad_revenue():
    assert max_ad_revenue([23], [39]) == 23 * 39 == 897
    assert max_ad_revenue([1, 3, -5], [-2, 4, 1]) == (3 * 4) + (1 * 1) + (-5 * -2) == 23
    assert max_ad_revenue([1, 3, 5], [2, 4, 1]) == (3 * 2) + (1 * 1) + (5 * 4) == 27


def test_collecting_signatures():
    assert len(collecting_signatures(segments=[(1, 3), (2, 5), (3, 6)])) == 1
    assert collecting_signatures(segments=[(1, 3), (2, 5), (3, 6)]) == [3]
    assert collecting_signatures(segments=[(4, 7), (1, 3), (2, 5), (5, 6)]) == [3, 6]
    assert len(collecting_signatures(segments=[(4, 7), (1, 3), (2, 5), (5, 6)])) == 2
