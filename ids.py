import math
from typing import List, Tuple

from Node import Node
from base_global_search import BaseGlobalSearch


class IDS(BaseGlobalSearch):
    def __init__(self, basic_order: List[int], side_length: int):
        self.close_list: List[Node] = []
        super().__init__(basic_order, side_length)

    def get_solve_node(self) -> Node:
        max_depth = math.factorial(math.fabs(self.side_length))

        for i in range(max_depth):
            self.close_list: List[Node] = []
            sol_node = self.dfs_with_limit(self.initial_node, i)
            if sol_node:
                return sol_node

    def dfs_with_limit(self, curr_node: Node, limit: int) -> Node:
        if curr_node.state == self.goal_state:
            return curr_node

        if limit == 0:
            return None

        self.close_list.append(curr_node)
        state = curr_node.state
        state_neighbors = state.get_neighbors()

        for neighbor in state_neighbors:
            neighbor_node = Node(neighbor[1], curr_node, neighbor[0])
            if neighbor_node not in self.close_list:
                sol_node = self.dfs_with_limit(neighbor_node, limit-1)
                if sol_node:
                    return sol_node
        return None




