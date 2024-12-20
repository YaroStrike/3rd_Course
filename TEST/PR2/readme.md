# Практическая работа № 2. #

### Тема: Тестирование "чёрным ящиком" ###

### Цель: изучить метод тестирования "чёрным ящиком" ###

#### Ход работы ####

##### Задания: #####

> 1. Написать калькулятор с небольшими багами. (В итоге взяли open-source калькуляторы на python).
>
Но грамотнее всё-таки начать с написания тестов, сначала за основу взяли калькулятор из Windows 7 с дополнением "Градусы"

> 2. Провести тестирование, составить отчёт.

##### Таблица тестов 1.py: #####

| Название теста         | Описание сценария                          | Входные данные                          | Выходные данные                | Успешность теста | Предложения по исправлению найденных ошибок | Пожелания пользователей          |
|------------------------|--------------------------------------------|----------------------------------------|--------------------------------|------------------|---------------------------------------------|----------------------------------|
| Тест линейной функции  | Проверка построения линейной функции      | a=2, b=3, x_min=0, x_max=10           | График линейной функции       | Успешно          | Убедиться в правильности ввода данных     | Добавить возможность сохранения графика |
| Тест квадратной функции| Проверка построения квадратной функции     | a=1, b=0, x_min=-10, x_max=10         | График квадратной функции     | Успешно          | Проверить обработку отрицательных значений | Возможность изменения цвета графика |
| Тест кубической функции | Проверка построения кубической функции    | a=1, b=0, c=0, x_min=-10, x_max=10    | График кубической функции     | Не успешно        | Исправить расчет коэффициентов            | Добавить возможность выбора диапазона |
| Тест степенной функции | Проверка построения степенной функции      | a=2, x_min=0, x_max=10                 | График степенной функции      | Успешно          | Проверить обработку дробных значений      | Возможность выбора степени функции  |
| Тест логарифмической функции | Проверка построения логарифмической функции | a=1, x_min=1, x_max=10                 | График логарифмической функции| Не успешно        | Исправить обработку нуля и отрицательных значений | Добавить возможность выбора основания логарифма |
| Тест показательной функции | Проверка построения показательной функции | a=2, x_min=0, x_max=10                 | График показательной функции  | Успешно          | Проверить корректность экспоненты         | Возможность выбора базового числа   |
| Тест тригонометрической функции (sin) | Проверка построения синусоиды | a=1, b=0, x_min=0, x_max=6.28         | График синусоиды             | Успешно          | Добавить возможность выбора периода        | Добавить сетку на графике       |
| Тест тригонометрической функции (cos) | Проверка построения косинусоиды | a=1, b=0, x_min=0, x_max=6.28         | График косинусоиды           | Не успешно        | Исправить отображение графика             | Возможность выбора цвета графика   |
| Usability-тест | Проверка функциональности кнопок | ввод/нажатие | должны были быть | Не успешно | Пофиксить кнопку "Очистить график" | Динамическое изменение графика, если менять цифры в текстбоксах. |

##### Таблица тестов Calculator.py: #####


| Название теста         | Описание сценария                          | Входные данные                          | Выходные данные                | Успешность теста | Предложения по исправлению найденных ошибок | Пожелания пользователей          |
|------------------------|--------------------------------------------|----------------------------------------|--------------------------------|------------------|---------------------------------------------|----------------------------------|
| Тест нажатия кнопки 1  | Проверка нажатия кнопки "1"               | Нажатие кнопки "1"                     |  "1"                | Успешно          | Убедиться в правильности отображения       | Добавить анимацию нажатия кнопки |
| Тест операции сложения  | Проверка операции сложения                 | Ввод "1", нажатие "+", ввод "2", нажатие "=" |  "3"                | Успешно          | Проверить корректность вычислений          | Возможность отображения истории операций |
| Тест операции вычитания | Проверка операции вычитания                | Ввод "5", нажатие "-", ввод "3", нажатие "=" |  "2"                | Успешно          | Проверить корректность вычислений          | Возможность отображения истории операций |
| Тест операции умножения | Проверка операции умножения                | Ввод "3", нажатие "x", ввод "4", нажатие "=" |  "12"               | Успешно          | Проверить корректность вычислений          | Возможность отображения истории операций |
| Тест операции деления   | Проверка операции деления                  | Ввод "8", нажатие "/", ввод "4", нажатие "=" |  "2"                | Успешно          | Проверить корректность вычислений          | Возможность отображения истории операций |
| Тест очистки ввода      | Проверка кнопки "C"                        | Нажатие "C"                            |  "0"                | Успешно          | Убедиться в сбросе всех значений           | Добавить подтверждение очистки    |
| Usability-тест          | Проверка функциональности всех кнопок      | Нажатие всех кнопок                    | Все значения должны отображаться | Успешно       | Сделать другие кнопки и анимацию        | Поддержка ввода с клавиатуры. |

##### Результат работы программы: #####

* Они запускаются с нужными библиотеками: tkinter, numpy, matplotlib

![Снимок1](screen1.png)

##### Вывод по проделанной работе: #####

> Очень интересно, это белый ящик, поэтому жаль что пришлось видеть код.