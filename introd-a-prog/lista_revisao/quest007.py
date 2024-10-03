#Programa que escolhe um número aleatório e faz com que o usuário tenha que tentar adivinhar.
import random

n1 = random.randint(1, 100)
n2 = random.randint(101, 1000)
#Gerando um numero aleatorio
senha = random.randint(n1, n2)
tentativa = 0
total_tent = 0

print(f'Número aleatório gerado em um intervalo de {n1} até {n2}')
print('Roleta da sorte! Adivinhe o número gerado para ganhar $$$')

#Pedindo ao usuário um numero para tentar acertar
#Loop - informar se é maior ou menor
while tentativa != senha:
    tentativa = int(input('Qual número achas que foi gerado? '))
    total_tent += 1
    print('Você errou!')
    if tentativa > senha:
        print('O número gerado é MENOR que o seu chute')
        print("<")
    else:
        print('O número gerado é MAIOR que o seu chute')
        print(">")
    

print(f'Parabéns! Você acertou o número aleatório gerado! Era o número {senha}')
print(f"Você precisou de {total_tent} tentativas para acertar!")