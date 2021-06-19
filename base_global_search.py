import math
from datetime import datetime
from typing import List

from Node import Node
from action_enum import Action
from state import State

from abc import ABC, abstractmethod


class BaseGlobalSearch(ABC):
    """
    base class for all global search algorithms
    """
    def __init__(self, basic_order: List[int], side_length: int):
        self.side_length: int = side_length
        self.initial_state: State = State(basic_order, side_length)
        create_time = datetime.timestamp(datetime.now())
        self.initial_node: Node = Node(self.initial_state, None, None, create_time)
        order: List[int] = list(range(1, int(math.pow(side_length, 2))))
        order.append(0)
        self.goal_state: State = State(order, side_length)
        self.solve_node: Node = self.get_solve_node()

    """
    :return the solution actions from the beginning to the end
    """
    def get_solve_moves(self) -> List[Action]:
        node = self.solve_node
        moves = []
        while node.parent:
            moves.insert(0, node.action)
            node = node.parent
        return moves

    """
    abstract method that all inherited algorithms need to implement
    :return the solve node that contain the solve path
    """
    @abstractmethod
    def get_solve_node(self):
        pass
