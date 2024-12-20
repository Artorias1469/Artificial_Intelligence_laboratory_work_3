#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Рассмотрим реализацию алгоритма поиска в глубину на практике, в программном коде.


class Node:
    def __init__(self, state):
        self.state = state


def is_cycle(node):
    # Логика проверки циклов
    pass


def expand(problem, node):
    # Логика расширения узлов
    pass


failure = None  # Определите значение failure, если это нужно


def depth_first_recursive_search(problem, node=None):
    if node is None:
        node = Node(problem.initial)

    if problem.is_goal(node.state):
        return node
    elif is_cycle(node):
        return failure
    else:
        for child in expand(problem, node):
            result = depth_first_recursive_search(problem, child)
            if result:
                return result

    return failure