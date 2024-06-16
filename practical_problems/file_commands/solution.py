
def get_file_or_dir_name(string: str) -> str:
    if string.startswith("cd"):
        return string[3:].strip()  
    
    elif string.startswith("touch"):
        return string[6:].strip()  
    
    return ""
    
    
def process_commands(commands: list) -> str:
    directory_map = {}  
    current_directory = None
    max_value= 0 
    
    for command in commands:
        file_or_dir = get_file_or_dir_name(command)
        
        if command.startswith("cd"):
            current_directory = file_or_dir
            if current_directory not in directory_map:
                directory_map[current_directory] = []
                
        elif command.startswith("touch"):
            if current_directory is not None:
                if file_or_dir not in directory_map[current_directory]:
                    directory_map[current_directory].append(file_or_dir)
                    
    max_files = 0
    dir_with_most_files = ""

    for directory, files in directory_map.items():
        if(len(files) > max_files):
            max_files = len(files)
            dir_with_most_files = directory
        
    return dir_with_most_files

# Test Case 1: Basic usage
commands1 = [
    "cd dir1",
    "touch fileA",
    "cd dir2",
    "touch fileB",
    "touch fileB",
    "cd dir1",
    "touch fileC",
]
print(process_commands(commands1) == 'dir1')  # Output: True

# Test Case 2: All files in the same directory
commands2 = [
    "cd dir1",
    "touch fileA",
    "touch fileB",
    "touch fileC",
]
print(process_commands(commands2) == 'dir1')  # Output: True

# Test Case 3: Multiple directories with equal number of files
commands3 = [
    "cd dir1",
    "touch fileA",
    "cd dir2",
    "touch fileB",
    "cd dir3",
    "touch fileC",
]
print(process_commands(commands3) in {'dir1', 'dir2', 'dir3'})  # Output: True

# Test Case 4: Empty command list
commands4 = []
print(process_commands(commands4) in [None, ""])  # Output: True

# Test Case 5: Multiple directories with different number of files
commands5 = [
    "cd dir1",
    "touch fileA",
    "touch fileB",
    "cd dir2",
    "touch fileC",
    "cd dir3",
    "touch fileD",
    "touch fileE",
    "touch fileF",
]
print(process_commands(commands5) == 'dir3')  # Output: True