from enum import Enum


class Action(Enum):
    """
    enum of available moves
    """
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

    def __gt__(self, other):
        return self.value > other.value


# dict between move action to sort action string
names_dict = {
    Action.LEFT: 'L',
    Action.RIGHT: 'R',
    Action.UP: 'U',
    Action.DOWN: 'D'
}


def get_short_name(action: Action):
    return names_dict.get(action)
