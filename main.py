import re


# Advent of Code
# --- Day 4: Ceres Search ---


def read_instructions(filename: str):

    my_file = open(filename, 'r')
    data = my_file.read()
    my_file.close()
    # Returns
    return data

def how_many_patterns(pattern, input_text):

    find_pattern =  re.findall(pattern, input_text)
    number_pattern = len(find_pattern)
    return  number_pattern

def is_valid_mas(grid, start_row, start_col, dx, dy):

    pattern = "MAS"
    rows, cols = len(grid), len(grid[0])
    for k in range(len(pattern)):  # Check for 3 characters
        ni, nj = start_row + k * dx, start_col + k * dy
        if not (0 <= ni < rows and 0 <= nj < cols) or grid[ni][nj] != pattern[k]:
            return False
    return True

if __name__ == '__main__':

    # Read and close file
    input_xmas = read_instructions('/home/zanetka/PycharmProjects/Advent_24_4/input.txt')
    pattern = 'XMAS'
    pattern_length = 4
    input_rows = input_xmas.strip().split('\n')  # Split text into each row
    # Initialization
    N = len(input_rows)
    L_row = len(input_rows[0])
    count = 0
    # Directions in string matrix
    directions = \
        [ (0, 1),  # Horizontal right
        (0, -1),   # Horizontal left
        (1, 0),    # Vertical down
        (-1, 0),   # Vertical up
        (1, 1),    # Diagonal down-right
        (-1, -1),  # Diagonal up-left
        (1, -1),   # Diagonal down-left
        (-1, 1) ]  # Diagonal up-right

    # Check every cell in the grid
    for i in range(N):
        for j in range(L_row):
            # For each direction, check if the word can be formed starting from grid[i][j]
            for dx, dy in directions:
                # Check if we can find the word in this direction
                found = True
                for k in range(pattern_length):
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
    print('Overall XMAS is ', count, '.')

    # TASK 2
    # grid = input_xmas.strip().split('\n')  # Split into rows
    count = 0
    rows, cols = len(input_rows), len(input_rows)

    # Check every cell for an X-MAS pattern
    for i in range(rows):
        for j in range(cols):
            # Check for two MAS
            if is_valid_mas(input_rows , i, j, 1, 1) and is_valid_mas(input_rows , i, j, -1, 1):
                count += 1

    print('Overall X-MAS count is', count, '.')
