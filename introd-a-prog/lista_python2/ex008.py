#exercicio 8 - Idades
#Declarando as variaveis de conta
jov = 0
adul = 0
idosos = 0
op = 0

#informando idades:
while op != 2:
    idd = int(input(f'Informe uma idade: '))
    op = int(input('Continuar [1], Sair [2]'))
    #confirmando condição de parada
    if op != 1 and op != 2:
        print('Valor inválido')
    #analise das idades e soma nas variáveis
    if idd <= 25:
        jov += 1
    elif idd > 25 and idd <= 60:
        adul += 1
    else:
        idosos += 1

#apresentando resultados   
print('Jovens:', jov)
print('Adultos:', adul)
print('Idosos:', idosos)

