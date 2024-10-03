#exercício 1 - Lista com 10 elementos (diferentes tipos de dados)
lista = []

for i in range(10):
    var1 = input(f'Digite o {i+1}º elemento: ')
    var2 = input('Qual o tipo? [int, float, string] ')

    if var2 == 'int':
        var1 = int(var1)
        lista.append(var1)
    elif var2 == 'float':
        var1 = float(var1)
        lista.append(var1)
    else:
        lista.append(var1)

    print(lista)
    print()


    lista_exercicio = [10, 'brot', 10.98, 'python', 9303.9, True, 'hello world', 5403.9, 'etc', False]

