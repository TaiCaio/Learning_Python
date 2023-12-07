n = int(input('Digite um número inteiro e positivo: '))
if n < 0:
    print('Digite um numero maior que zero')
else:
    print('O dobro de {} é {}, o triplo é {} e sua raiz quadrada é {}'.format(n, n**2, n**3, n**(1/2)))
