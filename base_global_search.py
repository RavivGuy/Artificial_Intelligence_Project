import math
from typing import List

from Node import Node
from action_enum import Action
from state import State

from abc import ABC, abstractmethod


class BaseGlobalSearch(ABC):
    def __init__(self, basic_order: List[int], side_length: int):
        self.side_length: int = side_length
        self.initial_state: State = State(basic_order, side_length)
        self.initial_node: Node = Node(self.initial_state, None, None)
        order: List[int] = list(range(1, int(math.pow(side_length, 2))))
        order.append(0)
        self.goal_state: State = State(order, side_length)
        self.solve_node: Node = self.get_solve_node()

    def get_solve_moves(self) -> List[Action]:
        node = self.solve_node
        moves = []
        while node.parent:
            moves.insert(0, node.action)
            node = node.parent
        return moves

    @abstractmethod
    def get_solve_node(self):
        pass
