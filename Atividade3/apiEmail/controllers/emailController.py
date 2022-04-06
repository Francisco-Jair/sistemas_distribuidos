from models.emailModels import enviar_emailBD


def enviarEmail(data, remetente):
    print(remetente)
    enviar_emailBD(data["destinatario"], data["assunto"], data["corpo"], remetente)
    return 1