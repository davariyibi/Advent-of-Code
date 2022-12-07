def solution(distinct_letters_needed: int) -> int:
    with open("input.txt") as file:
        line = next(file).strip()
        for char_idx, _ in enumerate(line):
            if char_idx < distinct_letters_needed - 1:
                continue
            
            char_set = set(line[char_idx + 1 - distinct_letters_needed:char_idx + 1])
            
            if len(char_set) == distinct_letters_needed:
                return char_idx + 1
    
    return -1


if __name__ == "__main__":
    print(solution(4)) # part 1
    print(solution(14)) # part 2