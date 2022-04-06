from models.emailModels import enviar_emailBD, lerEmail, caixaDeEntrada, excluirEmail


def enviarEmail(data, remetente):
    enviar_emailBD(data["destinatario"], data["assunto"], data["corpo"], remetente)
    return 1


def abrirEmail(id):
    mail = lerEmail(id)
    print(mail)
    return mail


def todosEmails(email):
    mail = caixaDeEntrada(email)
    return mail


def removerEmail(id):
    data = excluirEmail(id)
    return data