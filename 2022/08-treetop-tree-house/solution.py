from typing import List, Tuple

def get_input() -> List[List[int]]:
    trees = []

    with open("input.txt") as file:
        for line in file:
            heights = [int(tree) for tree in line.strip()]
            trees.append(heights)
    
    return trees

def part_1(trees: List[List[int]]) -> int:
    last_row_idx = len(trees) - 1
    last_col_idx = len(trees[0]) -1
    visible_trees = 0

    for row_idx, row in enumerate(trees):
        for col_idx, height in enumerate(row):
            if row_idx == 0 or col_idx == 0 or row_idx == last_row_idx or col_idx == last_col_idx:
                visible_trees += 1
            # up
            elif height > max(_row[col_idx] for _row in trees[:row_idx]):
                visible_trees += 1
            # down
            elif height > max(_row[col_idx] for _row in trees[row_idx + 1:]):
                visible_trees += 1
            # left
            elif height > max(row[:col_idx]):
                visible_trees += 1
            # right
            elif height > max(row[col_idx + 1:]):
                visible_trees += 1

    return visible_trees

def part_2(trees: List[List[int]]) -> int:
    rows = len(trees)
    cols = len(trees[0])

    def viewing_distance(start_row: int, start_col: int, direction: Tuple[int, int]) -> int:
        tree_height = trees[start_row][start_col]
        delta_row, delta_col = direction
        curr_row = start_row + delta_row
        curr_col = start_col + delta_col
        distance = 0
        
        while True:
            if 0 <= curr_row < rows and 0 <= curr_col < cols:
                distance += 1

                if trees[curr_row][curr_col] >= tree_height:
                    break
            else:
                break

            curr_row += delta_row
            curr_col += delta_col
        
        return distance

    max_scenic_score = 0
    range_cols = range(cols)

    for row_idx in range(rows):
        for col_idx in range_cols:
            up_distance = viewing_distance(row_idx, col_idx, (-1, 0))
            down_distance = viewing_distance(row_idx, col_idx, (1, 0))
            left_distance = viewing_distance(row_idx, col_idx, (0, -1))
            right_distance = viewing_distance(row_idx, col_idx, (0, 1))
            scenic_score = up_distance * down_distance * left_distance * right_distance
            max_scenic_score = max(max_scenic_score, scenic_score)

    return max_scenic_score


if __name__ == "__main__":
    trees = get_input()
    print(part_1(trees))
    print(part_2(trees))