#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Необходимо для построенного графа лабораторной работы 1
# написать программу на языке программирования Python, которая с помощью
# алгоритма поиска в глубину находит минимальное расстояние между
# начальным и конечным пунктами.

class Node:
    def __init__(self, state, parent=None, path_cost=0):
        self.state = state
        self.parent = parent
        self.path_cost = path_cost

    def path(self):

        node, path_back = self, []
        while node:
            path_back.append(node.state)
            node = node.parent
        return path_back[::-1]


class Problem:
    def __init__(self, initial, goal):
        self.initial = initial
        self.goal = goal

    def is_goal(self, state):
        return state == self.goal


failure = None


def is_cycle(node):
    """
    Проверка, есть ли цикл в текущем пути.
    """
    current = node
    visited = set()
    while current:
        if current.state in visited:
            return True
        visited.add(current.state)
        current = current.parent
    return False


def expand(graph, node):
    """
    Расширение узлов: генерация дочерних узлов.
    """
    for neighbor, weight in graph.get(node.state, []):
        yield Node(neighbor, node, node.path_cost + weight)


def depth_first_recursive_search(problem, graph, node=None, min_distance=float('inf'), min_path=None):
    """
    Рекурсивный поиск в глубину с нахождением минимального пути.
    """
    if node is None:
        node = Node(problem.initial)

    if problem.is_goal(node.state):
        if node.path_cost < min_distance:
            min_distance = node.path_cost
            min_path = node.path()
        return min_path, min_distance

    if is_cycle(node):
        return None, min_distance

    for child in expand(graph, node):
        result_path, result_distance = depth_first_recursive_search(problem, graph, child, min_distance, min_path)
        if result_path and result_distance < min_distance:
            min_distance = result_distance
            min_path = result_path

    return min_path, min_distance


if __name__ == "__main__":
    graph = {
        1: [(2, 219), (3, 488), (4, 314), (5, 462)],
        2: [(1, 219), (6, 287), (7, 365)],
        3: [(1, 488), (4, 334), (8, 226), (9, 217)],
        4: [(1, 314), (3, 334), (5, 192)],
        5: [(1, 462), (4, 192), (8, 424)],
        6: [(2, 287), (10, 354)],
        7: [(2, 365), (11, 214), (12, 354), (9, 219)],
        8: [(3, 226), (5, 424), (14, 291)],
        9: [(3, 217), (7, 219), (15, 211), (16, 222), (20, 460), (14, 360)],
        10: [(6, 354), (11, 124)],
        11: [(7, 214), (10, 124), (12, 146)],
        12: [(7, 354), (11, 146), (13, 153)],
        13: [(12, 153), (19, 188), (20, 192)],
        14: [(8, 291), (9, 360), (15, 164), (16, 148), (17, 68)],
        15: [(9, 211), (14, 164)],
        16: [(9, 222), (14, 148), (17, 110)],
        17: [(14, 68), (16, 110), (18, 381)],
        18: [(17, 381), (20, 148)],
        19: [(13, 188), (20, 112)],
        20: [(9, 460), (13, 192), (18, 148), (19, 112)],
        21: [(16, 344)],
    }

    start = 2
    goal = 17
    problem = Problem(start, goal)

    path, distance = depth_first_recursive_search(problem, graph)
    print("Кратчайший путь:", path)
    print("Длина пути:", distance)