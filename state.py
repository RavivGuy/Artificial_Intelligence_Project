import math
import random
from copy import deepcopy
from typing import List, Tuple

from action_enum import Action


class State:
    def __init__(self, order: List[int], side_length: int):
        self.order: List[int] = order
        self.side_length: int = side_length

    def __eq__(self, other):
        return isinstance(other, State) and self.order == other.order and self.side_length == other.side_length

    def __gt__(self, other):
        return (self.order, self.side_length) > (other.order, other.side_length)

    def get_neighbors(self):
        row_index, column_index = self._get_number_indexes(0)
        valid_actions = self._get_valid_actions(row_index, column_index)
        random.shuffle(valid_actions)

        return [(valid_action, self._get_new_state_for_action(valid_action)) for valid_action in valid_actions]

    def get_manhattan_dist(self):
        man_sum = 0
        for i in range(0, len(self.order)):
            row_index, column_index = self._get_number_indexes(i)
            goal_row_index, goal_column_index = self._get_goal_indexes(i)
            man_sum += math.fabs(row_index - goal_row_index) + math.fabs(column_index - goal_column_index)
        return man_sum

    def _get_new_state_for_action(self, action: Action):
        try:
            order_copy = deepcopy(self.order)
            zero_index = self._get_number_index(0)
            if action == Action.LEFT:
                order_copy[zero_index] = order_copy[zero_index + 1]
                order_copy[zero_index + 1] = 0
            if action == Action.RIGHT:
                order_copy[zero_index] = order_copy[zero_index - 1]
                order_copy[zero_index - 1] = 0
            if action == Action.UP:
                order_copy[zero_index] = order_copy[zero_index + self.side_length]
                order_copy[zero_index + self.side_length] = 0
            if action == Action.DOWN:
                order_copy[zero_index] = order_copy[zero_index - self.side_length]
                order_copy[zero_index - self.side_length] = 0
            return State(order_copy, self.side_length)
        except Exception as e:
            print('a')

    def _get_valid_actions(self, row_index: int, column_index: int) -> List[Action]:
        valid_action = []

        if self.side_length == 1:
            return valid_action

        if row_index != 0:
            valid_action.append(Action.DOWN)
        if row_index != self.side_length - 1:
            valid_action.append(Action.UP)
        if column_index != self.side_length - 1:
            valid_action.append(Action.LEFT)
        if column_index != 0:
            valid_action.append(Action.RIGHT)

        return valid_action

    def _get_number_indexes(self, number: int):
        num_index = self._get_number_index(number)
        row_index = int(num_index / self.side_length)
        column_index = num_index % self.side_length
        return row_index, column_index

    def _get_number_index(self, number: int):
        zero_index = self.order.index(number)
        return zero_index

    def _get_goal_indexes(self, number: int):
        if number == 0:
            return self.side_length - 1, self.side_length - 1
        row_index = int(number - 1 / self.side_length)
        column_index = number - 1 % self.side_length
        return row_index, column_index
