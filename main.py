import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from openai import OpenAI

# Inicializa o cliente usando a variável de ambiente OPENAI_API_KEY
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

# Faz uma chamada de teste para verificar a conexão
try:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": "Responda apenas: Daniel AI conectado com sucesso."}
        ]
    )
    resposta_texto = completion.choices[0].message.content
except Exception as e:
    resposta_texto = f"Erro ao conectar com a OpenAI: {str(e)}"

print(resposta_texto)

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(resposta_texto.encode("utf-8"))

    def log_message(self, format, *args):
        return

PORT = int(os.environ.get("PORT", 10000))
server = HTTPServer(("0.0.0.0", PORT), Handler)

print(f"Servidor rodando na porta {PORT}...")
server.serve_forever()
