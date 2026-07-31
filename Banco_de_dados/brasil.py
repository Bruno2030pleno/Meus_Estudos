from contextlib import closing
import sqlite3 as sql
dados_dos_estados = [["SÃO PAULO",104350]
,["CEARA",94349],["BAHIA",9458],
["MATO GROSSO", 934347],["SANTA CATARINA",96443],["RIO DE JANEIRO",432367],
["AMAZONAS",234567]]
with sql.connect('brasil.db') as conexão:
    conexão.row_factory = sql.Row
    with closing(conexão.cursor()) as cursor:
        cursor.execute("select * from estados")
        conexão.commit()
        dados = cursor.fetchall()
        for nomes in dados:
            print(f"estados {nomes['nome']} polução {nomes['população']}")