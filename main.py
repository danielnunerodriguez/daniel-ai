import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", 10000))

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Daniel AI funcionando!")

    def log_message(self, format, *args):
        return

server = HTTPServer(("0.0.0.0", PORT), Handler)

print(f"Daniel AI funcionando na porta {PORT}")

server.serve_forever()
