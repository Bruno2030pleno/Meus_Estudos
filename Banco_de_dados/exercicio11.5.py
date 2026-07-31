from contextlib import closing
import sqlite3 as sql
with sql.connect('preço.db') as agenda:
    with closing(agenda.cursor()) as cursor:
        cursor.execute("update preço set preço_produto = '7.98' where nome_produto  = 'manga'")
        cursor.execute("update preço set preço_produto = '6.98' where nome_produto  = 'banana'")
        cursor.execute("update preço set preço_produto = '4.98' where nome_produto  = 'leite'")
        cursor.execute("select * from preço")
        agenda.commit()
        resultado = cursor.fetchall()
        for nomes in resultado:
            print(f"nome do produto: {nomes[0]}\npreço {nomes[1]}")