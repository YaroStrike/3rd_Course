# Практическая работа № 2. #

### Тема: Тестирование "чёрным ящиком" ###

### Цель: изучить метод тестирования "чёрным ящиком" ###

#### Ход работы ####

##### Задания: #####

> 1. Написать калькулятор с небольшими багами. (В итоге взяли open-source калькуляторы на python).
>
Но грамотнее всё-таки начать с написания тестов, сначала за основу взяли калькулятор из Windows 7 с дополнением "Градусы"

> 2. Провести тестирование, составить отчёт.

##### Таблица тестов: #####

| Название теста                | Описание сценария                          | Входные данные | Выходные данные | Удачное/Неудачное тестирование | Предложения по исправлению найденных ошибок | Пожелания пользователей          |
|-------------------------------|--------------------------------------------|----------------|-----------------|-------------------------------|--------------------------------------------|----------------------------------|
| Тестирование преобразования    | Преобразование градусов в радианы         | 180            | 3.14159         | Удачное                       | Я бы выдал более точное значение п) | Добавить возможность выбора единиц |
| Тестирование "sin" и другой тригонометрии | Вычисление синуса угла                    | 90             | 1               | Удачное                       | Нет                                     | Поддержка углов в градусах и радианах |
| Тестирование "cos"    | Вычисление косинуса угла                  | 60             | 0.5             | Удачное                       | Нет                                     | Поддержка углов в градусах и радианах |
| Тестирование "tan"   | Вычисление тангенса угла                  | 45             | 1               | Удачное                       | Нет                                     | Поддержка углов в градусах и радианах |
| Тестирование "ln" | Вычисление натурального логарифма | 11             | 2.39789 | Удачное                       | Нет                                     | Поддержка настройки точности |
| Тестирование деления на ноль  | Проверка деления на ноль                  | 10 / 0        | Ошибка          | Удачное                       | Предположить что деление на 0 ведёт в бесконечность) | Более информативные сообщения об ошибках |
| Тестирование округления        | Округление значения синуса                 | 0.5            | 1               | Удачное                       | Нет                                     | Возможность выбора точности округления |
| Тестирование ошибок ввода      | Ввод некорректного значения                | "abc"          | Ошибка          | Удачное                       | Улучшить сообщение об ошибке            | Более информативные сообщения об ошибках |
| Тестирование диапазона         | Проверка значений за пределами диапазона   | 400            | Ошибка          | Удачное                       | Нет                                     | Предупреждение о том, что градусы ограничены от 0 до 360 |
| Тестирование производительности | Измерение времени выполнения вычислений    | 45             | Ну, может быть на линуксе быстрее | Удачное                       | Оптимизировать алгоритмы                 | Ускорить вычисления для больших значений |
| Тестирование пользовательского интерфейса | Проверка доступности функций         | -              | -               | Удачное                       | Улучшить интерфейс                       | Добавить подсказки для пользователей |
| Тестирование на разных платформах | Проверка работы на различных ОС         | -              | -               | Удачное                       | Нет                                     | Поддержка мобильных платформ      |
| Тестирование на разных языках  | Проверка локализации интерфейса           | -              | -               | Удачное                       | Нет                                     | Поддержка дополнительных языков   |
| Тестирование на больших числах  | Проверка работы с большими значениями    | 1e+10          | 12.71828      | Удачное                       | Нет                                     | Поддержка научной нотации         |


##### Дополнения: #####
```С

```
##### Результат работы программы: #####

* Ввод 1

![Снимок1](screen1.png)

##### Вывод по проделанной работе: #####

> 