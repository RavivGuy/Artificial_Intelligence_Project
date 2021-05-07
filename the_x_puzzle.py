import datetime
from typing import List

import action_enum
from a_star import AStar
from algo_enum import AlgoEnum
from base_global_search import BaseGlobalSearch
from bfs import BFS
from ids import IDS


def convert_order_to_nums(order_string: str) -> List[int]:
    order_list = order_string.split('-')
    return list(map(lambda x: int(x), order_list))


def get_input_from_file():
    with open("med_input.txt", "r") as input_file:
        lines = input_file.readlines()

        algo_enum = AlgoEnum(int(lines[0].strip()))
        N = int(lines[1].strip())
        order_string = lines[2]
    order_list = convert_order_to_nums(order_string)
    return algo_enum, N, order_list


def get_solve_graph(algo_enum: AlgoEnum):
    solve_graph: BaseGlobalSearch = None
    if algo_enum == AlgoEnum.IDS:
        solve_graph = IDS(order_int_list, N)
    elif algo_enum == AlgoEnum.BFS:
        solve_graph = BFS(order_int_list, N)
    elif algo_enum == AlgoEnum.A_STAR:
        solve_graph = AStar(order_int_list, N)
    return solve_graph


def write_output(moves):
    with open("output.txt", "w") as output_file:
        moves = str.join('', [action_enum.get_short_name(move) for move in moves])
        output_file.write(moves)


if __name__ == "__main__":
    algo, N, order_int_list = get_input_from_file()
    start_time = datetime.datetime.now()
    solution_graph = get_solve_graph(algo)
    end_time = datetime.datetime.now()
    print(end_time - start_time)
    solve_moves = solution_graph.get_solve_moves()
    write_output(solve_moves)
