def DecodeText(S, K):
    alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
    decrypted_text = ''

    with open(S, 'r', encoding='utf-8') as file:
        text = file.read()

    for char in text:
        if char in alphabet:
            original_index = alphabet.index(char)
            if original_index > 2:
                new_index = (original_index - K) % len(alphabet)
                decrypted_text += alphabet[new_index]
            else:
                new_index = (original_index - K + 32) % len (alphabet)
                decrypted_text += alphabet[new_index]
        else:
            decrypted_text += char

    return decrypted_text

# Example usage
result = DecodeText('encrypted.txt', 3)
print(result)