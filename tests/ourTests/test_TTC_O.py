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


def test_optimal_change_result():
    s1 = {"c1": 50, "c2": 49, "c3": 1}
    s2 = {"c1": 48, "c2": 46, "c3": 6}
    instance = fairpyx.Instance(
        agent_capacities={"s1": 1, "s2": 1, "s3": 1},
        item_capacities={"c1": 1, "c2": 1, "c3": 1},
        valuations={"s1": s1, "s2": s2}
    )

    assert fairpyx.divide(fairpyx.algorithms.TTC_O_function, instance=instance) == {'s1': ['c2'], 's2': ['c1']}, "ERROR"


def test_student_get_k_courses():  # in ttc a student didn't get k cources
    s1 = {"c1": 50, "c2": 10, "c3": 40}
    s2 = {"c1": 45, "c2": 30, "c3": 25}
    s3 = {"c1": 49, "c2": 15, "c3": 36}
    instance = fairpyx.Instance(
        agent_capacities={"s1": 2, "s2": 2, "s3": 2},
        item_capacities={"c1": 2, "c2": 2, "c2": 2},
        valuations={"s1": s1, "s2": s2, "s3": s3}
    )

    assert fairpyx.divide(fairpyx.algorithms.TTC_O_function, instance=instance) == {'s1': ['c2', 'c3'], 's2': ['c1', 'c2'], 's3': ['c1', 'c3']}, "ERROR"


def test_optimal_improve_cardinal_and_ordinal_results():
    s1 = {"c1": 50, "c2": 30, "c3": 20}
    s2 = {"c1": 40, "c2": 50, "c3": 10}
    s3 = {"c1": 60, "c2": 10, "c3": 30}
    instance = fairpyx.Instance(
        agent_capacities={"s1": 2, "s2": 2, "s3": 2},
        item_capacities={"c1": 2, "c2": 3, "c3": 1},
        valuations={"s1": s1, "s2": s2, "s3": s3}
    )

    assert fairpyx.divide(fairpyx.algorithms.TTC_O_function, instance=instance) == {'s1': ['c1', 'c2'], 's2': ['c2', 'c3'],  's3': ['c1', 'c2']}, "ERROR"


def test_sub_round_within_sub_round():
    s1 = {"c1": 40, "c2": 10, "c3": 20, "c4": 30}
    s2 = {"c1": 50, "c2": 10, "c3": 15, "c4": 25}
    s3 = {"c1": 60, "c2": 30, "c3": 2, "c4": 8}
    instance = fairpyx.Instance(
        agent_capacities={"s1": 2, "s2": 2, "s3": 2},
        item_capacities={"c1": 1, "c2": 2, "c2": 2, "c4": 1},
        valuations={"s1": s1, "s2": s2, "s3": s3}
    )

    assert fairpyx.divide(fairpyx.algorithms.TTC_O_function, instance=instance) == {'s1': ['c3', 'c4'], 's2': ['c1', 'c2'], 's3': ['c2', 'c3']}, "ERROR"


if __name__ == "__main__":
    pytest.main(["-v",__file__])
