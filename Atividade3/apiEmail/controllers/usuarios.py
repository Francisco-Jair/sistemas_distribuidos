from models.usuarioModel import inserirUsuario, recuperarUsuarioBD, recuperarUsuarioIDBD, recuperarUsuarioEmailBD


def recuperarTodosUsuario():
    """Recupera todos os usuarios"""
    data = {
    }

    dados = recuperarUsuarioBD()
    #print(dados[1].getNome())

    cont = 0
    for d in dados:
        pessoa = [dados[d].getId(), dados[d].getNome(), dados[d].getSobreNome(), dados[d].getEmail()]
        data[cont] = pessoa
        cont += 1
        #print(d)

    return data


def recuperarUsuarioID(id):
    """Recupera somente 1 usuario"""
    user = recuperarUsuarioIDBD(id)

    if user:
        pessoa = [user[f'{id}'].getId(), user[f'{id}'].getNome(), user[f'{id}'].getSobreNome(), user[f'{id}'].getEmail()]
    else:
        pessoa = []

    return pessoa


def recuperarUsuarioEmail(email):
    """Recupera somente 1 usuario"""
    user = recuperarUsuarioEmailBD(email)

    if user:
        pessoa = [user[f'{email}'].getId(), user[f'{email}'].getNome(), user[f'{email}'].getSobreNome(), user[f'{email}'].getEmail()]
    else:
        pessoa = []

    return pessoa


def criar_usuario(nome, sobrenome, email, senha):
    """Add um novo usuario"""

    if recuperarUsuarioEmail(email) == []:
        inserirUsuario(nome, sobrenome, email, senha)
        return 1
    else:
        return 0
        

