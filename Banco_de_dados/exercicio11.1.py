import sqlite3 as sql
from contextlib import closing
class Preço:
    def __init__(self):
        self.dados = [('manga','6.88'),('banana','5.78'),('leite', '4.50')]
        self.quatidade = [('quantidade', 100)]
    def criando_banco_de_dados(self):
        with sql.connect('preço.db') as preço:
            with closing(preço.cursor()) as cursor: # usando o closing para fechar o banco ?
               cursor.execute('create table quantidade(nome text, quantidade int)')
               cursor.executemany('insert into quantidade(nome, quantidade) values(?, ?)',(self.quatidade)) # varios inserts intos o execitemany
               preço.commit()
    def exibir_dados(self):
        with sql.connect('preço.db') as preço:
            with closing(preço.cursor()) as cursor: 
                cursor.execute('select * from preço')
                resultado = cursor.fetchall() # traz TODOS os registros de uma vez só, numa lista de tuplas
                for dados in resultado:
                    print(f"nome do produto {dados[0]}\npreço do produto {dados[1]}") 
    def exibir_quantidade(self):
            with sql.connect('preço.db') as preço:
                with closing(preço.cursor()) as cursor: 
                    cursor.execute('select * from quantidade')
                    resultado = cursor.fetchall() # traz TODOS os registros de uma vez só, numa lista de tuplas
                    for dados in resultado:
                        print(f"{dados[0]} {dados[1] - 1}")  
vendas = Preço()                 
# vendas.criando_banco_de_dados()
# vendas.exibir_dados()  
vendas.exibir_quantidade()                  
# se pergunta: "isso funcionou porque eu mudei o código,
#  ou porque eu limpei/resetei alguma coisa no ambiente?"
