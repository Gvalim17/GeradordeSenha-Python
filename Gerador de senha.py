import random
import string

completo = string.ascii_letters + string.digits + string.punctuation
pedido_usuario = ''


def gerar_senha(pedido, tamanho):
    senha = ''
    for i in range(tamanho):
        senha += random.choice(pedido)
    return senha


def get_tamanho():
    while True:
        tamanho_usuario = input('Insira quantos caracteres deseja (número inteiro positivo): ')
        if tamanho_usuario.isdigit() and int(tamanho_usuario) > 0:
            return int(tamanho_usuario)
        else:
            print('Insira um número inteiro positivo!')


while True:
    print('1. Gerar senha aleatória;\n2. Gerar senha a partir de uma base de caracteres;\n3. Sair do programa.')
    opcao = input('--> ')
    if opcao == '1':
        print(gerar_senha(completo, get_tamanho()))
    elif opcao == '2':
        pedido_usuario = input('Informe sua senha padrão: ')
        if len(pedido_usuario) < 6:
            print('No mínimo 6 caracteres!')
        else:
            senha = ''.join(random.sample(pedido_usuario, len(pedido_usuario)))
            print(senha)
    elif opcao == '3':
        print('Programa encerrado')
        break
    else:
        print('Opção inválida!')
