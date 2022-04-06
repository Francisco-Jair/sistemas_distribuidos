import os.path
import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "dados.db")


def enviar_emailBD(destinatario, assunto, corpo, remetente):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(f"""INSERT INTO emails (destinatario, assunto, corpo, usuario) VALUES ('{destinatario}', '{assunto}', '{corpo}', '{remetente}')""")
    con.commit()
    cur.close()


def caixaDeEntrada(email):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(f"""SELECT * FROM emails WHERE destinatario = '{email}';""")
    return cur.fetchall()


def caixaDeSaida(email):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(f"""SELECT * FROM emails WHERE usuario = '{email}';""")
    return cur.fetchall()


def lerEmail(id):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Atualizar
    cur.execute(f"""UPDATE FROM emails SET lido = 1 WHERE id_email = {id};""")
    con.commit()

    cur.execute(f"""SELECT * FROM emails WHERE id_email = {id};""")
    return cur.fetchone()


def excluirEmail(id):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(f"""DELETE * FROM emails WHERE id_email = {id};""")
    con.commit()
    cur.close()
    return True


if __name__ == '__main__':
    pass