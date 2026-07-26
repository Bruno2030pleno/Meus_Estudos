import sqlite3 as sql
from contextlib import closing
with sql.connect('agenda.db') as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute('select * from agenda')
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                break
            print(f'NOME: {resultado[0]}\ntelefone {resultado[1]}')