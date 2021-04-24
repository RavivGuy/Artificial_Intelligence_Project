from typing import List


class State:
    def __init__(self, order: List[int], neighbor_states: List[State]):
        self.order = order
        self.neighbor_states = neighbor_states