from pathlib import Path as path
import openpyxl
import json
from config import PASTA
import csv 

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
            print('erro de encoding ') 
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

    def deletar_arquivo(self):
        if path(self.nome_do_arquivo).exists():
           path(self.nome_do_arquivo).unlink() # remove O ARQUIVO
           print('arquivo removido')
        else:
            print('arquivo nao existe!!')

class ArquivoJSON(Arquivo):
    def __init__(self, nome_do_arquivo, conteudo_do_arquivo=''):
        super().__init__(nome_do_arquivo, conteudo_do_arquivo)
        self.dicionario = {}
    def criar_arquivoJson(self):
        if path(self.nome_do_arquivo).exists():
           print('o arquivo ja existe!!')    
        else:                                    
            path(PASTA).mkdir(parents=True, exist_ok=True)
            with open(self.nome_do_arquivo, 'w', encoding='utf-8') as arquivo:
                json.dump(self.dicionario, arquivo)
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
                    print('-'*40)
                    print(json.dumps(leitura,  indent=2, ensure_ascii=False))
                    print('-'*40)
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
            planilha = workbook.active
            for linha in planilha.iter_rows(values_only=True):
                try:
                    fase, etapa, o_que_aprender, status, prioridade, observacao = linha
                    if fase == 'FASE' or etapa == 'ETAPA' or fase is None or etapa is None:
                        continue
                    print(fase, etapa, o_que_aprender, status, prioridade, observacao) 
                    self.dados.append(linha) 
                except ValueError:
                    print(f'linha com formato inesperado, pulando: {linha}')
                    continue  
        except FileNotFoundError:
            print(f'arquivo não encontrado {self.nome_do_arquivo} ') 


class ArquivoCsv(Arquivo):
    def __init__(self, nome_do_arquivo, conteudo_do_arquivo=''):
       super().__init__(nome_do_arquivo, conteudo_do_arquivo)
       self.lista = []
    def ler_arquivo_csv(self):
        try:
            with open(self.nome_do_arquivo,'r', encoding='latin-1')  as arquivocsv:
                        leitura = csv.reader(arquivocsv)
                        for dados in leitura:
                            self.lista.append(dados)
                        return self.lista                                           
        except UnicodeError:
            print('Erro de unicode!!')
            try:
                with open(self.nome_do_arquivo,'r', encoding='utf-8')  as arquivocsv:
                    leitura = csv.reader(arquivocsv)
                    for dados in leitura:
                        self.lista.append(dados)
                    return self.lista    
            except FileNotFoundError:
                print('erro arquivo nao encontrado')             