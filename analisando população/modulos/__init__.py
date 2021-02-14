from time import sleep
from datetime import date


def Cabecalho(msg):
    print(f"{'-'*40}")
    Cores(msg.center(40), 1, 'amarelo')
    print(f"{'-'*40}")

def Menu(lista):
    for c in range(0, len(lista)):
        Cores(f"[{c+1}] {lista[c]}", 0, 'branco')
    print(f'{"-"*40}')


def LeiaInt(msg):
    while True:
        op = input(msg)
        if(op.isnumeric()):
            op = int(op)
            if (0 < op > 6):
                Cores('Opção Inválida...', 0, 'vermelho')
            else:
                return op
        else:
            Cores('ERRO! Digite um número inteiro...', 0, 'vermelho')


def AdicionarPessoa(file, nome, nasc, sexo, profissao):
    a = open(file, 'a')
    a.write(f'{nome};{nasc};{sexo};{profissao}\n')
    Cores('Registro adicionado com sucesso.', 1, 'verde')
    a.close()


def ListarPessoas(file):
    a = open(file, 'rt')
    for linha in a:
        dado = linha.split(';')
        dado[3] = dado[3].replace('\n', '')
        print(f'Nome: {dado[0]} \nAno nascimento: {dado[1]} \nSexo: {dado[2]} \nProfissão: {dado[3]}')
        print('-'*40)
        sleep(0.4)
    a.close()


def LeiaSexo(msg):
    while True:
        sexo = str(input(msg)).upper()[0]
        if(sexo == 'M' or sexo == 'F'):
            return sexo
        else:
            Cores('Sexo Inválido...', 1, 'vermelho')

def Estatistica(file):
    a = open(file, 'rt')
    atual = date.today().year
    soma = cont = contF = contM = contMaior = maior = menor = 0
    nomeMaior = nomeMenor = ' '
    for linha in a:
        dado = linha.split(';')
        idade = atual - int(dado[1])
        nome = dado[0]
        soma += idade
        if(idade >= 18):
            contMaior += 1
        if(dado[2] == 'F'):
            contF += 1
        if(dado[2] == 'M'):
            contM += 1
        cont += 1
        if(cont == 1):
            maior = idade
            nomeMaior = nome
            menor = idade
            nomeMenor = nome
        else:
            if(idade > maior):
                maior = idade
                nomeMaior = nome
            if(idade < menor):
                menor = idade
                nomeMenor = nome
    media = soma/cont
    Cores(f'A população total é {cont} pessoas.', 1, 'azul')
    Cores(f'A média de idade é {media:.2f} anos.', 1, 'azul')
    Cores(f'Há {contF} pessoas do sexo femenino.', 1, 'azul')
    Cores(f'Há {contM} pessoas do sexo masculino.', 1, 'azul')
    Cores(f'Há {contMaior} pessoas maior de idade.', 1, 'azul')
    Cores(f'{nomeMaior} é a pessoa mais velha e tem {maior} anos.', 1, 'azul')
    Cores(f'{nomeMenor} é a pessoa mais nova e tem {menor} anos.', 1, 'azul')
    a.close()

def EliminarRegistro(file, nome):
    a = open(file, 'rt')
    lista = list()
    i = 0
    for linha in a:
        dado = linha.split(';')
        if(dado[0] != nome):
            lista.append(linha)
        else:
            i += 1
    a.close()
    b = open(file, 'wt')
    for c in range(0, len(lista)):
        b.write(f'{lista[c]}')
    b.close()
    if(i == 0):
        Cores(f'{nome} não consta na lista', 1, 'vermelho')
    else:
        Cores(f'Registro eliminado com sucesso', 1, 'verde')


def Cores(msg, estilo=0, cor='branco'):
    cor.lower()
    if(cor == 'vermelho'):
        cor = 31
    elif(cor == 'verde'):
        cor = 32
    elif(cor == 'amarelo'):
        cor = 33
    elif(cor == 'azul'):
        cor = 34
    elif(cor == 'magenta'):
        cor = 35
    elif(cor == 'cinza'):
        cor = 36
    elif(cor == 'branco'):
        cor = 97
    elif(cor == 'preto'):
        cor = 30
    elif(cor == 'cizento'):
        cor = 37
    print(f'\033[{estilo};{cor}m{msg}\033[m')


def LeiaOpc(msg):
    while True:
        op = input(msg)
        if op.isnumeric():
            op = int(op)
            if 4 >= op >= 1:
                return op
            else:
                print('Opção Inválida...')
        else:
            print('Erro!!! Digite um número entre 1 a 4...')


def AlterarDados(file, nome, atual, novo):
    a = open(file, 'rt')
    lista = list()
    i = 0
    for linha in a:
        dado = linha.split(';')
        dado[1] = int(dado[1])
        for c in range(0, 4):
            if(nome == dado[0] and atual == dado[c]):
                dado[c] = novo
                i += 1
        lista.append(dado)
    a.close()
    b = open(file, 'wt')
    for c in range(0, len(lista)):
        b.write(f'{lista[c][0]};{lista[c][1]};{lista[c][2]};{lista[c][3]}')
    b.close()
    if(i == 0):
        Cores('Não foi possível realizar a alteração.', 1, 'vermelho')
    else:
        Cores('Alteração realizada com sucesso.', 1, 'verde')