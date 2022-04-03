import os.path
import sqlite3

from .usuarioModel import criarTabelasUsuario


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "dados.db")


if __name__ == '__main__':
    criarTabelasUsuario()