from pathlib import Path as path
import json
PASTA = "/home/brunodev/arquivos_Json/"
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
           path(self.nome_do_arquivo).unlink() # aprendi hoje, 01/07/2026
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
    
    def exir_arquivoJson(self):
        if path(self.nome_do_arquivo).exists():
            with open(self.nome_do_arquivo, 'r', encoding='utf-8') as leituras:
                leitura = json.load(leituras) 
                print(leitura)
        else:
            print('o arquivo para leitura não existe!!')
    
    def adicionar_dados(self):
        while True:
            print('para sair aperte enter')
            chave = input('digite a chave: ')
            if chave.lower() == '':
                break
            valor = input('digite o valor')
            self.dicionario[chave] = valor

class VarreduraJSON:
    def __init__(self, caminho):
        self.caminho =  caminho
    
    def varrerJson(self):
        pasta = path(self.caminho) 
        for arquivo in pasta.glob('*.json'): 
            print(arquivo)
            with open(arquivo, 'r', encoding='utf-8') as arquivo:
                leitura = json.load(arquivo)
                print('=============================================')
                print(json.dumps(leitura,  indent=2, ensure_ascii=False))
                print('=============================================')
# CRIANDO O MENU DE OPÇÕES
while True:
    print("---MENU DE OPÇÕES---")
    print('OPÇÃO  1 CRIAR ARQUIVO TXT')
    print('OPÇÃO  2 CRIAR ARQUIVO JSON')
    print('VARRER 3 ARQUIVOS')
    Usuario = input("Dentre as opções, qual você deseja? / ou Enter para sair ")
    if Usuario == '':
        print('sessão finalizada')
        break
    if Usuario == '1':
       nome_do_arquivo = input('qual vai ser o nome do arquivo? ')
       conteudo = input('agora me fala o conteudo? ')
       
       caminho = path(PASTA)
       
       arquivo = Arquivo(caminho/nome_do_arquivo, conteudo)
       arquivo.cria_arquivo()
       print('arquivo txt criado com sucesso')
    
    elif Usuario == '2':
        jsonn0 = ArquivoJSON(PASTA)
        jsonn0.criar_arquivoJson()
        print('arquivo json criado com sucesso')
    elif Usuario == '3':
        varrer = VarreduraJSON(PASTA)
        varrer.varrerJson()
        print('arquivos varridos com sucesso')
    else:
        print('Opção invalida!!')
# jsonn0 = ArquivoJSON('/home/brunodev/arquivos_Json/nome0.json')
# jsonn1 = ArquivoJSON('/home/brunodev/arquivos_Json/nome1.json')
# jsonn2 = ArquivoJSON('/home/brunodev/arquivos_Json/nome2.json')

# jsonn0.adicionar_dados()
# jsonn0.criar_arquivoJson()

# jsonn1.adicionar_dados()
# jsonn1.criar_arquivoJson()

# jsonn2.adicionar_dados()
# jsonn2.criar_arquivoJson()

# varrer = VarreduraJSON('/home/brunodev/arquivos_Json') 
# varrer.varrerJson()
