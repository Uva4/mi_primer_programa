

operacion_elegida = input('Elige una operacion: Multiplicar / Dividir / Sumar / Restar:').upper()

primer_numero = int(input('Primer Numero:'))

segundo_numero = int(input('Segundo Numero: '))



if operacion_elegida == 'MULTIPLICAR':
    print('Resultado = {}'.format(primer_numero * segundo_numero))
elif operacion_elegida == 'DIVIDIR':
    print('Resultado = {}'.format(primer_numero / segundo_numero))
elif operacion_elegida == "SUMAR":
    print('Resultado = {}'.format(primer_numero + segundo_numero))
elif operacion_elegida == 'RESTAR':
    print('Resultado = {}'.format(primer_numero - segundo_numero))







