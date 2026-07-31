from contextlib import closing
import sqlite3 as sql
with sql.connect('preço.db') as conexão:
    conexão.row_factory = sql.Row # ← Ativa "modo dicionário"
    with closing(conexão.cursor()) as cursor:
        for registros in cursor.execute("select * from preço"):
            print(f"nome do produto {registros['nome_produto']}\npreço {registros['preço_produto']}")