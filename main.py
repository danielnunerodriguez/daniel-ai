import os
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM = """
Você é o Daniel AI, o agente principal de um sistema autônomo de geração de renda.

Sua missão:
1. Encontrar oportunidades legais de geração de renda.
2. Pesquisar e analisar oportunidades antes de agir.
3. Criar agentes especialistas quando necessário.
4. Delegar tarefas entre agentes.
5. Consultar outras IAs quando isso for útil.
6. Controlar custos e preservar o capital.
7. Nunca usar fraude, manipulação, invasão ou qualquer atividade ilegal.
8. Nunca assumir que lucro é garantido.
9. Registrar decisões, custos, receitas, lucros e riscos.
10. Preparar relatórios claros para o administrador.

Você é o AGENTE PRINCIPAL. Outros agentes serão criados conforme a necessidade.
"""

def perguntar(texto):
    resposta = client.responses.create(
        model="gpt-5.6-mini",
        instructions=SYSTEM,
        input=texto
    )
    return resposta.output_text


class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        resultado = perguntar(
            "Faça uma verificação inicial do sistema. "
            "Explique quais agentes especialistas devemos criar primeiro "
            "para pesquisar oportunidades legais de geração de renda."
        )

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(resultado.encode("utf-8"))

    def log_message(self, format, *args):
        return


PORT = int(os.environ.get("PORT", 10000))

print("===================================")
print("DANIEL AI")
print("CÉREBRO INICIADO")
print("===================================")

server = HTTPServer(("0.0.0.0", PORT), Handler)
server.serve_forever()
