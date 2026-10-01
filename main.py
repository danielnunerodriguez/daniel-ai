import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from groq import Groq
from opportunity_agent import analisar_oportunidade

client = Groq(api_key=os.environ.get("OPENAI_API_KEY"))

# Ficheiro para guardar as vendas recebidas localmente
VENDAS_FILE = "vendas_data.json"

def carregar_dados_vendas():
    if os.path.exists(VENDAS_FILE):
        try:
            with open(VENDAS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {"total_arrecadado": 0.0, "total_vendas": 0, "ultimas_vendas": []}

def salvar_dados_vendas(dados):
    try:
        with open(VENDAS_FILE, "w") as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar vendas: {e}")

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DANIEL AI - Painel de Controle Autônomo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #0f172a; color: #f8fafc; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
        .card-custom {{ background-color: #1e293b; border: 1px solid #334155; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1); }}
        .badge-online {{ background-color: #10b981; color: white; padding: 5px 12px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; }}
        .stat-card {{ background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%); border-left: 4px solid #3b82f6; }}
        .agent-avatar {{ width: 45px; height: 45px; border-radius: 50%; background: #3b82f6; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; margin-right: 15px; }}
        .action-required {{ background-color: #451a03; border: 1px solid #78350f; border-radius: 8px; padding: 15px; margin-top: 15px; }}
        pre {{ white-space: pre-wrap; font-family: inherit; font-size: 0.95rem; line-height: 1.6; color: #cbd5e1; }}
    </style>
</head>
<body class="py-4">
    <div class="container">
        <!-- HEADER -->
        <div class="d-flex justify-content-between align-items-center mb-4 pb-3 border-bottom border-secondary">
            <div>
                <h2 class="fw-bold mb-0 text-white"><i class="fa-solid fa-robot text-primary me-2"></i>DANIEL AI</h2>
                <small class="text-muted">Sistema Autônomo de Geração de Renda & Infoprodutos</small>
            </div>
            <div>
                <span class="badge-online me-2"><i class="fa-solid fa-circle me-1"></i> SISTEMA ATIVO (GROQ + KIWIFY)</span>
                <button onclick="location.reload()" class="btn btn-sm btn-outline-light"><i class="fa-solid fa-rotate-right me-1"></i> Atualizar</button>
            </div>
        </div>

        <!-- MÉTRICAS PRINCIPAIS -->
        <div class="row mb-4">
            <div class="col-md-4">
                <div class="card card-custom stat-card p-3">
                    <div class="d-flex align-items-center">
                        <div class="agent-avatar bg-success text-white"><i class="fa-solid fa-wallet"></i></div>
                        <div>
                            <small class="text-muted d-block">Receita Arrecadada (Kiwify)</small>
                            <h3 class="fw-bold mb-0 text-success">R$ {total_arrecadado:.2f}</h3>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card card-custom stat-card p-3" style="border-left-color: #eab308;">
                    <div class="d-flex align-items-center">
                        <div class="agent-avatar bg-warning text-dark"><i class="fa-solid fa-bag-shopping"></i></div>
                        <div>
                            <small class="text-muted d-block">Total de Vendas Concluídas</small>
                            <h3 class="fw-bold mb-0 text-warning">{total_vendas} Vendas</h3>
                        </div>
                    </div>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card card-custom stat-card p-3" style="border-left-color: #8b5cf6;">
                    <div class="d-flex align-items-center">
                        <div class="agent-avatar bg-purple text-white" style="background:#8b5cf6"><i class="fa-solid fa-network-wired"></i></div>
                        <div>
                            <small class="text-muted d-block">Agentes Operacionais</small>
                            <h3 class="fw-bold mb-0 text-white">3 Agentes</h3>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="row">
            <!-- PAINEL DOS AGENTES -->
            <div class="col-md-4">
                <div class="card card-custom p-3">
                    <h5 class="fw-bold mb-3 border-bottom pb-2 text-primary"><i class="fa-solid fa-users-gear me-2"></i>Status dos Agentes</h5>
                    
                    <div class="d-flex align-items-center mb-3 p-2 rounded bg-dark">
                        <div class="agent-avatar bg-primary text-white"><i class="fa-solid fa-brain"></i></div>
                        <div>
                            <strong class="d-block text-white">Daniel AI (Cérebro)</strong>
                            <small class="text-success"><i class="fa-solid fa-circle-dot me-1"></i>Monitorando Sistema</small>
                        </div>
                    </div>

                    <div class="d-flex align-items-center mb-3 p-2 rounded bg-dark">
                        <div class="agent-avatar bg-info text-white"><i class="fa-solid fa-magnifying-glass-dollar"></i></div>
                        <div>
                            <strong class="d-block text-white">Agente de Oportunidades</strong>
                            <small class="text-info"><i class="fa-solid fa-spinner fa-spin me-1"></i>Mapeando Mercado</small>
                        </div>
                    </div>

                    <div class="d-flex align-items-center mb-3 p-2 rounded bg-dark">
                        <div class="agent-avatar bg-success text-white"><i class="fa-solid fa-receipt"></i></div>
                        <div>
                            <strong class="d-block text-white">Agente Kiwify (Vendas)</strong>
                            <small class="text-success"><i class="fa-solid fa-check me-1"></i>Webhook Pronto</small>
                        </div>
                    </div>

                    <div class="action-required">
                        <h6 class="fw-bold text-warning mb-2"><i class="fa-solid fa-circle-info me-2"></i>Status da Integração</h6>
                        <small class="d-block text-light mb-2">Sua URL de Webhook está ativa e pronta para receber alertas de vendas em tempo real.</small>
                        <span class="badge bg-success text-dark">Integrado à Kiwify</span>
                    </div>
                </div>
            </div>

            <!-- PAINEL DE OPORTUNIDADES PESQUISADAS -->
            <div class="col-md-8">
                <div class="card card-custom p-3">
                    <div class="d-flex justify-content-between align-items-center mb-3 border-bottom pb-2">
                        <h5 class="fw-bold mb-0 text-success"><i class="fa-solid fa-chart-line me-2"></i>Análise de Oportunidades & Produtos</h5>
                        <small class="text-muted">Gerado via Groq</small>
                    </div>
                    <div class="p-3 bg-dark rounded border border-secondary" style="max-height: 600px; overflow-y: auto;">
                        <pre>{conteudo_oportunidade}</pre>
                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Validação do teste do Webhook da Kiwify
        if self.path == "/webhook/kiwify":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "message": "Webhook Kiwify Ativo"}).encode("utf-8"))
            return

        try:
            dados_vendas = carregar_dados_vendas()

            resultado = analisar_oportunidade(
                """
                Faça uma análise focada em produtos digitais para venda na Kiwify e serviços automatizados.
                Identifique 3 ideias de e-books, modelos 3D ou ferramentas digitais simples que o Daniel AI pode gerar.
                """
            )

            pagina_html = HTML_TEMPLATE.format(
                total_arrecadado=dados_vendas.get("total_arrecadado", 0.0),
                total_vendas=dados_vendas.get("total_vendas", 0),
                conteudo_oportunidade=resultado
            )

            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(pagina_html.encode("utf-8"))
            
        except Exception as e:
            self.send_response(500)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            erro_msg = f"<h1>Erro ao carregar Dashboard:</h1><p>{str(e)}</p>"
            self.wfile.write(erro_msg.encode("utf-8"))

    def do_POST(self):
        if self.path == "/webhook/kiwify":
            try:
                content_length = int(self.headers.get("Content-Length", 0))
                body = self.rfile.read(content_length) if content_length > 0 else b"{}"
                payload = json.loads(body.decode("utf-8")) if body else {}

                status = payload.get("order_status") or payload.get("status")
                
                if status in ["paid", "approved", "completed"]:
                    comissao = payload.get("Commissions", {}).get("my_commission", 0)
                    valor_reais = float(comissao) / 100.0 if comissao > 0 else float(payload.get("order_ref_amount", 0)) / 100.0

                    dados = carregar_dados_vendas()
                    dados["total_arrecadado"] += valor_reais
                    dados["total_vendas"] += 1
                    dados["ultimas_vendas"].append({
                        "produto": payload.get("Product", {}).get("product_name", "Infoproduto"),
                        "valor": valor_reais,
                        "email": payload.get("Customer", {}).get("email", "N/A")
                    })
                    salvar_dados_vendas(dados)

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success"}).encode("utf-8"))
            except Exception as e:
                self.send_response(200)  # Retorna 200 para a Kiwify aceitar mesmo em testes
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "received", "note": str(e)}).encode("utf-8"))
        else:
            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return

PORT = int(os.environ.get("PORT", 10000))

print("===================================")
print("DANIEL AI - DASHBOARD + KIWIFY WEBHOOK")
print("===================================")

server = HTTPServer(("0.0.0.0", PORT), Handler)
server.serve_forever()
