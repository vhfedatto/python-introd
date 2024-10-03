#exercicio 6 - Divisivel por 5
num = int(input('Digite um número inteiro: '))

#dividindo por 5:
resul = num / 5

#% (módulo) - verifica o resto da divisão
if num % 5 == 0:
    print(f'{num} é divisivel por 5.') 

else:
    print(f'{num} não é divisivel por 5.') 