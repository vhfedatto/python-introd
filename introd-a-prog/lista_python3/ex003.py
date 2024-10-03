#exercício 3 - Adicionando elementos de uma vez ao final da lista
lista = [5, 10, 15, 20]

print(lista)
var1 = input('Gostaria de adicionar os elementos 25, 30, 35, 40 ao final da lista? [S/N] ')

if var1 == "S":
    lista2 = [25, 30, 35, 40]
    lista.extend(lista2)
    print(lista)
else:
    print()