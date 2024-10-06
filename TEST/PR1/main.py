def is_number(value):
    try:
        float(value) 
        return True
    except ValueError:
        return False

trinum = False
while not trinum:
    user_input = input("Введите длины сторон треугольника через пробел: ")
    numbers = user_input.split()
    
    if len(numbers) != 3 or not all(is_number(num) for num in numbers):
        print("нужны всего-лишь ТРИ не вещественных числа, и они должны быть положительными.")
    else:
        a, b, c = map(float, numbers)
        if a <= 0 or b <= 0 or c <= 0:
            print("Введите положительные числа!!")
        elif a + b < c or b + c < a or a + c < b:
            print("Сумма двух меньше третьего, пж, введите другое.")
        else:
            trinum = True
print("Спасибо.")
if a == b and a != c or b == c and b != a or a == c and a != b:
    print("Мы имеем типичный равнобедренный треугольник.")
elif a != b or b != c or c != a:
    print("Мы имеем типичный разносторонний треугольник.")
elif a == b == c:
    print("Мы имеем типичный равносторонний треугольник.")