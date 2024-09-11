# Практическая работа № 16. #

### Тема: Формирование потока ввода-вывода ###

### Цель: совершенствование навыков составления программ на основе потоков ###

#### Ход работы ####

##### Задание: #####

> 11. Описать процедуру DecodeText(S, K), которая дешифрует текстовый файл с именем S, зашифрованный с использованием кодового смещения K (способ шифрования описан в задании 10). Используя эту процедуру и зная кодовое смещение K, расшифровать файл с указанным именем.

##### Контрольный пример: #####

> Записываю в файл (предварительно, в encrypted.txt) "волонтёр", программа выведет "ялилкпён"
> Записываю в файл "ыифхргзщгхгв тугнхлнг", программа выведет "шестнадцатая практика".
> Записываю в файл "SPQR! Кесарь рулит.", программа выведет "SPQR! Звоэнщ нриеп."

##### Системный анализ: #####

> Входные данные: char.

> Промежуточные данные: lc_alphabet, uc_alphabet, text, original_index, new_index, S, K, decrypted_text.

> Выходные данные: result.

##### Блок-схема: #####

![блок-схема](block.png)

##### Код программы: #####
```python
def DecodeText(S, K):
    lc_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    uc_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    decrypted_text = ''

    with open(S, 'r', encoding='utf-8') as file:
        text = file.read()

    for char in text:
        if char in lc_alphabet:
            original_index = lc_alphabet.index(char)
            new_index = (original_index - K) % len(lc_alphabet)
            decrypted_text += lc_alphabet[new_index]
        elif char in uc_alphabet:
            original_index = uc_alphabet.index(char)
            new_index = (original_index - K) % len(uc_alphabet)
            decrypted_text += uc_alphabet[new_index]
        else:
            decrypted_text += char

    return decrypted_text

result = DecodeText('encrypted.txt', 3)
print(result)
```
##### Результат работы программы: #####

* Ввод 1

![Снимок1](screen1.png)

* Ввод 2

![Снимок2](screen2.png)

* Ввод 3

![Снимок3](screen3.png)

##### Вывод по проделанной работе: #####

> и почему букву ё недооценивают?