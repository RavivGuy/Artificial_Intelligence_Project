import math
from datetime import datetime
from typing import List

from Node import Node
from base_global_search import BaseGlobalSearch


class IDS(BaseGlobalSearch):
    def __init__(self, basic_order: List[int], side_length: int):
        self.close_list: List[Node] = []
        super().__init__(basic_order, side_length)

    def get_solve_node(self) -> Node:
        # max depth is factorial of side_length^2
        # (the number of ways to order side_length^2 in a row)
        max_depth = math.factorial(math.pow(self.side_length, 2))

        for i in range(max_depth):
            # every dfs_with_limit need to empty the close list
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

        create_time = datetime.timestamp(datetime.now())
        for neighbor in state_neighbors:
            neighbor_node = Node(neighbor[1], curr_node, neighbor[0], create_time)
            if neighbor_node not in self.close_list:
                sol_node = self.dfs_with_limit(neighbor_node, limit-1)
                if sol_node:
                    return sol_node
        return None




