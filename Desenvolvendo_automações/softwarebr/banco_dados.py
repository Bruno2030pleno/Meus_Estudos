import sqlite3 as sql
from contextlib import closing
from datetime import datetime
from config import BANCO

class BancoDeDadosSqlite:
    def __init__(self):
        self.dados = []
    def criando_banco_de_dados(self):
        with sql.connect(BANCO) as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute("""
                    create table if not exists arquivos(
                        id integer primary key autoincrement,
                        acao text,
                        nome_arquivo text,
                        tipo_arquivo text,
                        data_hora text,
                        nome_do_banco text
                    )
                """)
    def salvar_dados(self, acao, nome_arquivo, tipo_arquivo, nome_do_banco):
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with sql.connect(nome_do_banco) as conexão:
            with closing(conexão.cursor()) as cursor:
                cursor.execute(
                    "insert into arquivos(acao, nome_arquivo, tipo_arquivo, data_hora) values (?, ?, ?, ?)",
                    (acao, nome_arquivo, tipo_arquivo, data_hora)
                )
                conexão.commit()
    def exibir_dados_do_banco(self):
        with sql.connect(BANCO) as conexão:
            conexão.row_factory = sql.Row
            with closing(conexão.cursor()) as cursor:
                resultado = cursor.execute("select * from arquivos")
                for dados in resultado.fetchall():
                    self.dados.append(dados)
                    print("-"*50)
                    print(f"ID {dados['id']} -- ação {dados['acao']} -- nome do arquivo {dados['nome_arquivo']}")