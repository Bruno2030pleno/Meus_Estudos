from contextlib import closing
import sqlite3 as sql
with sql.connect('brasil.db') as conexão:
    conexão.row_factory = sql.Row
    print(f"{'id':3s} {'estados':<20s} {'população':12s}")
    print("-"*50)
    for estado in conexão.execute("select * from estados order by população desc"):
        print(f"{estado['id']:3d} {estado['nome']:<20s} {estado['população']:12d}")