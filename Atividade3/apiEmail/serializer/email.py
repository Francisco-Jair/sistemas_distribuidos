class Email():

    def __init__(self, id, destinatario, assunto, corpo, remetente, status=0):
        self.id = id
        self.destinatario = destinatario
        self.remetente = remetente
        self.assunto = assunto
        self.corpo = corpo
        self.status = status # 0 - nao lido, 1 - Lido
    

    def getId(self):
        return self.id


    def getDestinatario(self):
        return self.destinatario


    def getAssunto(self):
        return self.assunto


    def getCorpo(self):
        return self.corpo


    def getRemetente(self):
        return self.remetente


    def getStatus(self):
        return self.status

    