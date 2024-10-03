#exercicio 2 - Imprimindo Par ou Impar - saltos
n1 = int(input('Digite um valor: '))

#verificando
if n1 % 2 == 0:
    #imprimir até o numero indicado 
    for i in range (0, n1 + 1, 2):
        print(i)
else:
    for i in range (1, n1+1, 2):
        print(i)

