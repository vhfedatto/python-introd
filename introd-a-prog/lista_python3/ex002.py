#exercício 2 - Acessar o último elemento da lista.
lista = [2, 4, 6, 8, 10, 12, 14]

var1 = input('Gostaria de acessar o último elemento? [S/N] ')

if var1 == 'S':
    tamanho = len(lista)
    tam_real = tamanho - 1
    print(f'O item que está no indice {tam_real} é {lista[tam_real]}')
else:
    print()

