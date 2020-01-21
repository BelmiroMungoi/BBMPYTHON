import math
ang = float(input('Insira quanto vale o angulo: '))
seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O seno do angulo {} é {:.2f}'.format(ang, seno))
print('O cosseno do angulo {} é {:.2f}'.format(ang, cos))
print('A tangente do angulo {} é {:.2f}'.format(ang, tan))


