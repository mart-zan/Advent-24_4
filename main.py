import re


# Advent of Code
# --- Day 4: Ceres Search ---


def read_instructions(filename: str):

    my_file = open(filename, "r")
    data = my_file.read()
    my_file.close()
    # Returns
    return data


def read_horizontal(string_matrix
                     ,pattern):
    pattern_mul = r"mul\((\d+),(\d+)\)"
    numbers_list = re.findall(pattern_mul, instructions)
    return numbers_list


if __name__ == '__main__':
    # Read and close file
    input_xmas = read_instructions("input.txt")

    pattern = 'XMAS'

    horizontal_xmas =  read_horizontal(input_xmas, pattern)
    print(horizontal_xmas)