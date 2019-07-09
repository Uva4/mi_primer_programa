
user_sentence = input('Escribe una frase: ')

vocales = ['a', 'e', 'i', 'o', 'u']

for letra in user_sentence:
    if letra in vocales:
        print('{}'.format(letra))