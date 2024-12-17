import re


# Advent of Code
# --- Day 4: Ceres Search ---


def read_instructions(filename: str):

    my_file = open(filename, 'r')
    data = my_file.read()
    my_file.close()
    # Returns
    return data

# def read_rows(filename: str):
#
#     my_file = open(filename, "r")
#     data = my_file.read()
#     rows = data.strip().split('\n')  # Split text into each row
#     # Returns
#     return rows

def how_many_patterns(pattern, input_text):

    find_pattern =  re.findall(pattern, input_text)
    number_pattern = len(find_pattern)
    return  number_pattern

# def read_horizontal(string_matrix
#                      ,pattern):
#     pattern_mul = r"mul\((\d+),(\d+)\)"
#     numbers_list = re.findall(pattern_mul, instructions)
#     return numbers_list


if __name__ == '__main__':
    # Read and close file
    input_xmas = read_instructions('/home/zanetka/PycharmProjects/Advent_24_4/input.txt')
    pattern_xmas = 'XMAS'

    # Horizontal
    horizontal = how_many_patterns(pattern_xmas, input_xmas)
    # Hoizontal bacwards
    horizontal_bw = how_many_patterns(pattern_xmas, input_xmas[::-1])
    # Diagonal
    input_rows = input_xmas.strip().split('\n')  # Split text into each row
    print(input_rows)
    # for i in 1
    # diagonal =
    # diagonal_str = str()
    # diagonal_str_bw = str()
    # Initialization
    N = len(input_rows)
    L_row = len(input_rows[0])
    count = 0
    # Directions in string matrix
    directions = [ (0, 1),   # Horizontal right
        (0, -1),  # Horizontal left
        (1, 0),   # Vertical down
        (-1, 0),  # Vertical up
        (1, 1),   # Diagonal down-right
        (-1, -1), # Diagonal up-left
        (1, -1),  # Diagonal down-left
        (-1, 1) ]  # Diagonal up-right

    word_length = 4
    pattern= 'XMAS'
    # Check every cell in the grid
    for i in range(N):
        for j in range(L_row):
            # For each direction, check if the word can be formed starting from grid[i][j]
            for dx, dy in directions:
                # Check if we can find the word in this direction
                found = True
                for k in range(word_length):
                    ni, nj = i + k * dx, j + k * dy
                    # Check if the indices are out of bounds
                    if not (0 <= ni < N and 0 <= nj < L_row):
                        found = False
                        break
                    # Check if the character matches the corresponding character in "XMAS"
                    if input_rows[ni][nj] != pattern[k]:
                        found = False
                        break
                # If the word is found in this direction, increment count
                if found:
                    count += 1
    print(count)
    # print(input_rows)
    # print(input_rows[0])
    # print('rozmery: N, L ... ', N, L_row )
    # rows = input_rows
    # Traversing down-right diagonals (from top row and leftmost column)
    # for start in range(N):  # Start from each element in the first column
    #     i, j = start, 0
    #     while i < N and j < L_row:
    #         diagonal_str += input_rows[i][j]
    #         i += 1
    #         j += 1
    #
    # for start in range(1, L_row):  # Start from each element in the first row, excluding the top-left corner
    #     i, j = 0, start
    #     while i < N and j < L_row:
    #         diagonal_str += input_rows[i][j]
    #         i += 1
    #         j += 1
    #
    # # Traversing down-left diagonals (from top row and rightmost column)
    # for start in range(N):  # Start from each element in the last column
    #     i, j = start, L_row - 1
    #     while i < N and j >= 0:
    #         diagonal_str_bw += input_rows[i][j]
    #         i += 1
    #         j -= 1
    #
    # for start in range(L_row - 2, -1, -1):  # Start from each element in the first row, excluding the top-right corner
    #     i, j = 0, start
    #     while i < N and j >= 0:
    #         diagonal_str_bw += input_rows[i][j]
    #         i += 1
    #         j -= 1
    # # for i in range(0, N-1):
    # #     # if i is 140:
    # #     #     break
    # #     j = i
    # #     k = N-i-1
    # #
    # #     # under the diagonal line
    # #     for l in range(0, L_row-1-i):
    # #         print(j)
    # #         print(i + l)
    # #         print('--')
    # #         diagonal_str += str(rows[j][i+l])
    # #         print(diagonal_str)
    # #
    # #         # print(k)
    # #         # print(L_row-i-l-1)
    # #         diagonal_str_bw += str(rows[k][L_row-i-l-1])
    # #
    # #         k = k - 1
    # #         j = j + 1
    #     # just to make space between line
    # # diagonal_str += 'Z'        # over the diagonal line
    # # diagonal_str_bw += 'Z'
    #     # over the diagonal line
    #
    # for i in range(0, L_row - 1):
    #     # if i is 140:
    #     #     break
    #     j = i
    #     k = N - i - 1
    #
    #     for l in range(0, N-1-i):
    #         print(j)
    #         print(i + l)
    #         print('--')
    #         diagonal_str += str(rows[i+l][j])
    #         print(diagonal_str)
    #
    #         # print(k)
    #         # print(L_row-i-l-1)
    #         diagonal_str_bw += str(rows[L_row-i-l-1][k])
    #
    #         k = k - 1
    #         j = j + 1
    #
    #         # print(diagonal_str)
    #         # print(i)
    #         # print(j)
    #     # diagonal_str = rows[1][] + rows[2][2] + ... + row[i][N]
    #     # diagonal_str = rows[0][0] + rows[1][1] + ... + row[i+N][N]
    # diagonal = how_many_patterns(diagonal_str, pattern_xmas)
    # diagonal_bw = how_many_patterns(diagonal_str_bw, pattern_xmas)
    # print(horizontal)
    # print(horizontal_bw)
    # print(diagonal)
    # print(diagonal_bw)
    # all_xmas = horizontal+horizontal_bw+diagonal+diagonal_bw
    # print('vysledek ... ',str(all_xmas))
