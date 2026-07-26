import sqlite3 as sql # 1 
conexao = sql.connect('agenda.db') # 2
cursor = conexao.cursor() # 3
cursor.execute('select * from agenda') # 4
resultado = cursor.fetchall() # 5

for resgistro in resultado:
    print(f"nome: {resgistro[0]}\ntelefone {resgistro[1]}")
cursor.close() # 6
conexao.close() # 7   