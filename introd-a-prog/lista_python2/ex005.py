#exercicio 5 - Soma e media
#definir a variavel da soma
soma = 0 

#pedir cada número individualmente
for pos in range (6):
    val = float(input(f'Digite o {pos + 1}º valor: '))
    soma += val

#média
med = soma / 6

print("A soma foi igual a:", soma)
print("A média foi igual a:", med)

