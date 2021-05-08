import random
from typing import List

from Node import Node
from base_global_search import BaseGlobalSearch


class BFS(BaseGlobalSearch):
    def __init__(self, basic_order: List[int], side_length: int):
        self.close_list: List[Node] = []
        self.open_list: List[Node] = []
        super().__init__(basic_order, side_length)

    def get_solve_node(self) -> Node:
        self.open_list.append(self.initial_node)
        while self.open_list:
            node = self.open_list.pop()
            if node.state == self.goal_state:
                return node

            state = node.state
            state_neighbors = state.get_neighbors()
            random.shuffle(state_neighbors)

            for neighbor in state_neighbors:
                neighbor_node = Node(neighbor[1], node, neighbor[0])
                if neighbor_node not in self.close_list:
                    self.close_list.append(neighbor_node)
                    self.open_list.append(neighbor_node)
