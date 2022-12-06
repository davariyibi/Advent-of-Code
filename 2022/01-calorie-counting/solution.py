def part_1() -> int:
    max_elf_amount = 0
    current_elf_amount = 0
    with open("input.txt") as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                calorie = int(cleaned_line)
                current_elf_amount += calorie
            else:
                max_elf_amount = max(max_elf_amount, current_elf_amount)
                current_elf_amount = 0
        
        max_elf_amount = max(max_elf_amount, current_elf_amount)
        return max_elf_amount

def part_2() -> int:
    max_elves_amounts = [0, 0, 0]
    current_elf_amount = 0

    def get_new_maxes():
        min_amount = min(max_elves_amounts)
        if current_elf_amount > min_amount:
            min_amount_index = max_elves_amounts.index(min_amount)
            max_elves_amounts[min_amount_index] = current_elf_amount

    with open("input.txt") as file:
        for line in file:
            cleaned_line = line.strip()
            if cleaned_line:
                calorie = int(cleaned_line)
                current_elf_amount += calorie
            else:
                get_new_maxes()
                current_elf_amount = 0
        
        get_new_maxes()
        return sum(max_elves_amounts)

if __name__ == "__main__":
    print(part_1())
    print(part_2())