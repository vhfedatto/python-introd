#exercicio 7 - Sequência de Fibonacci
#Primeiras variaveis - lista e limita
fib = [0, 1]
lim = int(input('Digite o limite: '))

#Fazendo a sequencia
while True:
    nxt = fib[-1] + fib[-2]
    if nxt > lim:
        break
    fib.append(nxt)

#Apresentando os resultados
print(fib)
