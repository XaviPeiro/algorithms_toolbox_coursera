from tasks.greedy_algorithims import money_change


def test_money_change():
    assert money_change(11) == 2
    assert money_change(10) == 1
    assert money_change(0) == 0
    assert money_change(21) == 3
    assert money_change(3) == 3
    assert money_change(8) == 4


