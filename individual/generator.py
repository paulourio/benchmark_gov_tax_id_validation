import numpy as np
import numba


@numba.jit
def generate_ids(size: int, valid_prob: float = 0.5,
                 edge_case_prob: float = 0.1,
                 seed: int = 9423477) -> np.ndarray:
    np.random.seed(seed)
    data = np.random.randint(1, 999_999_999, size)
    for i, datum in enumerate(data):
        cd = get_check_digits(datum)
        if np.random.rand() <= valid_prob:
            data[i] = data[i]*100 + cd 
        elif np.random.rand() <= edge_case_prob:  
            data[i] = int(str(data[i]%10) * 11)
        else:
            cd = (cd + np.random.randint(1, 99)) % 100
            data[i] = data[i]*100 + cd
    return format_int_id(data)


@numba.jit(nopython=True)
def get_check_digits(x: int) -> int:
    """Return the two check digits for an individual tax id.

    Parameters
    ----------
    x : str
        The first 9 digits of individual tax id.

    Returns
    -------
    int
        Integer in domain [0, 99] representing the two check digits.
    """
    s = 0
    r = x
    for j in range(2, 11):
        s += j * (r % 10)
        r //= 10
    d1 = (s*10) % 11
    if d1 == 10:
        d1 = 0
    s = 0
    r = x
    for j in range(3, 12):
        s += j * (r % 10)
        r //= 10
    s += 2 * d1
    d2 = (s*10) % 11
    if d2 == 10:
        d2 = 0
    return d1*10 + d2


format_int_id = np.vectorize(lambda x: f'{x:011d}')
