from pathlib import Path as path
class Arquivo:
    def __init__(self, nome_do_arquivo, conteudo_do_arquivo=''):
        self.nome_do_arquivo = nome_do_arquivo
        self.conteudo_do_arquivo = conteudo_do_arquivo
    
    def cria_arquivo(self):
        if path(self.nome_do_arquivo).exists():
            with open(self.nome_do_arquivo, 'w', encoding='utf-8') as arquivo_teste:
                arquivo_teste.write(self.conteudo_do_arquivo)
                print('arquvo criado com sucesso')
        else:
            print('o arquivo ja existe!!!')
    def ler_arquivo(self):
        with open(self.nome_do_arquivo, 'r', encoding='utf-8') as leitura:
            tela = leitura.read()
            print(tela) 
    
    def adicionar_arquivo(self):
        with open(self.nome_do_arquivo, 'a', encoding='utf-8') as adiciona:
            adiciona.write(self.conteudo_do_arquivo + '\n')  
            print('arquivo adicionado com sucesso')  

arquivo = Arquivo('TERÇA.TXT')
arquivo2 = Arquivo('teste.txt')
# arquivo.adicionar_arquivo()
arquivo.ler_arquivo()
arquivo2.ler_arquivo()

