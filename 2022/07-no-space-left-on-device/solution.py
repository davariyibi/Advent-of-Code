from typing import List, Optional, Tuple


class File():
    def __init__(self, name: str, size: int):
        self.name = name
        self.size = size

class Directory():
    def __init__(self, name: str, parent: Optional["Directory"]):
        self.name = name
        self.files = []
        self.directories = []
        self.parent = parent
        self.size = 0
    
    def update_size(self) -> int:
        size = sum(file.size for file in self.files)
        size += sum(directory.update_size() for directory in self.directories)
        self.size = size
        return size

def get_file_system_sizes() -> Tuple[int, int]:
    root = Directory("/", None)
    directories = [root]
    current_directory = None
    
    with open("input.txt") as file:
        for line in file:
            command = line.strip().split(" ")
            if command[0] == "$": # a command
                if len(command) == 2: # ls command
                    continue
                
                # cd command
                if command[2] == "/":
                    current_directory = root
                elif command[2] == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = next(
                        directory
                        for directory in current_directory.directories
                        if directory.name == command[2]
                    )
            elif command[0] == "dir":
                new_directory = Directory(command[1], current_directory)
                current_directory.directories.append(new_directory)
                directories.append(new_directory)
            else:
                new_file = File(command[1], int(command[0]))
                current_directory.files.append(new_file)
    
    root.update_size()
    return root.size, [directory.size for directory in directories]

def part_1(sizes: List[int]) -> int:
    return sum(size for size in sizes if size <= 100000)

def part_2(root_size: int, sizes: List[int]) -> int:
    unused_space = 70000000 - root_size
    space_needed = 30000000 - unused_space
    min_eligible_size = root_size
    
    for size in sizes:
        if size >= space_needed:
            min_eligible_size = min(min_eligible_size, size)

    return min_eligible_size


if __name__ == "__main__":
    root_size, all_sizes = get_file_system_sizes()
    print(part_1(all_sizes))
    print(part_2(root_size, all_sizes))