s = float(input('Digite seu salário para calcularmos o desconto no valor total: '))
sf = round(s - (s*(15/100)),2)
print('Seu salário com desconto fica de: {}R$.'.format(sf))
