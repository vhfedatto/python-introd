#exercicio 1 - Calcular Bhaskara
#Importando a raiz quadrada
import math
#Iniciando a calculadora
print('Cálculo de Bhaskara. Siga as instruções')
print()
a = float(input('Primeiro número: '))
b = float(input('Segundo número: '))
c = float(input('Terceiro número: '))
#Calculo de Delta
delta = (b**2) - 4 * a * c
#Condicionais
if delta > 0 and a != 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f'Resultado de X1 = {x1:.5f}')
    print(f'Resultado de X2 = {x2:.5f}')

else:
    print('A equação não possui raízes reais.')


