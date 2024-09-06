import os

def LineCount(S):
    if not os.path.isfile(S):
        return -1
    with open(S, 'r') as file:
        return len(file.readlines())

print("директория: ", os.getcwd())

file_names = ['file1.txt', 'texts.txt', 'file3.txt']
lines = {file: LineCount(file) for file in file_names}

for file, count in lines.items():
    if count == -1:
        print(f"Файл '{file}' не обнаружен.")
    else:
        print(f"Файл '{file}' содержит {count} строк.")
