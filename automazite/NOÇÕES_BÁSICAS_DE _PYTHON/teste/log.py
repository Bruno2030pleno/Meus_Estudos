import logging     
from pathlib import Path as path
import json
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s -  %(message)s')
class Arquivo:
    def __init__(self, nome_arquivo, conteudo):
        self.nome_arquivo = nome_arquivo
        self.conteudo = conteudo
    def cria_arquivo_TXT(self):
        if path(self.nome_arquivo).exists():
            logging.info("o arquivo ja existe")

        else:
            with open(self.nome_arquivo, 'w', encoding='utf-8') as arquivo:
               arquivo.write(self.conteudo)
              
    def ler_arquivoJSON(self):
        if path(self.nome_arquivo).exists():
            with open(self.nome_arquivo, 'r', encoding='utf-8') as jsonx:
               leitura = json.load(jsonx)
               logging.info("Leitura efetivada com sucesso")
               print(json.dumps(leitura,  indent=2, ensure_ascii=False))
        else:
              logging.warning("algo inesperado: a leitura falhou, o arquivo não existe!!:")     
               
    def cria_arquivo_json(self):
        if path(self.nome_arquivo).exists():
            logging.info("o arquivo ja existe")

        else:
            with open(self.nome_arquivo, 'w', encoding='utf-8') as arquivojson:
                json.dump(self.conteudo, arquivojson)
                print('arquivo criado')  
         
arquivo = Arquivo('jsodn.json', 'bruno') 
txt = Arquivo('NOME.txt', 'BRdUNO')
txt.cria_arquivo_TXT()  
arquivo.ler_arquivoJSON()
 