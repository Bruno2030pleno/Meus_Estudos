from contextlib import closing
import sqlite3 as sql
def listar_preços_da_tabela():
    with sql.connect('preço.db') as preço:
        with closing(preço.cursor()) as cursor:
            cursor.execute('select preço from preço')
            resultado = cursor.fetchall()
            for valores in resultado:
                print(f"valores R$ {valores[0]}")
listar_preços_da_tabela()                