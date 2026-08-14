from collections import UserList
from agendanilo import *
from pathlib import Path as path
import os
import sqlite3 as sql 

class DBListaUnica(ListaÚnica):
    def __init__(self, elem_classe):
        super().__init__(elem_classe)            
        self.apagados = []
    def remove(self, elem):
        if elem.id is not None:
           self.apagados.append(elem.id) 
        super().remove(elem)
    def limpa(self):
        self.apagados = []

class DBNome(Nome):
    def __init__(self, nome, id_=None):
        super().__init__(nome)
        self.id = id_ 

class DBTipoTelefone(TipoTelefone):
    def __init__(self, id_,tipo):
        super().__init__(tipo)
        self.id = id_

class DBTelefone(Telefone):
    def __init__(self, número, tipo=None, id_=None, id_nome=None):
        super().__init__(número, tipo)
        self.id = id_
        self.id_nome = id_nome

class DBTelefones(DBListaUnica):
    def __init__(self):
        super().__init__(DBTelefone)

class DBTiposTelefone(ListaÚnica):
    def __init__(self):
        super().__init__(DBTipoTelefone)

class DBDadoAgenda:
    def __init__(self, nome):
        self.nome = nome
        self.telefone = DBTelefones()
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, DBNome):
           raise TypeError("o nome deve ser uma instancia da classe DBnome")
        self._nome = valor
    def pesquisaTelefone(self, telefone):
        posição = self.telefone.pesquisa(DBTelefone(telefone))
        if posição == -1:
           return None
        else:
            return self.telefone[posição]  

BANCO = "create table tipos(id integer primary key autoincrement, descrição text);" \
"create table nomes(id integer primary key autoincrement, nome text);" \
"create table telefones(id integer primary key autoincrement,id_nome, numero text, id_tipo integer);" \
"insert into tipos(descrição) values ('celular');" \
"insert into tipos(descrição) values ('fixo');" \
"insert into tipos(descrição) values ('fax');" \
"insert into tipos(descrição) values ('trabalho');"

class DBAgenda:
    def __init__(self, banco):
        self.tiposTelefone = DBTiposTelefone()
        self.banco =  banco
        novo = not os.path.isfile(banco)
        self.conexao = sql.connect(banco)
        self.conexao.row_factory = sql.Row
        if novo:
            self.cria_banco()
        self.carregaTipos()
    def carregaTipos(self):
        for tipo in self.conexao.execute("select * from tipos"):
            id_ = tipo['id']
            descrição = tipo['descrição']
            self.tiposTelefone.adiciona(DBTipoTelefone(id_, descrição))
    def cria_banco(self):
        self.conexao.executescript(BANCO)
    def pesquisaNome(self, nome):
        if not isinstance(nome, DBNome): 
           raise TypeError("nome deve ser do tipo DBNome")
        achado = self.conexao.execute("select count(*) from nomes where nome = ?",(nome.nome,)).fetchone()
        if achado[0] > 0:
            return self.carrega_por_nome(nome)
        else:
            return None
    def carrega_por_nome(self, id):
        consulta = self.conexao.execute("select * from nomes where id = ?",(id,))
        return self.carrega(consulta.fetchone())
    def carrega(self, consulta):
        if consulta is None:
            return None
        novo = DBDadoAgenda(DBNome(consulta['nome'], consulta['id']))
        for telefone in self.conexao.execute("select * from telefones where id_nome = ?",(novo.nome.id,)): 
            ntel = DBTelefone(telefone['numero'], None, telefone['id'], telefone['id_nome'])
            for tipo in self.tiposTelefone:
                if tipo.id == telefone['id_tipo']:
                   ntel.tipo = tipo
                   break
            novo.telefones.adiciona(ntel)
        return novo
    def lista(self):
        consulta = self.conexao.execute("select * from nomes order by nome")
        for resgistro in consulta:
            yield self.carrega(resgistro)        
    def novo(self, registro):
        try:
            cur = self.conexao.cursor()
            cur.execute("insert into nomes(nome) values(?)",(str(registro),))
            registro.nome.id = cur.lastrowid
            for telefone in registro.telefones:
                cur.execute("insert into telefones(numero, id_tipo, id_nome)values(?,?,?)",(telefone.numero, telefone.tipo.id,registro.nome.id))
                telefone.id = cur.lastrowid
            self.conexao.commit()
        except Exception:
            self.conexao.rollback()
            raise
        finally:
            cur.close()
    def atualiza(self, resgistro):
        try:
            cur = self.conexao.cursor()
            cur.execute("update nomes set nome=? where id = ?",(str(resgistro.nome), resgistro.nome.id))
            for telefone in resgistro.telefones:
                if telefone.id is None:
                    cur.execute("insert into telefones(numero, id_tipo, id_nome)values(?,?,?)",(telefone.numero, telefone.tipo.id, resgistro.nome.id)) 
                    telefone.id = cur.lastrowid
                else:
                    cur.execute("update telefones set numero=?,id_tipo=?, id_nome=? where id = ?",(telefone.numero, telefone.tipo.id, resgistro.nome.id, telefone.id))
            for apagado in resgistro.telefones.apagados:
                cur.execute("delete from telefones where id = ?", (apagado))
            self.conexao.commit()
        except Exception:
            self.conexao.rollback()
            raise
        finally:
            cur.close()
    def apaga(self, registro):
        try:
            cur = self.conexao.cursor()
            cur.execute("delete from telefones where id_nome = ?", (registro.nome.id))
            self.conexao.commit()
        except Exception:
            self.conexao.rollback()
            raise
        finally:
            cur.close()                                                   
      
        