import random
from itertools import combinations

from tasks.greedy_algorithims.collecting_signatures import collecting_signatures
from tasks.greedy_algorithims.fuel_car import less_travels_fuel_car
from tasks.greedy_algorithims.max_ad_revenue import max_ad_revenue
from tasks.greedy_algorithims.max_value_of_the_loot import max_value_loot
from tasks.greedy_algorithims.maximum_number_of_prizes import maximum_number_of_prizes
from tasks.greedy_algorithims.maximum_salary import maximum_salary
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
    assert less_travels_fuel_car(
        destination=10,
        max_travel_distance=3,
        n_stops=4,
        stops=[1, 2, 5, 9]) == -1
    assert less_travels_fuel_car(950, 400, 4, [200, 375, 550, 750]) == 2
    assert less_travels_fuel_car(200, 250, 2, [100, 150]) == 0
    assert less_travels_fuel_car(700, 200, 4, [100, 200, 300, 400]) == -1


def test_max_ad_revenue():
    assert max_ad_revenue([23], [39]) == 23 * 39 == 897
    assert max_ad_revenue([1, 3, -5], [-2, 4, 1]) == (3 * 4) + (1 * 1) + (-5 * -2) == 23
    assert max_ad_revenue([1, 3, 5], [2, 4, 1]) == (3 * 2) + (1 * 1) + (5 * 4) == 27


def test_collecting_signatures():
    assert len(collecting_signatures(segments=[(1, 3), (2, 5), (3, 6)])) == 1
    assert collecting_signatures(segments=[(1, 3), (2, 5), (3, 6)]) == [3]
    assert collecting_signatures(segments=[(4, 7), (1, 3), (2, 5), (5, 6)]) == [3, 6]
    assert len(collecting_signatures(segments=[(4, 7), (1, 3), (2, 5), (5, 6)])) == 2


def test_maximum_number_of_prizes():
    assert maximum_number_of_prizes(6) == [1, 2, 3]
    assert maximum_number_of_prizes(8) == [1, 2, 5]
    assert maximum_number_of_prizes(9) == [1, 2, 6]
    assert maximum_number_of_prizes(2) == [2]


def test_maximum_salary():
    assert maximum_salary([12, 22, 23, 45]) == 45232212
    assert maximum_salary([21, 2]) == 221
    assert maximum_salary([2801, 2]) == 28012
    assert maximum_salary([227, 2]) == 2272
    assert maximum_salary([7591, 30, 22]) == 75913022
    assert maximum_salary([2223, 2]) == 22232
    assert maximum_salary([2221, 2]) == 22221
    assert maximum_salary([21, 2, 890]) == 890221
    assert maximum_salary([8172, 8613, 8889, 890, 89]) == 89890888986138172
    assert maximum_salary([9_000_000, 1]) == 90_000_001
    assert maximum_salary([1, 9_000_000]) == 90_000_001
    assert maximum_salary([9_900, 1]) == 99_001
    assert maximum_salary([89200, 899]) == 89989200
    assert maximum_salary([88270, 882]) == 88288270
    assert maximum_salary([89200]) == 89200
    assert maximum_salary([8200, 1341, 11, 2, 23, 12, 21, 2, 5, 5413_55623, 51_2351222, 2_3331]) == 8200_5_541355623_512351222_23331_23_2_2_21_1341_12_11
    assert maximum_salary([89200, 0, 10]) == 89200100
    assert maximum_salary([89200, 0, 10]) == 89200100
    assert maximum_salary([34, 4]) == 434
    assert maximum_salary([34, 2]) == 342
    assert maximum_salary([34, 3]) == 343
    assert maximum_salary([34, 2]) == 342
    assert maximum_salary([5428, 4090, 5967, 2402, 7019, 8791, 7868, 98, 6870, 5134, 9383, 7177, 898, 447, 3899, 1621, 6681, 4818, 4350,
      8446, 7057, 6074, 2956, 2179, 9019, 105, 856, 2796, 1180, 7563, 2943, 6777, 8431, 6129, 9391, 443, 4842, 7104,
      3800, 4665]) == 989391938390198988791856844684317868756371777104705770196870677766816129607459675428513448424818466544744343504090389938002956294327962402217916211180105
    i = [2, 8, 2, 3, 6, 4, 1, 1, 10, 6, 3, 3, 6, 1, 3, 8, 4, 6, 1, 10, 8, 4, 10, 4, 1, 3, 2, 3, 2, 6, 1, 5, 2, 9, 8, 5, 10, 8, 7, 9, 6, 4, 2, 6, 3, 8, 8, 9, 8, 2, 9, 10, 3, 10, 7, 5, 7, 1, 7, 5, 1, 4, 7, 6, 1, 10, 5, 4, 8, 4, 2, 7, 8, 1, 1, 7, 4, 1, 1, 9, 8, 6, 5, 9, 9, 3, 7, 6, 3, 10, 8, 10, 7, 2, 5, 1, 1, 9, 9, 5]
    assert maximum_salary(i) == 9999999998888888888887777777776666666666555555554444444443333333333222222222111111111111111101010101010101010
