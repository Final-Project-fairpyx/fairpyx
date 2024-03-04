from itertools import cycle
from fairpyx import Instance, AllocationBuilder

import logging
logger = logging.getLogger(__name__)

def SP(alloc: AllocationBuilder) -> list[list[any]]:
    """
    "Optimization-based Mechanisms for the Course Allocation Problem", by Hoda Atef Yekta, Robert Day (2020) .https://doi.org/10.1287/ijoc.2018.0849
    Algorethem 2: Allocate the given items to the given agents using the SP protocol.
    :param alloc: an allocation builder, which tracks the allocation and the remaining capacity for items and agents of
     the fair course allocation problem(CAP).


    >>> from fairpyx.adaptors import divide
    >>> s1 = {"c1": 50, "c2": 49, "c3": 1}
    >>> s2 = {"c1": 48, "c2": 46, "c3": 6}
    >>> agent_capacities = {"s1": 1, "s2": 1}                                 # 2 seats required
    >>> course_capacities = {"c1": 1, "c2": 1, "c3": 1}                       # 3 seats available
    >>> valuations = {"s1": s1, "s2": s2}
    >>> instance = Instance(agent_capacities=agent_capacities, item_capacities=course_capacities, valuations=valuations)
    >>> divide(SP, instance=instance)
    {'s1': ['c1'], 's2': ['c2']}
    """
    return 0


