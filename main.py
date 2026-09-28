import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

resposta = client.responses.create(
    model="gpt-5.6-mini",
    input="Responda apenas: Daniel AI conectado com sucesso."
)

print(resposta.output_text)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(resposta.output_text.encode())

    def log_message(self, format, *args):
        return

PORT = int(os.environ.get("PORT", 10000))
server = HTTPServer(("0.0.0.0", PORT), Handler)

server.serve_forever()
