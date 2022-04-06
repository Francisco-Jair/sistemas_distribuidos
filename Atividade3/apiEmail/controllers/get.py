

listaLogin = []

def testeGET():
    return {"version": "1.0.0"}


def login(email):

    if email not in listaLogin:
        listaLogin.append(email)
        return True
    else:
        return False
    

def logout(email):
    listaLogin.remove(email)