from contextlib import closing
import sqlite3 as sql
class ApagaDados:
    def __init__(self):
        pass
    def delete_dados(self):
        with sql.connect('agenda.db') as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute("delete from agenda where nome = 'miguel'")
                print("registro apagados:", cursor.rowcount)
                if cursor.rowcount == 1:
                    conexão.commit()
                    print("registros gravados")
                else:
                    conexão.rollback()
                    print("alterações abortadas")    
cliente = ApagaDados()
cliente.delete_dados()                    