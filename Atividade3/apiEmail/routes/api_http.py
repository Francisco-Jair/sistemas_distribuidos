import http.server
import json
from .list_routers import lista_rotas as rotas
from controllers import emailController, get, usuariosController

loginEmail = None


class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):

        id = self.path.split('/')[-1]

        if self.path == rotas[1]:
            # /teste
            print(self.__class__.loginEmail)
            output_data = {'status': 'OK', 'result': get.testeGET()['version']}
        elif self.path == rotas[3]:
            # /usuario
            data = usuariosController.recuperarTodosUsuario()
            output_data = {'status': 'OK', 'result': data}
        elif self.path == rotas[4].format(id):
            # /usuario/id
            data = usuariosController.recuperarUsuarioID(id)
            output_data = {'status': 'OK', 'result': data}
        else:
            output_data = {'status': 'OK', 'result': "Faça login para pode acessar a rota"}


        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        output_json = json.dumps(output_data)
        
        self.wfile.write(output_json.encode('utf-8'))
    

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None


        if self.path == rotas[2]:
            #/criar_usuario
            code = usuariosController.criar_usuario(input_data["nome"], input_data["sobrenome"], input_data["email"], input_data["senha"])
            msg = ""
            if code == 1:
                msg = "Usuário cadastrado com sucesso"
            elif code == 0:
                msg = "Usuário com e-mail Já cadastrado"

            output_data = {'status': 'OK', 'result': msg}
        elif self.path == rotas[5]:
            # /enviar_email
            code = emailController.enviarEmail(input_data, self.__class__.loginEmail)
            output_data = {'status': 'OK', 'result': "E-mail Enviado"}
        elif self.path == rotas[6]:
            # /login
            if get.login(input_data["login"]):
                msg = "Login realizado com sucesso"
                self.__class__.loginEmail = input_data["login"]
            else:
                msg = "Usuarios já logado"

            output_data = {'status': 'OK', 'result': msg}
        else:
            output_data = {'status': 'OK', 'result': "Faça login para pode acessar a rota"}
        
        
        # - response -
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        
        output_json = json.dumps(output_data)
        self.wfile.write(output_json.encode('utf-8'))
    

    def do_DELETE(self):
        id = self.path.split('/')[-1]

        content_length = int(self.headers['Content-Length'])
        #print('content_length:', content_length)
        
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None
            
        #print(input_data)
        
        # - response -
        
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        
        output_data = {'status': 'OK', 'result': 'DELETE'}
        output_json = json.dumps(output_data)
        
        self.wfile.write(output_json.encode('utf-8'))
    

    def do_PUT(self):
        id = self.path.split('/')[-1]
        content_length = int(self.headers['Content-Length'])
        #print('content_length:', content_length)
        
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None
            
        #print(input_data)
        
        # - response -
        
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        
        output_data = {'status': 'OK', 'result': 'PUT'}
        output_json = json.dumps(output_data)
        
        self.wfile.write(output_json.encode('utf-8'))


Handler = MyHandler

