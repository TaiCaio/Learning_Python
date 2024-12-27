n = float(input('Digite uma distância em metros: '))
print('-'*12)
print('Selecione uma das medidas para ser convertida\n 1-km\n 2-hm\n 3-dam\n 4-dm\n 5-cm\n 6-mm')
print('-'*12)
s = int(input())

if s == 1:
    print('A distancia convertida é de: {} km'.format(n/1000))
if s == 2:
    print('A distancia convertida é de: {} hm'.format(n/100))
if s == 3: 
    print('A distancia convertida é de: {} dam'.format(n/10))
if s == 4:
    print('A distancia convertida é de: {} dm'.format(n*10))
if s == 5:
    print('A distancia convertida é de: {} cm'.format(n*100))
if s == 6:
    print('A distancia convertida é de: {} mm'.format(n*1000))
