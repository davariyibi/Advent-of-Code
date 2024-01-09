LOOKUP = {
    "o": {"n": {"e": "1"}},
    "t": {
        "w": {"o": "2"},
        "h": {"r": {"e": {"e": "3"}}},
    },
    "f": {
        "o": {"u": {"r": "4"}},
        "i": {"v": {"e": "5"}},
    },
    "s": {
        "i": {"x": "6"},
        "e": {"v": {"e": {"n": "7"}}},
    },
    "e": {"i": {"g": {"h": {"t": "8"}}}},
    "n": {"i": {"n": {"e": "9"}}},
}

def part_1() -> int:
    calibration_number_sum = 0
    with open("input.txt") as file:
        for line in file:
            cleaned_line = line.strip()
            first_num_char = None
            last_num_char = None
            for char in cleaned_line:
                if char.isdigit():
                    if first_num_char is None:
                        first_num_char = char
                    last_num_char = char

            calibration_number_sum += int(f"{first_num_char}{last_num_char}")

    return calibration_number_sum


def part_2() -> int:
    calibration_number_sum = 0
    with open("input.txt") as file:
        for line in file:
            cleaned_line = line.strip()
            first_num_char = None
            last_num_char = None
            for idx, char in enumerate(cleaned_line):
                if char.isdigit():
                    if first_num_char is None:
                        first_num_char = char
                    last_num_char = char
                    continue
                
                curr_idx = idx
                curr_char = char
                curr_lookup = LOOKUP
                while curr_char in curr_lookup:
                    new_lookup = curr_lookup[curr_char]
                    
                    if isinstance(new_lookup, str):
                        if first_num_char is None:
                            first_num_char = new_lookup
                        last_num_char = new_lookup
                        break

                    if curr_idx + 1 >= len(cleaned_line):
                        break

                    curr_idx += 1
                    curr_char = cleaned_line[curr_idx]
                    curr_lookup = new_lookup
       
            calibration_number_sum += int(f"{first_num_char}{last_num_char}")

    return calibration_number_sum

if __name__ == "__main__":
    print(part_1())
    print(part_2())