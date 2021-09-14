import re


_EDGE_CASES = {d*11 for d in range(10)}


def baseline_set_cython_validate(tax_id: str) -> bool:
    # Check if type is str
    if not isinstance(tax_id, str):
        return False

    # Remove some unwanted characters
    # tax_id = re.sub("[^0-9]",'',tax_id)

    # Verify if CPF number is equal
    if tax_id in _EDGE_CASES:
        return False

    # Checks if string has 11 characters
    if len(tax_id) != 11:
        return False

    sum = 0
    weight = 10

    # Calculating the first tax_id check digit.
    for n in range(9):
        sum = sum + int(tax_id[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 - sum % 11

    if verifyingDigit > 9:
        firstVerifyingDigit = 0
    else:
        firstVerifyingDigit = verifyingDigit

    # Calculating the second check digit of tax_id.
    sum = 0
    weight = 11
    for n in range(10):
        sum = sum + int(tax_id[n]) * weight

        # Decrement weight
        weight = weight - 1

    verifyingDigit = 11 - sum % 11

    if verifyingDigit > 9:
        secondVerifyingDigit = 0
    else:
        secondVerifyingDigit = verifyingDigit

    if tax_id[-2:] == "%s%s" % (firstVerifyingDigit, secondVerifyingDigit):
        return True
    return False
