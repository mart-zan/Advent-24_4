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
    diagonal_str = str()
    diagonal_str_bw = str()
    N = len(input_rows)
    L_row = len(input_rows[0])
    # print(input_rows)
    # print(input_rows[0])
    # print('rozmery: N, L ... ', N, L_row )
    rows = input_rows
    for i, row in N:
       if i is 140:
            break
        j = i
        k = N-i-1
        for l in range(0, L_row-1):
            print(j)
            print(i + l)
            print('--')
            diagonal_str += str(rows[j][i+l])

            # print(k)
            # print(L_row-i-l-1)
            diagonal_str_bw += str(rows[k][L_row-i-l-1])

            k = k - 1
            j = j + 1
            # print(diagonal_str)
            # print(i)
            # print(j)
        # diagonal_str = rows[1][] + rows[2][2] + ... + row[i][N]
        # diagonal_str = rows[0][0] + rows[1][1] + ... + row[i+N][N]
    diagonal = how_many_patterns(diagonal_str, pattern_xmas)
    diagonal_bw = how_many_patterns(diagonal_str_bw, pattern_xmas)
    print(horizontal)
    print(horizontal_bw)
    print(diagonal)
    print(diagonal_bw)
    all_xmas = horizontal+horizontal_bw+diagonal+diagonal_bw
    print('vysledek ... ',str(all_xmas))
