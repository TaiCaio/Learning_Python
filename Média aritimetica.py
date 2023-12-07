n = float(input('Digite as médias do aluno: '))
n2 = float(input())
m = (n + n2) / 2
if m < 6.99:
    print('A média do aluno foi de: {}. Reprovado'.format(m))
else:
    print('A média do aluno foi de: {}. Aprovado'.format(m))
