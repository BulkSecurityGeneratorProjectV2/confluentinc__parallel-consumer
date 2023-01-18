#
# Copyright (C) 2020-2023 Confluent, Inc.
#

import time
from functools import wraps
from random import randint
from typing import Callable


def timeit(fn: Callable):
    @wraps(fn)
    def inner_log_time(*args, **kwargs):
        start_time = time.process_time()
        result = fn(*args, **kwargs)
        end_time = time.process_time()
        time_elapsed = end_time - start_time
        print(f"{fn.__name__} executed in {time_elapsed} seconds")
        return result

    return inner_log_time


def sleep_a_bit():
    time.sleep(randint(0, 5) / 1000)