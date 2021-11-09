import random
from collections import Counter

columns = []  # columns is the locations for each of the queens
# columns[r] is a number if a queen is placed at row r and column c.
size = 15


def place_n_queens(size):
    columns.clear()
    row = 0
    while row < size:
        column = random.randrange(0, size - 1)
        columns.append(column)
        row += 1


def display():
    for row in range(len(columns)):
        for column in range(size):
            if column == columns[row]:
                print('♛', end=' ')
            else:
                print(' .', end=' ')
        print()


# place_n_queens(size)
# display()
# print(columns)

"""This of course is not necessary legal, so we'll write a simple DFS search with backtracking:"""


def solve_queen(size):
    columns.clear()
    number_of_moves = 0
    number_of_iterations = 0
    row = 0
    column = 0
    while True:
        # place queen in next row
        ''''print(columns)
        print("I have ", row, " number of queens put down")
        display()
        print(number_of_moves)'''
        while column < size:
            number_of_iterations += 1
            if next_row_is_safe(column):
                place_in_next_row(column)
                number_of_moves += 1
                row += 1
                column = 0
                break
            else:
                column += 1
        # if I could not find an open column or if board is full
        if column == size or row == size:
            number_of_iterations += 1
            # if board is full, we have a solution
            if row == size:
                print("I did it! Here is my solution")
                display()
                # print(number_of_moves)
                return number_of_iterations, number_of_moves
            # I couldn't find a solution so I now backtrack
            prev_column = remove_in_current_row()
            number_of_moves += 1
            if prev_column == -1:  # I backtracked past column 1
                print("There are no solutions")
                # print(number_of_moves)
                return number_of_iterations, number_of_moves
            # try previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column


""" This code is nice, but it uses three functions:

place_in_next_row

remove_in_current_row

next_row_is_safe

That we now have to define

"""


def british_algorithm(size):
    columns.clear()
    number_of_iterations = 0
    flag = True
    while flag:
        place_n_queens(size)
        # display()
        number_of_iterations += 1
        finished = True
        for row, column in enumerate(columns):
            #  verify colums:
            count_column = 0
            for queen_column in columns:
                if column == queen_column:
                    count_column += 1
                    if count_column > 1:  # He will always find himself
                        # print("Aie, there is already a queen in this column ", column)
                        finished = False

            # check diagonal1
            count_diagonal1 = 0
            for queen_row, queen_column in enumerate(columns):
                if queen_column - queen_row == column - row:
                    count_diagonal1 += 1
                    if count_diagonal1 > 1:
                        # print("Aie, there is already a queen in diagonal1 ", column)
                        finished = False

            # check diagonal2
            count_diagonal2 = 0
            for queen_row, queen_column in enumerate(columns):
                if queen_column - queen_row == column - row:
                    count_diagonal2 += 1
                    if count_diagonal2 > 1:
                        # print("Aie, there is already a queen in this diagonal2 ", column)
                        finished = False

        if finished:
            flag = False
        # print(columns)
    return number_of_iterations


def forward_checking(size):
    number_of_moves = 0  # where do I change this so it counts the number of Queen moves?
    number_of_iterations = 0
    row = 0
    column = 0
    rows, cols = (size, size)
    arr = [[0 for x in range(rows)] for y in range(cols)]
    # iterate over rows of board
    while True:
        while column < size:
            # S'il n y pas que des 'X' dans la prochaine ligne:
            if not next_row_is_only_X(arr, row):
                number_of_iterations += 1
                if next_row_is_safe(column):
                    place_in_next_row(column)
                    add_now = putX(arr, row, column)
                    number_of_moves += 1
                    row += 1
                    column = 0
                    break
                else:
                    column += 1
            else:
                # backtracking
                prev_column = remove_in_current_row()
                arr = removeX(arr, add_now)
                number_of_moves += 1
                if prev_column == -1:  # I backtracked past column 1
                    print("There are no solutions")
                    # print(number_of_moves)
                    return number_of_iterations, number_of_moves
                # try previous row again
                row -= 1
                # start checking at column = (1 + value of column in previous row)
                column = 1 + prev_column
            # Sinon. bactrack
        # if board is full
        if row == size:
            print("I did it! Here is my solution")
            display()
            # print(number_of_moves)
            return number_of_iterations, number_of_moves
        if column == 4:
            columns.clear()
            column = 1
            row = 0
            arr = [[0 for x in range(rows)] for y in range(cols)]


