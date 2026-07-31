import sqlite3 as sql
from contextlib import closing
class Preço:
    def __init__(self):
        self.dados = [('manga',6.88),('banana',5.78),('leite', 4.50)]
        
    def criando_banco_de_dados(self):
        with sql.connect('preço.db') as preço:
            with closing(preço.cursor()) as cursor: # usando o closing para fechar o banco ?
               cursor.execute('create table preço(nome_produto text, preço_produto REAL)')
               cursor.executemany('insert into preço(nome_produto, preço_produto) values(?,?)',(self.dados)) # varios inserts intos o execitemany
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
                        print(f"{dados[0]} {dados[1] }") 
                    
vendas = Preço()                 
# vendas.criando_banco_de_dados()
# vendas.criando_banco_de_dados()  
vendas.exibir_dados()
# vendas.exibir_quantidade()                  
# se pergunta: "isso funcionou porque eu mudei o código,
#  ou porque eu limpei/resetei alguma coisa no ambiente?"
