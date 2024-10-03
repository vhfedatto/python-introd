#exercicio 3 - Continuar ou sair
continuar = 1
sair = 2
print('Seja bem-vindo ao nosso sistema. O que gostarias de fazer?')
op = int(input('Continuar [1], sair [2] '))

#verificar o numero e se for 2 (sair). Se for 1 ou diferente (continuar ou valor invalido - e continua também).
while op != 2:
    op = int(input('Continuar [1], sair [2] '))
    if op != 1 and op != 2:
        print('Valor inválido')

        