from typing import List

from algo_enum import AlgoEnum
from bfs import BFS
from puzzle_graph import PuzzleGraph
from state import State


def convert_order_to_nums(order_string: str) -> List[int]:
    order_list = order_string.split('-')
    return list(map(lambda x: int(x), order_list))


with open("input.txt", "r") as input_file:
    lines = input_file.readlines()

    algo_num = int(lines[0].strip())
    N = int(lines[1].strip())
    order_string = lines[2]

order_int_list = convert_order_to_nums(order_string)

# root_state = State(order_int_list, N)

# graph = PuzzleGraph(order_int_list, N)

if algo_num == AlgoEnum.IDS.value:
    pass
elif algo_num == AlgoEnum.BFS.value:
    bfs_graph = BFS(order_int_list, N)
    print("a")
elif algo_num == AlgoEnum.A_STAR.value:
    pass
