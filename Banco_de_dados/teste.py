from contextlib import closing
import sqlite3 as sql
with sql.connect('agenda.db') as agenda:
    with closing(agenda.cursor()) as cursor:
        cursor.execute("update agenda set telefone = '000-0000' where nome  = 'bruno'")
        cursor.execute("select * from agenda")
        agenda.commit()
        resultado = cursor.fetchall()
        for nomes in resultado:
            print(f"nome: {nomes[0]}\ntelefone {nomes[1]}")
        
        
    