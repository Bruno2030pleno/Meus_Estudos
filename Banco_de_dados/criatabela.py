import sqlite3 as sql
# conexao = sql.connect('agenda.db') # nome do banco
# cursor = conexao.cursor() # cursor e um objeto que usamos para enviar e receber resultados de bancos de dados
# cursor.execute('''create table agenda (nome text, telefone text)''')
# cursor.execute('''insert into agenda (nome, telefone) values(?, ?)''',('bruno', '9637-6666'))
# conexao.commit()
# cursor.close()
# conexao.close()
dados = [('bruno','9748'),('lena','9475'),('miguel', '98475')]
conexao = sql.connect('agenda.db')
cursor = conexao.cursor()
cursor.executemany('insert into agenda (nome, telefone) values(?, ?)',dados)
cursor.execute('select * from agenda')
conexao.commit()
resultado = cursor.fetchall()
print(resultado)
conexao.close()
