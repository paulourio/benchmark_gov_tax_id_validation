from individual.validators import baseline, unrolled
from typing import Callable, Dict, Final, List 

from .baseline import baseline_validate, baseline_set_validate
from .baseline_cython import baseline_set_cython_validate
from .unrolled import unrolled_validate, unrolled_regex_validate
from .unrolled_cython import unrolled_cython_validate
from .unrolled_cython import unrolled_regex_cython_validate


Validator = Callable[[str], bool]


def get_validators() -> Dict[str, Validator]:
    return _METHODS.copy()


_METHODS: Final[Dict[str, Validator]] = {
    'baseline': baseline_validate,
    'baseline+set': baseline_set_validate,
    'baseline+set+cython': baseline_set_cython_validate,
    'unrolled': unrolled_validate,
    'unrolled+regex': unrolled_regex_validate,
    'unrolled+cython': unrolled_cython_validate,
    'unrolled+regex+cython': unrolled_regex_cython_validate,
}