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
    read_rows = input_xmas.strip().split('\n')  # Split text into each row
    print(read_rows)
    # for i in 1
    # diagonal =
    diagonal_str = []
    for i, row in enumerate(read_rows):
        
    print(horizontal)
    print(horizontal_bw)
