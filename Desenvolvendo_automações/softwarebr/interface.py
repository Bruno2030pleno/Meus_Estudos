from pathlib import Path as path
from gerenciador_arquivos import Arquivo, ArquivoJSON,VarreduraJSON, ArquivoExcel, ArquivoCsv
from banco_dados import BancoDeDadosSqlite
from config import PASTA, PASTA1,BANCO


# CRIANDO O MENU DE OPÇÕES
def iniciar_menu():
    def opção_1(nome_do_arquivo):
        conteudo = input('agora me fala o conteudo? ')
        caminho = path(PASTA)
        arquivo = Arquivo(caminho/nome_do_arquivo, conteudo)
        arquivo.cria_arquivo()
        banco = BancoDeDadosSqlite()
        banco.salvar_dados('criando arquivo txt', nome_do_arquivo, "txt", BANCO)

    def opção_2(nome_do_arquivo):
        exibir = ArquivoJSON(path(PASTA)/nome_do_arquivo)
        exibir.exibir_arquivoJson()

    def opção_3(nome_do_arquivo):
        caminho = path(PASTA)
        arquivo = Arquivo(caminho/nome_do_arquivo)
        arquivo.ler_arquivo()

    def opção_4(nome_do_arquivo):
        caminho = path(PASTA)
        arquivo = Arquivo(caminho/nome_do_arquivo)
        if (caminho/nome_do_arquivo).exists():
           arquivo.deletar_arquivo() 
           banco = BancoDeDadosSqlite()
           dado = path(nome_do_arquivo).suffix
           banco.salvar_dados('deletar arquivos',nome_do_arquivo,dado,BANCO) 

    def opção_5(nome_do_arquivo):
        caminho = path(PASTA1)
        arquivo = VarreduraJSON(caminho/nome_do_arquivo)
        arquivo.varrerJson()

    def opção_6(nome_do_arquivo):
        caminho = path(PASTA)
        arquivo_excel = ArquivoExcel(caminho/nome_do_arquivo)
        arquivo_excel.ler_arquivos_excel() 

    def opção_7(_):
        banco = BancoDeDadosSqlite()
        banco.exibir_dados_do_banco()

    def opção_8(nome_do_arquivo):
        caminho = path(PASTA)
        csv = ArquivoCsv(caminho/nome_do_arquivo)
        csv.ler_arquivo_csv()

    opcao = {
        '1':opção_1,
        '2':opção_2,
        '3':opção_3,
        '4':opção_4,
        '5':opção_5,
        '6':opção_6,
        '7':opção_7, 
        '8': opção_8    
    }

    while True:
        print("\n---MENU DE OPÇÕES---")
        print('OPÇÃO 1 CRIAR ARQUIVO TXT')
        print('OPÇÃO 2 EXIBIR ARQUIVO jSON')
        print('OPÇÃO 3 LER ARQUIVOS')
        print('OPÇÃO 4 DELETAR UM ARQUIVO')
        print('OPÇÃO 5 VARRER ARQUIVOS JSON')
        print('OPÇAO 6 LER ARQUIVOS EXCEL')
        print("OPÇÃO 7 EXIBIR OS DADOS DO BANCO")
        print("OPÇÃO 8 EXIBIR ARQUIVO CSV")
        Usuario = input("\nDentre as opções, qual você deseja? / ou Enter para sair ")
        if Usuario == '':
            print('sessão finalizada')
            break
        if Usuario in opcao:
            nome_do_arquivo = input('digite o nome do arquivo ou diretorio, enter para sair: ')
            if nome_do_arquivo == '':
               continue
            opcao[Usuario](nome_do_arquivo)
        else:
            print('Opção invalida!!!')
            continue
iniciar_menu()       