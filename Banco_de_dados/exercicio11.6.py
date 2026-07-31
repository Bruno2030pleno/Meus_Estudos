from contextlib import closing
import sqlite3 as sql
class BancodeDados:
    def __init__(self):
        pass
    def adicionar_dados(self,preço_novo,nome_produto):
        with sql.connect('preço.db') as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute("update preço set preço_produto = ?  where nome_produto = ?",(preço_novo,nome_produto),)
                cursor.execute('select * from preço')
                conexão.commit()
                resultado = cursor.fetchall()
                print('--------------------')
                for nome in resultado:
                    print(f'nome do produto: {nome[0]}\n preço do produto R$ {nome[1]}')
a = BancodeDados()
while True:
    preço = input("qual o novo preço do produto ?: ")
    nome1 = input('nome do produto ?: ')
    if nome1 == '':
        break
    a.adicionar_dados(preço, nome1)
