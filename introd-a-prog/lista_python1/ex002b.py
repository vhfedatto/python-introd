#exercício 02 - Idade e ano de nascimento (sendo mais especifico)
print('Cálculo de Ano de Nascimento. Siga as instruções')

idade = int(input("Qual a sua idade? (apenas o número) "))
dia_nasc, mes_nasc = map(int, input('Em que dia e mês você nasceu? (DD MM - separe com espaço) ').split())
dia, mes = map(int, input('Em que dia e mês estamos? (DD MM - separe com espaço) ').split())
anoA = int(input('Em que ano estamos? '))

#cálculo do ano em que ele nasceu
ano_nasc = anoA - idade

#Ajuste do ano caso o usuário não tenha feito aniversário ainda.
if (mes < mes_nasc) or (mes == mes_nasc and dia < dia_nasc):
    ano_nasc -= 1

#Magica acontecendo...
print('Vou adivinhar o ano que você nasceu...')
print('Você nasceu em', ano_nasc)