print('================ Desconto ================')
p = float(input('Insira o preco do produto: '))
d = float(input('Insira a percentagem de desconto desejada: '))
np = p-(p*d/100)
print('='*30)
print('O produto que custava {:.2f} mts\nCom um desconto de {}%\nPassará a custar {:.2f} mts'. format(p, d, np))
print('='*30)
