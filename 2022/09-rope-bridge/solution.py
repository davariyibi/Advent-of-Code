from typing import List, Optional, Tuple

DIRECTIONS = {"L": (-1, 0), "R": (1, 0), "U": (0, 1), "D": (0, -1)}

def get_input() -> List[List[int]]:
    moves = []

    with open("input.txt") as file:
        for line in file:
            parts = line.strip().split(" ")
            moves.append((parts[0], int(parts[1])))
    
    return moves

def part_1(moves: List[Tuple[str, int]]) -> int:
    head = (0, 0)
    tail = (0, 0)
    tail_locations = {tail}

    for direction, amount in moves:
        delta_x, delta_y = DIRECTIONS[direction]

        for _ in range(amount):
            head = (head[0] + delta_x, head[1] + delta_y)
            horizontal_distance = head[0] - tail[0] if head[0] > tail[0] else tail[0] - head[0]
            vertical_distance = head[1] - tail[1] if head[1] > tail[1] else tail[1] - head[1]

             # IF 2-far away in any one direction, move tail in that direction
             # IF L-shaped away, move tail to head's previous position
             # ELSE do nothing
            if horizontal_distance > 1:
                if vertical_distance:
                    tail = (head[0] - delta_x, head[1] - delta_y)
                else:
                    tail = (tail[0] + delta_x, tail[1] + delta_y)
            elif vertical_distance > 1:
                if horizontal_distance:
                    tail = (head[0] - delta_x, head[1] - delta_y)
                else:
                    tail = (tail[0] + delta_x, tail[1] + delta_y)
            
            tail_locations.add(tail)

    return len(tail_locations)

def part_2(moves: List[Tuple[str, int]]) -> int:
    knots_idxs = list(range(10))
    knots = [(0, 0) for _ in knots_idxs]
    tail_locations = {knots[-1]}

    def print_board():
        board = [[".", ".", ".", ".", ".", "."] for _ in range(5)]
        board[0][0] = "s"
        for idx, (x, y) in list(enumerate(knots))[::-1]:
            board[y][x] = str(idx)
        
        for row in board[::-1]:
            print("".join(row))
        print()


    for direction, amount in moves:
        print(f"--- {direction} {amount} ---")
        delta_x, delta_y = DIRECTIONS[direction]

        for _ in range(amount):
            head_x, head_y = knots[0]
            knots[0] = (head_x + delta_x, head_y + delta_y)

            for knot_a_idx, knot_b_idx in zip(knots_idxs, knots_idxs[1:]):
                knot_a = knots[knot_a_idx]
                knot_b = knots[knot_b_idx]
                horizontal_distance = knot_a[0] - knot_b[0]
                vertical_distance = knot_a[1] - knot_b[1]

                if horizontal_distance > 1 or horizontal_distance < -1:
                    horizontal_movement = horizontal_distance // 2
                    vertical_position = knot_a[1] if vertical_distance else knot_b[1]
                    knot_b = (knot_b[0] + horizontal_movement, vertical_position)
                elif vertical_distance > 1 or vertical_distance < -1:
                    horizontal_position = knot_a[0] if horizontal_distance else knot_b[0]
                    vertical_movement = vertical_distance // 2
                    knot_b = (horizontal_position, knot_b[1] + vertical_movement)
                
# ......
# ......
# ....H.
# ....1.
# 432...
                
                knots[knot_b_idx] = knot_b
                
            tail_locations.add(knots[-1])
            print_board()

    return len(tail_locations)


if __name__ == "__main__":
    trees = get_input()
    print(part_1(trees))
    print(part_2(trees))