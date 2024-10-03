#exercicio 5 - Ordem Crescente com IF
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))
orden = []
#Usando if
if n1 >= n2 and n1 >= n3:
    if n2 >= n3:
        orden.append(n3)
        orden.append(n2)
        orden.append(n1)
    else:
        orden.append(n2)
        orden.append(n3)
        orden.append(n1)

elif n2 >= n1 and n2 >= n3:
    if n1 >= n3:
        orden.append(n3)
        orden.append(n1)
        orden.append(n2)
    else:
        orden.append(n1)
        orden.append(n3)
        orden.append(n2)

elif n3 >= n1 and n3 >= n2:
    if n1 >= n2:
        orden.append(n2)
        orden.append(n1)
        orden.append(n3)
    else:
        orden.append(n1)
        orden.append(n2)
        orden.append(n3)

#Printando
print('Os números em ordem crescente são:', orden)