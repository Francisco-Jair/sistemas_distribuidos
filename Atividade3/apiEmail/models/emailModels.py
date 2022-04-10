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
    cur.execute(f"""UPDATE emails SET lido = 1 WHERE id_email = {id};""")
    con.commit()

    cur.execute(f"""SELECT * FROM emails WHERE id_email = {id};""")
    return cur.fetchone()


def excluirEmail(id):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    cur.execute(f"""DELETE FROM emails WHERE id_email = {id};""")
    con.commit()
    cur.close()
    return True


def reponderEmail(id, resposta, destinatario, remetente):
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Atualizar
    cur.execute(f"""UPDATE emails SET corpo = '{resposta}' WHERE id_email = {id};""")
    con.commit()
    cur.execute(f"""UPDATE emails SET lido = 0 WHERE id_email = {id};""")
    con.commit()
    cur.execute(f"""UPDATE emails SET destinatario = '{destinatario}' WHERE id_email = {id};""")
    con.commit()
    cur.execute(f"""UPDATE emails SET usuario = '{remetente}' WHERE id_email = {id};""")
    con.commit()

    return 1


if __name__ == '__main__':
    pass