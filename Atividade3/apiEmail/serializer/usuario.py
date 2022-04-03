class Usuario():

    def __init__(self, id, nome, sobrenome, email, senha):
        self.id = id
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha 

    def getId(self):
        return self.id

    def getNome(self):
        return f"{self.nome}"

    def getSobreNome(self):
        return f"{self.sobrenome}"

    def getEmail(self):
        return self.email