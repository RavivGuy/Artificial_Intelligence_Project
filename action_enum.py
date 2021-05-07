from enum import Enum


class Action(Enum):
    LEFT = 0
    RIGHT = 1
    UP = 2
    DOWN = 3

    def __gt__(self, other):
        return self.value > other.value

names_dict = {
    Action.LEFT: 'L',
    Action.RIGHT: 'R',
    Action.UP: 'U',
    Action.DOWN: 'D'
}


def get_short_name(action: Action):
    return names_dict.get(action)
