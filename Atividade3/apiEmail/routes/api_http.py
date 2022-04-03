import http.server
import json
from .list_routers import lista_rotas as rotas
from controllers import get, usuarios
#from urllib.parse import urlparse
#import socketserver
#PORT = 8000


class MyHandler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        #query = urlparse(self.path).query
        id = self.path.split('/')[-1]

        """
        content_length = int(self.headers['Content-Length'])

        
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = Nones
        """

        if self.path == rotas[1]:
            # /teste
            output_data = {'status': 'OK', 'result': get.testeGET()['version']}
        elif self.path == rotas[3]:
            # /usuario
            data = usuarios.recuperarTodosUsuario()
            output_data = {'status': 'OK', 'result': data}
        elif self.path == rotas[4].format(id):
            data = usuarios.recuperarUsuarioID(id)
            output_data = {'status': 'OK', 'result': data}


        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        output_json = json.dumps(output_data)
        
        self.wfile.write(output_json.encode('utf-8'))
    

    def do_POST(self):
        # - request -
        content_length = int(self.headers['Content-Length'])
        #print('content_length:', content_length)
        
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None


        if self.path == rotas[2]:
            #/criar_usuario
            code = usuarios.criar_usuario(input_data["nome"], input_data["sobrenome"], input_data["email"], input_data["senha"])
            msg = ""
            if code == 1:
                msg = "Usuário cadastrado com sucesso"
            elif code == 0:
                msg = "Usuário com e-mail Já cadastrado"

            output_data = {'status': 'OK', 'result': msg}
        

        # - response -
        
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        
        
        output_json = json.dumps(output_data)
        
        self.wfile.write(output_json.encode('utf-8'))
    

    def do_DELETE(self):
        content_length = int(self.headers['Content-Length'])
        #print('content_length:', content_length)
        
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None
            
        print(input_data)
        
        # - response -
        
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        
        output_data = {'status': 'OK', 'result': 'DELETE'}
        output_json = json.dumps(output_data)
        
        self.wfile.write(output_json.encode('utf-8'))
    

    def do_PUT(self):
        content_length = int(self.headers['Content-Length'])
        #print('content_length:', content_length)
        
        if content_length:
            input_json = self.rfile.read(content_length)
            input_data = json.loads(input_json)
        else:
            input_data = None
            
        print(input_data)
        
        # - response -
        
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        
        output_data = {'status': 'OK', 'result': 'PUT'}
        output_json = json.dumps(output_data)
        
        self.wfile.write(output_json.encode('utf-8'))


Handler = MyHandler

"""
try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Starting http://0.0.0.0:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("Stopping by Ctrl+C")
    httpd.server_close()  # to resolve problem `OSError: [Errno 98] Address already in use`
"""