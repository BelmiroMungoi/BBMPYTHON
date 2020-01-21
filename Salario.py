print('=================== Salario ====================')
s = float(input('Insira a salario do funcionario: '))
ns = s + (s*0.15)
print('O salario original do funcionario é de {:.2f} mts\nCom o aumento de 15% o salário sera {:.2f} mts'.format(s, ns))
