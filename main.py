import os
from http.server import HTTPServer, BaseHTTPRequestHandler
from groq import Groq
from opportunity_agent import analisar_oportunidade

# O cliente da Groq puxa a chave direto da variável OPENAI_API_KEY do Render
client = Groq(api_key=os.environ.get("OPENAI_API_KEY"))

SYSTEM = """
Você é o Daniel AI, o agente principal de um sistema autônomo de geração de renda.

Sua missão é encontrar, analisar e executar oportunidades legais de geração de renda.

Você pode criar e coordenar agentes especialistas conforme a necessidade.

Áreas possíveis:
- serviços com IA
- logos e design
- tradução
- textos
- programação
- automação
- Workana e Freelancer
- marketplaces
- afiliados
- produtos digitais
- criação de plataformas
- investimentos e mercados financeiros, quando houver estrutura adequada
- qualquer outra oportunidade legal

Regras:
- preservar o capital
- testar antes de escalar
- nunca considerar lucro garantido
- controlar custos e riscos
- nunca utilizar atividades ilegais
- registrar decisões, custos, receitas e resultados
"""

def pensar(missao):
    resposta = client.chat.completions.create(
        model="llama-3.1-8b-instant",  # <--- Alterado aqui
        messages=[
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": missao}
        ]
    )
    return resposta.choices[0].message.content

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        try:
            resultado = analisar_oportunidade(
                """
                Faça uma primeira análise de oportunidades para o Daniel AI.

                Procure possibilidades de gerar renda começar com pouco capital,
                incluindo serviços de IA, plataformas de freelancers,
                criação de produtos digitais e criação de pequenas plataformas.

                Identifique quais oportunidades devem ser investigadas primeiro.
                """
            )

            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write(resultado.encode("utf-8"))
            
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.end_headers()
            erro_msg = f"Erro ao processar oportunidade: {str(e)}"
            self.wfile.write(erro_msg.encode("utf-8"))

    def log_message(self, format, *args):
        return

PORT = int(os.environ.get("PORT", 10000))

print("===================================")
print("DANIEL AI")
print("CÉREBRO + AGENTE DE OPORTUNIDADES")
print("ONLINE (GROQ)")
print("===================================")

server = HTTPServer(("0.0.0.0", PORT), Handler)
server.serve_forever()
