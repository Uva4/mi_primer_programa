
mi_lista = []

input_usuario = input('Que quieres comprar (Escribe FIN para terminar): ')

while input_usuario != 'FIN':
    mi_lista.append(input_usuario)
    input_usuario = input('Que quieres comprar (Escribe FIN para terminar): ')

for item in mi_lista:
    print(Tengo que comprar {}.format(item))


