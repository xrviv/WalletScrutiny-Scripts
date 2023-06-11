import os

def find_duplicate_entries(file_path):
    entries = set()
    duplicates = set()

    with open(file_path, 'r') as file:
        for line in file:
            entry = line.strip()
            if entry in entries:
                duplicates.add(entry)
            else:
                entries.add(entry)

    return duplicates

def count_duplicates(file_path):
    duplicates = find_duplicate_entries(file_path)
    count = len(duplicates)
    print(f"Duplicate count: {count}")

file_path = input("Enter the file path: ")
if not os.path.isfile(file_path):
    print("Invalid file path.")
    exit()

count_duplicates(file_path)
