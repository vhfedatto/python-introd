#exercício 02 - Idade e ano de nascimento
print('Cálculo de Ano de Nascimento. Siga as instruções')

idade = int(input("Qual a sua idade? (apenas o número) "))
anoA = int(input('Em que ano estamos? '))

#cálculo do ano
ano_nasc = anoA - idade

print('Vou adivinhar o ano que você nasceu...')
print('Você nasceu em', ano_nasc)

#se quiser mais especifico, vá para "ex002b"