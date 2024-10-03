#exercicio 3 - recebendo o raio de uma circunferência
raio = float(input('Insira o Raio da circunferência: '))
pi = 3.14

#condicional
if raio < 0:
    print('O raio não pode ser negativo.')

else:
    #calculo do raio:
    area = pi * raio**2
    #mostrando a área
    print(f'A área da circunferência é igual a: {area:.4f}')


