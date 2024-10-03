#Receba um número e some-o com os 50 números seguintes.

n1 = int(input('Digite um número: '))
n2 = n1

for i in range(50):
    n2 = n2+1
    soma = n1 + (n2)
    print(f'A soma de {n1} + {n2} é {soma}')
