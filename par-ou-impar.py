numero_inteiro = int(input('Insira um número inteiro: '))
numero = numero_inteiro // 2
resto = numero_inteiro % 2
if resto == 0:
    print('O número', numero_inteiro, 'é par.')
else:
    print('O número', numero_inteiro, 'é impar.')
