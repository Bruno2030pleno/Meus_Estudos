import sqlite3 as sql
from contextlib import closing
lista_de_nomes = [['bruno nobre', 86996366604], ['miguel costa', 85996456678], ['lena nobre costa',85998764523]]
lista_endereço = [['rua regina de fatima', 100],['rua b', 50], ['rua z', 30]]
with sql.connect('agenda.db') as conexão:
        conexão.row_factory = sql.Row
        with closing(conexão.cursor()) as cursor:
                cursor.execute("create table lista_contato(id integer primary key autoincrement, nome_completo, numero_tel integer)")
                cursor.execute("create table lista_endereco(id integer primary key autoincrement, endereco, numero_casa integer)")
                cursor.executemany("insert into lista_contato(nome_completo, numero_tel)values(?,?)",lista_de_nomes)
                cursor.executemany("insert into lista_endereco(endereco, numero_casa)values(?,?)",lista_endereço)
                conexão.commit()
        for nome in conexão.execute("select * from lista_contato"):
                print(f"nome {nome['nome_completo']}\ntelefone {nome['numero_tel']}")