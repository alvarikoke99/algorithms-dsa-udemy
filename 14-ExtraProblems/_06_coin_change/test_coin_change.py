from coin_change import CoinChange


def test_coin_change():
    c = CoinChange()

    assert c.coin_change([1, 2, 5], 11) == 3
    assert c.coin_change([2], 3) == -1
