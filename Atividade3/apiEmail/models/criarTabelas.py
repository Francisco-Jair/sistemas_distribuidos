import os.path
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "dados.db")


def criarBanco():
    con = sqlite3.connect(db_path)
    #con.close()


def criarTabelasUsuario():
    con = sqlite3.connect(db_path)    
    cur = con.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS usuarios (id integer primary key autoincrement not null , nome text, sobrenome text, email text, senha text)''')
    #con.close()


def criarTabelasEmail():
    con = sqlite3.connect(db_path)    
    cur = con.cursor()
    cur.execute('''    
    CREATE TABLE IF NOT EXISTS emails (id_email integer primary key autoincrement not null , destinatario text, assunto text, corpo text, lido integer, usuario text not null)
    ''')
    con.close()
    

if __name__ == '__main__':
    criarBanco()
    criarTabelasUsuario()
    criarTabelasEmail()
    #con.close()