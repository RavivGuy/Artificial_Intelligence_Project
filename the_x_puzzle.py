import datetime
from typing import List, Tuple

import action_enum
from a_star import AStar
from algo_enum import AlgoEnum
from base_global_search import BaseGlobalSearch
from bfs import BFS
from ids import IDS

"""
convert the string of the puzzle order to list of ints
"""
def convert_order_to_nums(order_string: str) -> List[int]:
    order_list = order_string.split('-')
    return list(map(lambda x: int(x), order_list))

"""
file_name: the file of the puzzle data
return: the puzzle data
"""
def get_input_from_file(file_name: str) -> Tuple[AlgoEnum, int, List[int]]:
    with open(file_name, "r") as input_file:
        lines = input_file.readlines()

        algo_enum = AlgoEnum(int(lines[0].strip()))
        N = int(lines[1].strip())
        order_string = lines[2]
    order_list = convert_order_to_nums(order_string)
    return algo_enum, N, order_list

"""
algo_enum - the enum that represent which algorithm to use
return- the graph of the solution path
"""
def get_solve_graph(algo_enum: AlgoEnum):
    solve_graph: BaseGlobalSearch = None
    if algo_enum == AlgoEnum.IDS:
        solve_graph = IDS(order_int_list, N)
    elif algo_enum == AlgoEnum.BFS:
        solve_graph = BFS(order_int_list, N)
    elif algo_enum == AlgoEnum.A_STAR:
        solve_graph = AStar(order_int_list, N)
    return solve_graph

"""
write the solution path to file
"""
def write_output(moves, file_name: str):
    with open(file_name, "w") as output_file:
        moves = str.join('', [action_enum.get_short_name(move) for move in moves])
        output_file.write(moves)

"""
the main method
"""
if __name__ == "__main__":
    algo, N, order_int_list = get_input_from_file("med_input.txt")
    solution_graph = get_solve_graph(algo)
    end_time = datetime.datetime.now()
    solve_moves = solution_graph.get_solve_moves()
    write_output(solve_moves, "output.txt")
