#exercicio 6 - tabuada
print("Tabuada.")
num = int(input('Escolha um número de 0 a 10: '))

#caso seja maior que 10
while num > 10:
    print('Você não entendeu?. Eu disse de 0 a 10.')
    num = int(input('Escolha um número de 0 a 10: '))

#tabuada em si.
for i in range (11):
    print(f'{i} =', num * i)

