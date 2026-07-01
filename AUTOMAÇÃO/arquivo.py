from pathlib import Path as path
import json
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
        
        self.dicionario = {
            'nome': 'bruno',
            'endereço': 'rua regina de fatima',
            'bairro': 'parrasé', 'cep': '45677-788', 'numero': 34}
    
    def criar_arquivoJosn(self):
        if path(self.nome_do_arquivo).exists():
           print('o arquivo ja existe!!')    
        else:
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

arquivo = Arquivo('miguel.Json','miguel e bom de assistir tv')
jsonn = ArquivoJSON('endereço_em_dicionario') 
jsonn.criar_arquivoJosn() 