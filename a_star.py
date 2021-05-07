from typing import List, Tuple
import heapq
from Node import Node
from base_global_search import BaseGlobalSearch


class AStar(BaseGlobalSearch):
    def __init__(self, basic_order: List[int], side_length: int):
        self.close_list: List[Node] = []
        self.open_list: List[Tuple[int, int, Node]] = []
        super().__init__(basic_order, side_length)

    def get_solve_node(self) -> Node:
        manhattan_dist = self.initial_node.state.get_manhattan_dist()
        heapq.heappush(self.open_list, (manhattan_dist, 0, self.initial_node))

        while self.open_list:
            popped_item = heapq.heappop(self.open_list)
            node = popped_item[2]
            if node.state == self.goal_state:
                return node

            state = node.state
            state_neighbors = state.get_neighbors()

            for neighbor in state_neighbors:
                neighbor_node = Node(neighbor[1], node, neighbor[0])
                if neighbor_node not in self.close_list:
                    self.close_list.append(neighbor_node)
                    manhattan_dist = neighbor_node.state.get_manhattan_dist()
                    path_len = popped_item[1] + 1
                    full_dist = manhattan_dist + path_len
                    heapq.heappush(self.open_list, (full_dist, path_len, neighbor_node))
