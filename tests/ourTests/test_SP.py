
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

    assert fairpyx.divide(fairpyx.algorithms.SP_function , instance=instance) == {'s1': ['c1'], 's2': ['c2']}, "ERROR"


def test_optimal_change_result():
    s1 = {"c1": 50, "c2": 49, "c3": 1}
    s2 = {"c1": 48, "c2": 46, "c3": 6}
    instance = fairpyx.Instance(
        agent_capacities={"s1": 1, "s2": 1, "s3": 1},
        item_capacities={"c1": 1, "c2": 1, "c3": 1},
        valuations={"s1": s1, "s2": s2}
    )

    assert fairpyx.divide(fairpyx.algorithms.TTC_function, instance=instance) == {'s1': ['c1'], 's2': ['c2']}, "ERROR"


def test_sub_round_within_round():
    s1 = {"c1": 44, "c2": 39, "c3": 17}
    s2 = {"c1": 50, "c2": 45, "c3": 5}
    s3 = {"c1": 45, "c2": 40, "c3": 15}
    instance = fairpyx.Instance(
        agent_capacities={"s1": 1, "s2": 1, "s3": 1},
        item_capacities={"c1": 1, "c2": 1, "c3": 1},
        valuations={"s1": s1, "s2": s2, "s3": s3}
    )

    assert fairpyx.divide(fairpyx.algorithms.TTC_function, instance=instance) == {'s1': ['c3'], 's2': ['c1'], 's3': ['c2']}, "ERROR"


def test_students_with_the_same_list():
    s1 = {"c1": 55, "c2": 45}
    s2 = {"c1": 55, "c2": 45}
    instance = fairpyx.Instance(
        agent_capacities={"s1": 1, "s2": 1},
        item_capacities={"c1": 1, "c2": 1},
        valuations={"s1": s1, "s2": s2}
    )

    assert fairpyx.divide(fairpyx.algorithms.TTC_function, instance=instance) == {'s1': ['c1'], 's2': ['c2']}, "ERROR"


def test_student_bids_the_same_for_different_courses():
    s1 = {"c1": 50, "c2": 50}
    s2 = {"c1": 40, "c2": 60}
    s3 = {"c1": 71, "c2": 25}
    instance = fairpyx.Instance(
        agent_capacities={"s1": 1, "s2": 1, "s3": 1},
        item_capacities={"c1": 2, "c2": 1},
        valuations={"s1": s1, "s2": s2, "s3": s3}
    )

    assert fairpyx.divide(fairpyx.algorithms.TTC_function, instance=instance) == {'s1': ['c1'], 's2': ['c2'], 's3': ['c1']}, "ERROR"


def test_different_k_for_students():
    s1 = {"c1": 400, "c2": 200, "c3": 150, "c4": 130, "c5": 120}
    s2 = {"c1": 160, "c2": 350, "c3": 150, "c4": 140, "c5": 200}
    s3 = {"c1": 300, "c2": 250, "c3": 110, "c4": 180, "c5": 160}
    s4 = {"c1": 280, "c2": 250, "c3": 180, "c4": 130, "c5": 160}
    s5 = {"c1": 140, "c2": 180, "c3": 270, "c4": 250, "c5": 160}
    s6 = {"c1": 150, "c2": 250, "c3": 200, "c4": 260, "c5": 140}
    s7 = {"c1": 250, "c2": 180, "c3": 210, "c4": 200, "c5": 160}
    instance = fairpyx.Instance(
        agent_capacities={"s1": 1, "s2": 1, "s3": 2, "s4": 3, "s5": 3, "s6": 4, "s7": 1},
        item_capacities={"c1": 2, "c2": 5, "c3": 4, "c4": 3, "c5": 2},
        valuations={"s1": s1, "s2": s2, "s3": s3, "s4": s4, "s5": s5, "s6": s6, "s7": s7}
    )

    assert fairpyx.divide(fairpyx.algorithms.TTC_function, instance=instance) == {'s1': ['c1'], 's2': ['c2'], 's3': ['c1', 'c2'], 's4': ['c2', 'c3', 'c5'], 's5': ['c2', 'c3', 'c4'], 's6': ['c2', 'c3', 'c4', 'c5'], 's7': ['c3']}, "ERROR"


if __name__ == "__main__":
    pytest.main(["-v",__file__])
