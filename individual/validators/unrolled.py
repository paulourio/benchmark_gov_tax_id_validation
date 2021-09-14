import re


def unrolled_validate(tax_id: str) -> bool:
    if len(tax_id) != 11:
        return False
    x = [0] * 11
    for i in range(11):
        x[i] = ord(tax_id[i]) - ord('0')
    m = ((10*x[0] + 9*x[1] + 8*x[2] + 7*x[3] + 6*x[4]
          + 5*x[5] + 4*x[6] + 3*x[7] + 2*x[8]) * 10) % 11
    if not (m == x[9] or (m == 10 and x[9] == 0)):
        return False
    m = ((11*x[0] + 10*x[1] + 9*x[2] + 8*x[3] + 7*x[4]
          + 6*x[5] + 5*x[6] + 4*x[7] + 3*x[8] + 2*x[9]) * 10) % 11
    if not (m == x[10] or (m == 10 and x[10] == 0)):
        return False
    first = x[0]
    for i in range(1, 11):
        if x[i] != first:
            return True
    return False


def unrolled_regex_validate(tax_id: str) -> bool:
    if len(tax_id) != 11:
        return False
    x = [0] * 11
    for i in range(11):
        x[i] = ord(tax_id[i]) - ord('0')
    m = ((10*x[0] + 9*x[1] + 8*x[2] + 7*x[3] + 6*x[4]
          + 5*x[5] + 4*x[6] + 3*x[7] + 2*x[8]) * 10) % 11
    if not (m == x[9] or (m == 10 and x[9] == 0)):
        return False
    m = ((11*x[0] + 10*x[1] + 9*x[2] + 8*x[3] + 7*x[4]
          + 6*x[5] + 5*x[6] + 4*x[7] + 3*x[8] + 2*x[9]) * 10) % 11
    if not (m == x[10] or (m == 10 and x[10] == 0)):
        return False
    return _all_eq_pat.match(tax_id) is None


_all_eq_pat = re.compile(r'^(\d)\1+$')
