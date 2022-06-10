from tasks.generic_algorithms import __version__
from tasks.generic_algorithms.last_digit_of_a_large_fibonnaci_number import last_digit_of_a_large_fibonnaci_number
from tasks.generic_algorithms.last_digit_of_fibonnaci_number_again import last_digit_of_fibonaci_interval
from tasks.generic_algorithms.last_digit_of_square_fibonnaci_number import last_digit_of_fibonaci_squares


def test_version():
    assert __version__ == '0.1.0'


def test_last_digit_of_a_large_fibonnaci_number():
    assert last_digit_of_a_large_fibonnaci_number(0) == 0
    assert last_digit_of_a_large_fibonnaci_number(1) == 1
    assert last_digit_of_a_large_fibonnaci_number(2) == 2
    assert last_digit_of_a_large_fibonnaci_number(3) == 4
    assert last_digit_of_a_large_fibonnaci_number(4) == 7
    assert last_digit_of_a_large_fibonnaci_number(239) == 0
    assert last_digit_of_a_large_fibonnaci_number(832564823476) == 3
    assert last_digit_of_a_large_fibonnaci_number(1000) == 5


def test_last_digit_of_fibonaci_interval_1():
    assert last_digit_of_fibonaci_interval(1, 2) == 2
    assert last_digit_of_fibonaci_interval(1, 4) == 7
    assert last_digit_of_fibonaci_interval(3, 7) == 1
    assert last_digit_of_fibonaci_interval(10, 10) == 5
    assert last_digit_of_fibonaci_interval(10, 200) == 2
    assert last_digit_of_fibonaci_interval(1, 100000000) == 5


def test_last_digit_of_fibonaci_squares_1():
    assert last_digit_of_fibonaci_squares(0) == 0
    assert last_digit_of_fibonaci_squares(7) == 3
    assert last_digit_of_fibonaci_squares(1) == 1
    assert last_digit_of_fibonaci_squares(2) == 2
    assert last_digit_of_fibonaci_squares(3) == 6
    assert last_digit_of_fibonaci_squares(5) == 0
    assert last_digit_of_fibonaci_squares(613455) == 0
    assert last_digit_of_fibonaci_squares(10) == 5
    assert last_digit_of_fibonaci_squares(1000) == 5
    assert last_digit_of_fibonaci_squares(999999) == 0
    assert last_digit_of_fibonaci_squares(832564823476) == 9
