import sqlite3 as sql
conexao = sql.connect('agenda.db')
cursor = conexao.cursor()
cursor.execute('select * from agenda')
while True:
    resultado = cursor.fetchone() # 1
    if resultado is None:
        break
    print(f"nome {resultado[0]}\ntelefone {resultado[1]}")
cursor.close()
conexao.close()    