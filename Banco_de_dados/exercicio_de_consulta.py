from contextlib import closing
import sqlite3 as sql
class Cunsulta_no_banco_de_dados:
    def __init__(self, nome,algo ):
        self.nome = nome
        self.algo =  algo
    def consultar_dados(self):
        with sql.connect('preço.db') as preço:
            with closing(preço.cursor()) as cursor:
                cursor.execute('select * from preço where nome =?',(self.nome,))
                resultado = cursor.fetchall()
                for nome in resultado:
                    print(f"nome {nome[0]}\npreço {nome[1]}") 

    def peerguntar_dois_valores(self):
            with sql.connect('preço.db') as preço:
                with closing(preço.cursor()) as cursor:
                    cursor.execute('select * from preço where preço_produto >= ? and preço_produto <= ?',(self.nome,self.algo))
                    resultado = cursor.fetchall()
                    for nome in resultado:
                        print(f"preço R$ {nome[1]}")
                        print(f'nome {nome[0]}')                                                  
while True:
    nome = input("nome para a consulta 0: ?")
    algo = input("nome para a consulta 1: ?")
    a = Cunsulta_no_banco_de_dados(nome, algo)
    if nome == '':
        break
    a.peerguntar_dois_valores()
 
