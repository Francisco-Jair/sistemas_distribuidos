#import os.path
import sqlite3
from serializer import usuario
from .mainModels import db_path

#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#db_path = os.path.join(BASE_DIR, "dados.db")

def criarBanco():
    #print(BASE_DIR)
    con = sqlite3.connect(db_path)
    con.close()


def criarTabelasUsuario():
    con = sqlite3.connect(db_path)    
    cur = con.cursor()
    cur.execute('''CREATE TABLE usuarios (id integer primary key autoincrement not null , nome text, sobrenome text, email text, senha text)''')
    con.close()


def inserirUsuario(nome, sobrenome, email, senha):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(f"""INSERT INTO usuarios (nome, sobrenome, email, senha) VALUES ('{nome}', '{sobrenome}', '{email}', '{senha}')""")
    con.commit()
    cur.close()


def recuperarUsuarioBD():
    users = {}

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    cur.execute("""SELECT * FROM usuarios;""")
    for linha in cur.fetchall():
        user = usuario.Usuario(linha[0], linha[1], linha[2], linha[3], linha[4])
        users[linha[0]] = user

    cur.close()
    return users


def recuperarUsuarioIDBD(id):
    users = {}

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    info = cur.execute(f"""SELECT * FROM usuarios WHERE id = {id} """).fetchall()

    if info:
        info = info[0]
        users[id] = usuario.Usuario(info[0], info[1], info[2], info[3], info[4])
    

    cur.close()
    return users


def recuperarUsuarioEmailBD(email):
    users = {}

    con = sqlite3.connect(db_path)
    cur = con.cursor()
    
    info = cur.execute(f"""SELECT * FROM usuarios WHERE email = '{email}' """).fetchall()

    if info:
        info = info[0]
        users[email] = usuario.Usuario(info[0], info[1], info[2], info[3], info[4])
    
    cur.close()
    return users



if __name__ == '__main__':
    pass
    #criarBanco()
    #criarTabelas()