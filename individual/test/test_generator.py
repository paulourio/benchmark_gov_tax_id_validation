from individual import get_check_digits


def test_individual_get_check_digits():
    # Edge cases
    for i in range(10):
        assert get_check_digits(int(f'{i}' * 9)) == int(f'{i}' * 2)
    # Random cases
    assert get_check_digits(452671545) == 4
    assert get_check_digits(577813782) == 61
    assert get_check_digits(831720547) == 99
    assert get_check_digits(756377921) == 35
    assert get_check_digits(191) == 0
    assert get_check_digits(485500) == 0
    assert get_check_digits(845655) == 0
    assert get_check_digits(12955) == 0

