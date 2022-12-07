def part_1() -> int:
    stacks = [[], [], [], [], [], [], [], [], []]

    with open("input.txt") as file:
        for line_idx, line in enumerate(file):
            # create stacks
            if line_idx < 8: 
                for idx in range(9):
                    crate = line[idx * 4 + 1]
                    if crate != " ":
                        stacks[idx].insert(0, crate)

            # intermediate lines
            elif line_idx < 10:
                continue

            # move crates
            else:
                cleaned_line = line.strip().split()
                amount = int(cleaned_line[1])
                from_ = int(cleaned_line[3]) - 1
                to_ = int(cleaned_line[5]) - 1

                for _ in range(amount):
                    stacks[to_].append(stacks[from_].pop())
    
    return "".join([stack[-1] for stack in stacks])

def part_2() -> int:
    stacks = [[], [], [], [], [], [], [], [], []]

    with open("input.txt") as file:
        for line_idx, line in enumerate(file):
            # create stacks
            if line_idx < 8: 
                for idx in range(9):
                    crate = line[idx * 4 + 1]
                    if crate != " ":
                        stacks[idx].insert(0, crate)

            # intermediate lines
            elif line_idx < 10:
                continue

            # move crates
            else:
                cleaned_line = line.strip().split()
                amount_range = range(int(cleaned_line[1]))
                from_ = int(cleaned_line[3]) - 1
                to_ = int(cleaned_line[5]) - 1
                in_crane = []

                for _ in amount_range:
                    in_crane.append(stacks[from_].pop())
                
                for _ in amount_range:
                    stacks[to_].append(in_crane.pop())
    
    return "".join([stack[-1] for stack in stacks])


if __name__ == "__main__":
    print(part_1())
    print(part_2())