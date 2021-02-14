from modulos import *

ficheiro = 'populacao.txt'
Cabecalho("População de CV-SV")
Menu(['Listar as pessoas', 'Adiciodado[1] = int(dado[1])nar uma nova pessoa', 'Elimar registro', 'Alterar dados','Monstrar as estatisticas', 'Sair do sistema'])
op = LeiaInt('Sua opção: ')
if(op == 1):
    Cabecalho('Listagem da População')
    ListarPessoas(ficheiro)
elif(op == 2):
    Cabecalho('Adicinar Pessoa')
    nome = str(input('Nome: ')).title()
    nascimento = int(input('Ano Nascimento: '))
    sexo = LeiaSexo('Sexo: ')
    profissao = str(input('Profissão: ')).title()
    AdicionarPessoa(ficheiro, nome, nascimento, sexo, profissao)
elif(op == 3):
    Cabecalho('Eliminando Registro')
    nome = str(input('Nome: ')).title()
    EliminarRegistro(ficheiro, nome)
elif(op == 4):
    Cabecalho('Alterar dados')
    Menu(['Alterar nome', 'Alterar data nascimento', 'Alterar sexo', 'Alterar profissão'])
    opc = LeiaOpc('Sua opção: ')
    nome = str(input('Nome: '))
    if(opc == 1):
        atual = str(input('Nome Atual: ')).title()
        novo = str(input('Novo nome: ')).title()
    elif(opc == 2):
        atual = int(input('Ano nascimento atual: '))
        novo = int(input('Novo ano nascimnto: '))
    elif(opc == 3):
        atual = LeiaSexo('Sexo actual: ')
        novo = LeiaSexo('Novo sexo: ')
    elif(opc == 4):
        atual = str(input('Atual profissão: ')).title()
        novo = str(input('Novo profissão: ')).title()
    AlterarDados(ficheiro, nome, atual, novo)
elif(op == 5):
    Cabecalho('Monstrando Estatistica')
    Estatistica(ficheiro)
Cabecalho('Saindo do Programa')


