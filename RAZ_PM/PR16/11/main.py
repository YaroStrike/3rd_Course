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
