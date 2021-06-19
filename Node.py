from typing import Optional

from action_enum import Action
from state import State


class Node:
    def __init__(self, state: State, parent, action: Optional[Action], create_time: float):
        self.state = state
        self.parent = parent
        self.action = action
        self.create_time = create_time

    def __eq__(self, other):
        return isinstance(other,
                          Node) and self.state == other.state and self.action == other.action

    def __gt__(self, other):
        return (self.create_time, self.action) > (other.create_time, other.action)

