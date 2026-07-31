from contextlib import closing
import sqlite3 as sql
nome = input("nome a selecionar: ")
with sql.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("select * from agenda where nome = ?", (nome,))
        x = 0
        while True:
            resultado = cursor.fetchone()
            if resultado is None:
                if x == 0:
                    print('nada encontrado')
                break
            print(f"nome: {resultado[0]}\ntelefone {resultado[1]}")
            x += 1

