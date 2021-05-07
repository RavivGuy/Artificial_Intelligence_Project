from typing import Optional

from action_enum import Action
from state import State


class Node:
    def __init__(self, state: State, parent, action: Optional[Action]):
        self.state = state
        self.parent = parent
        self.action = action

    def __eq__(self, other):
        return isinstance(other,
                          Node) and self.state == other.state and self.action == other.action

    def __cmp__(self, other):
        return __cmp__((self.action, self.state), (other.action, other.state))

    def __gt__(self, other):
        return (self.action, self.state) > (other.action, other.state)

