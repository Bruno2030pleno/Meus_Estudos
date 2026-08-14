import sqlite3 as sql
import datetime 

hoje = datetime.date.today()
hoje60dias = hoje + datetime.timedelta(days=60)
with sql.connect('brasil.db',detect_types=sql.PARSE_DECLTYPES) as conexão:
        conexão.row_factory = sql.Row
        for feriado in conexão.execute("select * from feriados"):
            print(f"{feriado['descricao']} {feriado['data'].strftime('%d/%m')}")

        
        
    