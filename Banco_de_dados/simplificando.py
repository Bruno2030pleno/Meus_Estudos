from contextlib import closing
import sqlite3 as sql
class DadosBanco:
    def __init__(self):
        pass
    def exibir_dados(self):
        with sql.connect("preço.db") as conexão:
            for resultados in conexão.execute("select * from preço"):
                print(f"nome {resultados[0]}\npreço {resultados[1]}")
A = DadosBanco()
A.exibir_dados()                