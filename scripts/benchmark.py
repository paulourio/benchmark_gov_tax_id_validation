from functools import partial
import timeit

import numba
import numpy as np

import individual


def run():
    data = individual.generate_ids(
        size=10_000,
        valid_prob=0.5,
        edge_case_prob=0.1,
        seed=9423477
    )
    for name, entry in individual.get_validators().items():
        t = timeit.Timer(partial(_trial, entry, data))
        print(f'{name}: {t.timeit(1_000) / 1_000:.4f}s')


@numba.jit
def _trial(fn: individual.Validator, data: np.ndarray):
    for datum in data:
        fn(str(datum))


if __name__ == '__main__':
    run()
