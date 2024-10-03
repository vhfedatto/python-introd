#Recebendo 20 valores inteiros. Retorne o maior e o menor;
numeros = []

for i in range(5):
    valor = int(input('Digite um número Inteiro: '))
    numeros.append(valor)

maximo = max(numeros)
minimo = min(numeros)

print(f'O maior número digitado foi {maximo}')
print(f'O menor número digitado foi {minimo}')