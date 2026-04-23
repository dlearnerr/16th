from http.server import SimpleHTTPRequestHandler, HTTPServer
PORT = 5020

class MyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(b"<h1>Hello from Docker Python Container</h1>")

server = HTTPServer(("0.0.0.0", PORT), MyHandler)
print(f"Server running on port {PORT}...")
server.serve_forever()



from http.server import *
class H(SimpleHTTPRequestHandler):
    def do_GET(s):
        s.send_response(200); s.end_headers()
        s.wfile.write(b"Hello from Docker")
HTTPServer(("",5020),H).serve_forever()
