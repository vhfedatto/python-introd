#exercicio 5 - Ordem Crescente
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite um número inteiro: '))
n3 = int(input('Digite um número inteiro: '))

#Usando lista e sorte() - Poderia fazer usando if, mas ia ficar um código imenso.
nums = [n1, n2, n3]

#ordenando:
ordenados = sorted(nums)

#Printando
print('Os números em ordem crescente são:', ordenados)

#se quiser ver usando if, vá para ex005b;