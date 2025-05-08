import http.server

def readFile(path):
    return open(path, 'rb').read().decode('utf-8', 'ignore')

def obtenirDocument(path):
    #print(path)
    return readFile('documents' + path)

def extension(path):
    point = path.rfind('.')
    return '' if point<0 else path[point:]
    
def mimeType(path):
    ext = extension(path)
    if ext == '.html': return 'text/html'
    if ext == '.css':  return 'text/css'
    if ext == '.js':   return 'text/javascript'
    if ext == '.py':   return 'text/python'
    if ext == '.svg':  return 'image/svg+xml'
    return 'text/plain'

class ServeurWeb(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        path = self.path

        if path == '/': path = '/index.html'

        if extension(path) in ['.ico', '.map']: return

        doc = obtenirDocument(path)

        self.send_response(200)
        self.send_header('Content-type', mimeType(path))
        self.end_headers()
        self.wfile.write(doc.encode('utf-8'))

    def log_message(self, format, *args):
        pass

http.server.HTTPServer(('', 8000), ServeurWeb).serve_forever()
