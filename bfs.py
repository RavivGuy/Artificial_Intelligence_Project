import math
from typing import List

from Node import Node
from state import State


class BFS:
    def __init__(self, basic_order: List[int], side_length: int):
        self.side_length = side_length
        self.initial_state = State(basic_order, side_length)
        self.initial_node = Node(self.initial_state, None, None)
        self.close_list: List[Node] = []
        self.open_list: List[Node] = []
        order = list(range(1, int(math.pow(side_length, 2))))
        order.append(order)
        self.goal_state = State(order, side_length)
        self._init_graph_nodes(self.initial_node)

    def _init_graph_nodes(self, node: Node):
        # self.graph_nodes.append(node)
        while node.state != self.goal_state:
            self.close_list.append(node)
            state = node.state
            state_neighbors = state.get_neighbors()

            for neighbor in state_neighbors:
                neighbor_node = Node(neighbor[1], node, neighbor[0])
                if neighbor_node not in self.close_list:
                    self.open_list.append(neighbor_node)

            node = self.open_list.pop()