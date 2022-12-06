def part_1() -> int:
    encompassing_pairs = 0

    with open("input.txt") as file:
        for line in file:
            pairs = [
                [int(val) for val in pair.split("-")]
                for pair in line.strip().split(",")
            ]

            if (
                (pairs[0][0] <= pairs[1][0] and pairs[1][1] <= pairs[0][1])
                or (pairs[1][0] <= pairs[0][0] and pairs[0][1] <= pairs[1][1])
            ):
                encompassing_pairs += 1
    
    return encompassing_pairs

def part_2() -> int:
    overlapping_pairs = 0

    with open("input.txt") as file:
        for line in file:
            pairs = [
                [int(val) for val in pair.split("-")]
                for pair in line.strip().split(",")
            ]

            # if it's not the case that they don't overlap, then they overlap :)
            if not (pairs[0][1] < pairs[1][0] or pairs[1][1] < pairs[0][0]):
                overlapping_pairs += 1
    
    return overlapping_pairs


if __name__ == "__main__":
    print(part_1())
    print(part_2())