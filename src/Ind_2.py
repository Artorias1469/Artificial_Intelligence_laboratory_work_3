#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def find_words(board, dictionary):
    found_words = set()
    rows, cols = len(board), len(board[0])

    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),        (0, 1),
                  (1, -1), (1, 0), (1, 1)]

    def dfs(x, y, path, visited):
        path += board[x][y]
        if path in dictionary:
            found_words.add(path)

        if len(path) > max_length:
            return

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if (0 <= new_x < rows and
                0 <= new_y < cols and
                (new_x, new_y) not in visited):
                visited.add((new_x, new_y))
                dfs(new_x, new_y, path, visited)
                visited.remove((new_x, new_y))

    max_length = max(len(word) for word in dictionary)

    for i in range(rows):
        for j in range(cols):
            visited = set()
            visited.add((i, j))  # Начинаем с текущей ячейки
            dfs(i, j, '', visited)  # Запускаем поиск

    return found_words

if __name__ == '__main__':
    board = [
        ['К', 'О', 'Т'],
        ['А', 'Р', 'Ь'],
        ['С', 'Л', 'О']
    ]

    dictionary = ['КОТ','КОЛ','ОРК','СОК','ТОРС','ТОКАРЬ','СЛОТ','СОЛЬ','ЛОСЬ','ЛОТ','КОРОЛЬ','СОРТ']

    result = find_words(board, dictionary)
    print("Найденные слова:", result)