def next_row_is_only_X(arr, row):
    if arr[row] == ['X', 'X', 'X', 'X']:
        return True
    return False


def putX(arr, row, column):
    add_now_to_the_list = [[0 for x in range(size)] for y in range(size)]
    number_of_diagonal1 = column - row
    number_of_diagonal2 = column + row
    for i in range(size):  # X in columns
        if arr[i][column] == 0:
            add_now_to_the_list[i][column] = 'X'
        arr[i][column] = 'X'

    for i in range(size):  # X in first diagonal
        if 0 <= (i + number_of_diagonal1) < size:
            if arr[i][i + number_of_diagonal1] == 0:
                add_now_to_the_list[i][i + number_of_diagonal1] = 'X'
            arr[i][i + number_of_diagonal1] = 'X'

    for i in range(size):  # X in second diagonal
        if 0 <= (number_of_diagonal2 - i) < size:
            if arr[i][number_of_diagonal2 - i] == 0:
                add_now_to_the_list[i][number_of_diagonal2 - i] = 'X'
            arr[i][number_of_diagonal2 - i] = 'X'

    return add_now_to_the_list
    # print(arr)


def removeX(arr, add_now):
    for i in range(size):  # I pass on all the sublist.
        for j in range(size):
            if arr[i][j] == add_now[i][j]:
                arr[i][j] = 0
            else:
                arr[i][j] = 'X'
    return arr


def personal_algorithm(size):
    number_of_iterations = 0
    for i in range(int(size/2)):
        columns.append(1 + i*2)
    if size%2 != 0:
        row = size/2 - 0.5
    else:
        row = size/2
    column = 0
    # iterate over rows of board
    while True:
        # place queen in next row
        while column < size:
            number_of_iterations += 1
            if next_row_is_safe(column):
                place_in_next_row(column)
                row += 1
                column = 0
                break
            else:
                column += 1
        # if I could not find an open column or if board is full
        if column == size or row == size:
            number_of_iterations += 1
            # if board is full, we have a solution
            if row == size:
                print("I did it! Here is my solution")
                display()
                # print(number_of_moves)
                return number_of_iterations
            # I couldn't find a solution so I now backtrack
            prev_column = remove_in_current_row()
            if prev_column == -1:  # I backtracked past column 1
                print("There are no solutions")
                # print(number_of_moves)
                return number_of_iterations
            # try previous row again
            row -= 1
            # start checking at column = (1 + value of column in previous row)
            column = 1 + prev_column

    display()


def place_in_next_row(column):
    columns.append(column)


def remove_in_current_row():
    if len(columns) > 0:
        return columns.pop()
    return -1


def next_row_is_safe(column):
    row = len(columns)
    # check column
    for queen_column in columns:
        if column == queen_column:
            return False

    # check diagonal
    for queen_row, queen_column in enumerate(columns):
        if queen_column - queen_row == column - row:
            return False

    # check other diagonal
    for queen_row, queen_column in enumerate(columns):
        if ((size - queen_column) - queen_row
                == (size - column) - row):
            return False
    return True


"""Things should be ok but we don't have the counters I asked for.  That will be the first things you'll need to add.  Either way, let's print what we have:"""

# size = int(input('Enter n: '))
# sum = 0, iter = 0
# for i in range(0, 100):
#    columns = [] #columns is the locations for each of the queens
# iter, sum=solve_queen(size)
# print("# of iterations:", iter)
# print("# of queens placed + backtracks:", sum)
# print(columns)
# iter = british_algorithm(size)
# print("iteration", iter)
# forward_checking(size)

# rows, cols = (size, size)
# arr = [[0 for x in range(rows)] for y in range(cols)]
# print(next_row_is_only_X(arr, 2))

# iter, sum = personal_algorithm(size)
# print("# of iterations:", iter)
# print("# of queens placed + backtracks:", sum)
iter = personal_algorithm(size)
print("# of iterations:", iter)


"""
explication of the personal algorithm and executions:
I place in the first half of the rows queens with a space of 2 adn I begin in the second column.
When I do this, in all the first half of the board, all the queens don't "touch" the other queens.
We only have the last part left. And we this organisation of the first, we don't have to do a lot of backtrack
because the queens are in place that we could have a solution.

results of the run:
n = 4: 5
n = 8: 17
n = 12: 37
n = 15: 7569
"""


