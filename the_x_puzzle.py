from typing import List

from algo_enum import AlgoEnum
from state import State


def convert_order_to_nums(order_string: str) -> List[int]:
    order_list = order_string.split('-')
    return list(map(lambda x: int(x), order_list))


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

    algo_num = lines[0]
    N = lines[1]
    order_string = lines[2]

order_int_list = convert_order_to_nums(order_string)

root_state = State(order_int_list)

if algo_num == AlgoEnum.IDS.value:
    pass
elif algo_num == AlgoEnum.BFS.value:
    pass
elif algo_num == AlgoEnum.A_STAR.value:
    pass
