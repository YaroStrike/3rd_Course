def check_input(user_input):
    if user_input.isdigit():
        return f"The input '{user_input}' is a valid integer."
    else:
        return f" это '{user_input}', а не число"

# Example usage
input_value = input("Please enter a number: ")
result = check_input(input_value)
print(result)

def find_min_positive_max_negative():
    N = int(input("Ввод N: "))
    numbers = []

    for i in range(N):
        while True:
            try:
                number = int(input(f"Введите ЧИСЛО {i + 1}: "))
                numbers.append(number)
                break 
            except ValueError:
                print("Я ж сказал число")

    min_positive = float('inf')
    max_negative = float('-inf')
    min_positive_index = -1
    max_negative_index = -1

    for index, number in enumerate(numbers):
        if number > 0 and number < min_positive:
            min_positive = number
            min_positive_index = index
        elif number < 0 and number > max_negative:
            max_negative = number
            max_negative_index = index

    if min_positive_index != -1 and (max_negative_index == -1 or min_positive_index < max_negative_index):
        print(f"Минимальное положительное {min_positive} появилось раньше.")
    elif max_negative_index != -1:
        print(f"Максимальное негативное {max_negative} появилось раньше.")
    elif N == 0:
        print(f"Последовательность равна 0!!")
    else:
        print("Здесь нет ни положительных, ни отрицательных чисел.")

find_min_positive_max_negative()
