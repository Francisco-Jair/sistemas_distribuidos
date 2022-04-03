import argparse
import socketserver
from routes.api_http import Handler as apiRouter


parser = argparse.ArgumentParser(description = "switch port")
parser.add_argument("-p", required=False, default=8000) # Pode escolher a porta

def getArgs():
    args = parser.parse_args()
    return int(args.p)


if __name__ == '__main__':
    PORT = getArgs()

    
    try:
        with socketserver.TCPServer(("", PORT), apiRouter) as httpd:
            print(f"Starting http://0.0.0.0:{PORT}")
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("Stopping by Ctrl+C")
        httpd.server_close()  # to resolve problem `OSError: [Errno 98] Address already in use`
    