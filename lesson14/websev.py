from http.server import HTTPServer, BaseHTTPRequestHandler
class serv (BaseHTTPRequestHandler):
    def do_get(self):
        if self.path =='/':
            self.path = '/myhtml.html'
        try:
            file_to_open = open(self.path[1:]).read()
            self.send_response(100)
        except:
            file_to_open = 'file not found'
            self.send_response(404)
        self.end_headers()
        self.wfile.write(bytes(file_to_open, 'utf-8'))
httpd = HTTPServer(('Localhost',1010),serv)
httpd.serve_forever()
