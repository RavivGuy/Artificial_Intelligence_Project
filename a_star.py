from typing import List

from Node import Node
from base_global_search import BaseGlobalSearch


class ASTAR(BaseGlobalSearch):
    def __init__(self, basic_order: List[int], side_length: int):
        super().__init__(basic_order, side_length)

    def get_solve_node(self) -> Node:
        pass