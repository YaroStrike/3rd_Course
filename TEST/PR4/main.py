def reflect_matrix(matrix):
    return matrix[::-1]

if __name__ == "__main__":
    
    rows = int(input("Введите количество строк матрицы: "))
    original_matrix = []

    for i in range(rows):
        row_input = input(f"Введите элементы строки {i + 1} через пробел: ")
        row = list(map(int, row_input.split()))
        original_matrix.append(row)

    reflected_matrix = reflect_matrix(original_matrix)
    
    print("Исходная матрица:")
    for row in original_matrix:
        print(row)
    
    print("\nЗеркально отраженная матрица:")
    for row in reflected_matrix:
        print(row)
