from more_itertools import chunked

ITEM_VALUE_LIST = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def part_1() -> int:
    total = 0

    with open("input.txt") as file:
        for line in file:
            items = line.strip()
            half = len(items) // 2
            compartment_1 = set(items[:half])
            compartment_2 = set(items[half:])
            common_item = (compartment_1 & compartment_2).pop()
            total += ITEM_VALUE_LIST.index(common_item) + 1
    
    return total

def part_2() -> int:
    total = 0

    with open("input.txt") as file:
        for lines in chunked(file, 3):
            group = [set(line.strip()) for line in lines]
            common_item = (group[0] & group[1] & group[2]).pop()
            total += ITEM_VALUE_LIST.index(common_item) + 1
    
    return total


if __name__ == "__main__":
    print(part_1())
    print(part_2())