from contextlib import closing
import sqlite3 as sql
with sql.connect('agenda.db') as agenda:
    with closing(agenda.cursor()) as cursor:
        cursor.execute("update agenda set telefone = '000-0030' where nome  = 'lena'")
        cursor.execute("select * from agenda")
        print('registros alterados: ',cursor.rowcount)
        print('-------------------------------------')
        if cursor.rowcount == -1:
            agenda.commit()
            print('alterações feitas no banco de dados com sucesso')
        else:
            agenda.rollback()
            print('alterações abortadas')    