"""
Test that course-allocation algorithms return a feasible solution.

Programmer: OFEK, TAMAR, MORIYA ESTER
Since:  2024-03
"""

import pytest

import fairpyx
import numpy as np


def test_feasibility():

    # TODO
    s1 = {"c1": 50, "c2": 49, "c3": 1}
    s2 = {"c1": 48, "c2": 46, "c3": 6}
    instance = fairpyx.Instance(
        agent_capacities = {"s1": 1, "s2": 1},
        item_capacities = {"c1": 1, "c2": 1, "c3": 1},
        valuations = {"s1": s1, "s2": s2}
        )

    assert fairpyx.divide(fairpyx.algorithms.TTC_O_function , instance=instance) == {'s1': ['c1'], 's2': ['c2']}, "ERROR"

if __name__ == "__main__":
    pytest.main(["-v",__file__])
