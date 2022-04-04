from models.emailModels import enviar_emailBD


def enviarEmail(destinatario, assunto, corpo):
    enviar_emailBD(destinatario, assunto, corpo)
    return 1