from number_of_provinces import NumberOfProvinces


def test_number_of_provinces():
    number_of_provinces = NumberOfProvinces()

    first = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    assert number_of_provinces.number_of_provinces(first) == 2

    second = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    assert number_of_provinces.number_of_provinces(second) == 3
