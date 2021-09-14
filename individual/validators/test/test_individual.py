from hypothesis import given, note, strategies as st
import logging

import numpy as np

import individual


def _all_ne(x: int) -> bool:
    """Return True when the least 9 digits are not all equal."""
    first = x % 10
    for i in range(8):
        x //= 10
        if x % 10 != first:
            return True
    return False


_VALID_CASES = [
    '00000485500',
    '00000000191',
]


@given(st.integers(min_value=0, max_value=999_999_999).filter(_all_ne),
       st.sampled_from(list(individual.get_validators().keys())))
def test_validators(tax_id, method):
    impl = individual.get_validators()[method]

    check_digits = individual.get_check_digits(tax_id)
    tax_id = tax_id * 100 + check_digits
    fmt_id = str(individual.format_int_id(tax_id))
    assert impl(fmt_id) is True

    # assert individual.get_check_digits(12955) == 0
    # invalid_cd = (check_digits + np.random.randint(5, 99)) % 100
    # print(tax_id, check_digits, 'distorted to', invalid_cd)
    # invalid_tax_id = tax_id * 100 + invalid_cd
    # invalid_fmt_id = str(individual.format_int_id(invalid_tax_id))
    # assert impl(invalid_fmt_id) is False


@given(st.sampled_from(_VALID_CASES),
       st.sampled_from(list(individual.get_validators().keys())))
def test_validators_specific_cases(tax_id, method):
    impl = individual.get_validators()[method]
    assert impl(tax_id) is True
