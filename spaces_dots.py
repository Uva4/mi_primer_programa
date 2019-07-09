

user_sentence = input('Escribe una frase: ')

space = ' '
dot = '.'
comma = ','

n_space = 0
n_dots = 0
n_commas = 0


for letra in user_sentence:
    if letra in space:
        n_space += 1
    elif letra in dot:
        n_dots += 1
    elif letra in comma:
        n_commas += 1

print('Espacios = {}'.format(n_space))
print('Puntos = {}'.format(n_dots))
print('Comas = {}'.format(n_commas))







