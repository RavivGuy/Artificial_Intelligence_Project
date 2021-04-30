import math
from collections import defaultdict
from optparse import Option
from typing import List

from Node import Node
from state import State


class PuzzleGraph:
    def __init__(self, basic_order: List[int],side_length: int):
        self.side_length = side_length
        self.initial_state = State(basic_order, side_length)
        self.initial_node = Node(self.initial_state, None, None)
        self.graph_nodes: List[Node] = []
        self._init_graph_nodes(self.initial_node)

    def _init_graph_nodes(self, node: Node):
        self.graph_nodes.append(node)
        state = node.state
        state_neighbors = state.get_neighbors()

        for neighbor in state_neighbors:
            neighbor_node = Node(neighbor[1], node, neighbor[0])
            if neighbor_node not in self.graph_nodes:
                self._init_graph_nodes(neighbor_node)