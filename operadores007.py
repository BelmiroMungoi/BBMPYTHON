print('=================== Operadores aritmeticos =======================')
n1 = float(input('O primeiro valor: '))
n2 = float(input('O segundo valor: '))
s = n1 + n2
n = n1 - n2
m = n1 * n2
d = n1/n2
di = n1//n2
r = n1 % n2
e = n1**n2
print('='*25, 'RESULTADO', '='*25,'\n')
print('A soma é igual a {}\nA diferenca é igual a {}\nA produto é igual a {}\nA divisao é igual a {:.2f}\nA divisao inteira é igual a {}\nO resto da divisao é igual a {}\nA exponeciacao é igual a {}\n'.format(s,n, m, d, di, r, e))
print('='*30, 'FIM', '='*27)