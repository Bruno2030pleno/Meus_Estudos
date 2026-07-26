from pathlib import Path as path
import openpyxl
import json
PASTA = "/home/brunodev/arquivos_Json/"
PASTA1 = "/home/brunodev/"
class Arquivo:
    def __init__(self, nome_do_arquivo, conteudo_do_arquivo=''):
        self.nome_do_arquivo = nome_do_arquivo
        self.conteudo_do_arquivo = conteudo_do_arquivo
    def cria_arquivo(self):
        if path(self.nome_do_arquivo).exists():
            print('o arquivo ja existe')
        else:
            with open(self.nome_do_arquivo, 'w', encoding='utf-8') as arquivo_teste:
                arquivo_teste.write(self.conteudo_do_arquivo)
                print('arquvo criado com sucesso')
    def ler_arquivo(self):
        try:
            with open(self.nome_do_arquivo, 'r', encoding='utf-8') as leitura:
                tela = leitura.read()
                print(tela) 
        except FileNotFoundError:
            print(f'arquivo não encontrado {self.nome_do_arquivo} ')
        except UnicodeDecodeError:
            print('erro de codec!! ') 
            try:
                with open(self.nome_do_arquivo, 'r', encoding='latin-1') as leitura:
                    tela = leitura.read()
                    print(tela) 
            except Exception:
                print(f'não foi possível ler o arquivo')
    def adicionar_arquivo(self):
        if path(self.nome_do_arquivo).exists():
            with open(self.nome_do_arquivo, 'a', encoding='utf-8') as adiciona:
                adiciona.write(self.conteudo_do_arquivo + '\n')  
                print('arquivo adicionado com sucesso')  
        else:
            print('arquivo nao existe!!')
    # preciso colocar uma pergunta sobre qual arquivo o usuario deseja apagar
    def deletar_arquivo(self):
        if path(self.nome_do_arquivo).exists():
           path(self.nome_do_arquivo).unlink() # apaga arquivos: 01/07/2026
           print('arquivo removido')
        else:
            print('arquivo nao existe!!')
# nessa parte do codigo estou reforçando o meu conhecimento em escrever arquivos Json
class ArquivoJSON(Arquivo):
    def __init__(self, nome_do_arquivo, conteudo_do_arquivo=''): # tambem estou reforçando
        super().__init__(nome_do_arquivo, conteudo_do_arquivo)
        self.dicionario = {}
    def criar_arquivoJson(self):
        if path(self.nome_do_arquivo).exists():
           print('o arquivo ja existe!!')    
        else:                                    
             # parents=True → cria o que faltar | exist_ok=True → não reclama se já existir
            path(PASTA).mkdir(parents=True, exist_ok=True) # esse pequeno codigo de verificação nao foi eu que fiz, mas serve como aprendizado
            with open(self.nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(self.dicionario, arquivo) # reforçando meu conhecimento 
                print('arquivo criado com sucesso') 
    def exibir_arquivoJson(self):
        try: 
            if path(self.nome_do_arquivo).exists():
                with open(self.nome_do_arquivo, 'r', encoding='utf-8') as leituras:
                    leitura = json.load(leituras) 
                    print(leitura)
            else:
                print('o arquivo para leitura não existe!!')
        except json.JSONDecodeError:
           print('arquivo JSON vazio ou inválido!')        
    def adicionar_dados(self):
        while True:
            chave = input('digite a chave: ')
            if chave.lower() == '':
                break
            valor = input('digite o valor')
            self.dicionario[chave] = valor
class VarreduraJSON:
    def __init__(self, caminho):
        self.caminho =  caminho
    def varrerJson(self):
        if path(self.caminho).exists():
            pasta = path(self.caminho)    
            encontrou = False
            for arquivo in pasta.glob('*.json'): 
                print(arquivo)
                with open(arquivo, 'r', encoding='utf-8') as arquivo:
                    leitura = json.load(arquivo)
                    print('=============================================')
                    print(json.dumps(leitura,  indent=2, ensure_ascii=False))
                    print('=============================================')
                encontrou = True
            if not encontrou:        
                print('arquivo não existe')
        else:   
            print('pasta não existe')  
class ArquivoExcel(Arquivo):
    def __init__(self, nome_do_arquivo, conteudo_do_arquivo=''):
        super().__init__(nome_do_arquivo, conteudo_do_arquivo)
        self.dados = [] 
    def ler_arquivos_excel(self):
        try:    
            workbook = openpyxl.load_workbook(self.nome_do_arquivo)
            planilha = workbook.active  # pega a aba ativa (a que está selecionada)
            for linha in planilha.iter_rows(values_only=True):
                print(linha)  # cada "linha" já vem como uma tupla com os valores das células     
                self.dados.append(linha)
        except FileNotFoundError:
            print(f'arquivo não encontrado {self.nome_do_arquivo} ')    
# CRIANDO O MENU DE OPÇÕES
def opção_1(nome_do_arquivo):
    conteudo = input('agora me fala o conteudo? ')
    caminho = path(PASTA)
    arquivo = Arquivo(caminho/nome_do_arquivo, conteudo)
    arquivo.cria_arquivo()
    print('arquivo txt criado com sucesso')
def opção_2(nome_do_arquivo):
    caminho = path(PASTA)
    jsonn0 = ArquivoJSON(caminho/nome_do_arquivo)
    jsonn0.adicionar_dados()
    jsonn0.criar_arquivoJson()
    print('arquivo json criado com sucesso')
def opção_3(nome_do_arquivo):
    varrer = ArquivoJSON(path(PASTA)/nome_do_arquivo)
    varrer.exibir_arquivoJson()
    print('arquivos varridos com sucesso')
def opção_4(nome_do_arquivo):
    caminho = path(PASTA)
    arquivo = Arquivo(caminho/nome_do_arquivo)
    arquivo.ler_arquivo()
def opção_5(nome_do_arquivo):
    caminho = path(PASTA)
    arquivo = Arquivo(caminho/nome_do_arquivo)
    arquivo.deletar_arquivo()  
def opção_6(nome_do_arquivo):
    caminho = path(PASTA1 )
    arquivo = VarreduraJSON(caminho/nome_do_arquivo)
    arquivo.varrerJson()
def opção_7(nome_do_arquivo):
    caminho = path(PASTA)
    arquivo_excel = ArquivoExcel(caminho/nome_do_arquivo)
    arquivo_excel.ler_arquivos_excel()    
opcao = {
    '1':opção_1,
    '2':opção_2,
    '3':opção_3,
    '4':opção_4,
    '5':opção_5,
    '6':opção_6,
    '7':opção_7
}
while True:
    print("\n---MENU DE OPÇÕES---")
    print('OPÇÃO 1 CRIAR ARQUIVO TXT')
    print('OPÇÃO 2 CRIAR ARQUIVO JSON')
    print('OPÇÃO 3 VARRER  ARQUIVOS')
    print('OPÇÃO 4 LER ARQUIVOS')
    print('OPÇÃO 5 DELETAR UM ARQUIVO')
    print('OPÇÃO 6 VARRER ARQUIVOS JSON')
    print('OPÇAO 7 LER ARQUIVOS EXCEL')
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
    
