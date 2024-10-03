#exercicio 4 - login e senha
login = "Un" 
senha = "123"
tent = 0

#menu inicial
print("Sistema de ensino. Conecte-se!")
log1 = input('Usuário: ')
pwrd = input('Senha: ')

#loop até acertar a senha
while log1 != login or pwrd != senha:
    print('Usuário ou senha inválidos.')
    tent += 1 #Apenas para contar quantas tentativas o usuário fez
    log1 = input('Usuário: ')
    pwrd = input('Senha: ')

tent += 1 #para contar a tentativa correta
print('Você está logado.')
print(f'Você fez {tent} tentativas falhas')

