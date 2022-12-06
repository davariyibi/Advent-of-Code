def part_1() -> int:
    rps = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}

    def outcome(_opponent, _me) -> int:
        if _me == _opponent:
            return 3

        if _me - (_opponent % 3) == 1: # if I have 1 number higher than opponent
            return 6
        
        return 0
        
    total_score = 0
    with open("input.txt") as file:
        for line in file:
            round = line.strip()
            opponent = rps[round[0]]
            me = rps[round[2]]
            total_score += me + outcome(opponent, me)
    
    return total_score


def part_2() -> int:
    rps = {"A": 1, "B": 2, "C": 3, "X": 0, "Y": 3, "Z": 6}

    def which_hand(_opponent, _outcome) -> int:
        if _outcome == 3:
            return _opponent
        
        if _outcome == 6:
            return _opponent + 1 if _opponent != 3 else 1
        
        return _opponent - 1 if _opponent != 1 else 3
        
    total_score = 0
    with open("input.txt") as file:
        for line in file:
            round = line.strip()
            opponent = rps[round[0]]
            outcome = rps[round[2]]
            total_score += which_hand(opponent, outcome) + outcome
    
    return total_score



if __name__ == "__main__":
    print(part_1())
    print(part_2())