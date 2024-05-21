from os import set_inheritable
from controller import *


while True:
    print('=========== [MENU] ============')
    decidir = int(input('Digite 1 para cadastrar\n'
                    'Digite 2 para Logar\n'
                    'Digite 3 para sair\n'))
    
    if decidir == 1:
        nome = input('Digite seu nome:\n')
        email = input('Digite seu email:\n')
        senha = input('Digite sua senha:\n')
        
        resultado = ControllerCadastro.cadastrar(nome, email, senha)

        if resultado == 2:
            print('Tamanho do nome digitado inválido\n')
        elif resultado == 3:
            print('E-mail maior que 200 caracteres\n')
        elif resultado == 4:
            print('Tamanho da senha inválido\n')
        elif resultado == 5:
            print('E-mail já cadastrado\n')
        elif resultado == 6:
            print('Erro interno do sistema\n')
        elif resultado == 1:
            print('Cadastro realizado com sucesso\n')

    elif decidir == 2:
        email = input('Digite seu email:\n')
        senha = input('Digite sua senha:\n')
        resultado = ControllerLogin.login(email, senha)

        if not resultado:
            print('E-mail ou senha inválido(s)\n')
        else:
            print(f'Logado com sucesso ----------\n\n{resultado}\n\n-----------------------------')
            
    else:
        break