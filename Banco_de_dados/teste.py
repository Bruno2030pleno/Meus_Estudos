from contextlib import closing
import sqlite3 as sql
with sql.connect('agenda.db') as agenda:
    with closing(agenda.cursor()) as cursor:
        cursor.execute("select * from agenda where nome = 'lena'")
        resultado = cursor.fetchall()
        for nomes in resultado:
            print(f"nome: {nomes[0]}\nphone: {nomes[1]}")