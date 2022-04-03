class Email():

    def __init__(self, destinatario, remetente, assunto, corpo):
        self.destinatario = destinatario
        self.remetente = remetente
        self.assunto = assunto
        self.corpo = corpo
        self.status = 0 # 0 - nao lido, 1 - Lido