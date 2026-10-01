import os
import json
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from groq import Groq
from opportunity_agent import analisar_oportunidade

client = Groq(api_key=os.environ.get("OPENAI_API_KEY"))

VENDAS_FILE = "vendas_data.json"

def carregar_dados_vendas():
    if os.path.exists(VENDAS_FILE):
        try:
            with open(VENDAS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            pass
    return {
        "total_arrecadado": 0.0,
        "total_vendas": 0,
        "ultimas_vendas": [],
        "agentes_criados": [
            {
                "id": "agente-01",
                "nome": "Cérebro Central (Daniel AI)",
                "tipo": "Orquestrador",
                "status": "Executando",
                "acao": "Gerenciando matriz de agentes e balanceando cargas na Groq API",
                "pos_x": 50, "pos_y": 50
            },
            {
                "id": "agente-02",
                "nome": "Agente Kiwify (Pagamentos)",
                "tipo": "Financeiro",
                "status": "Ativo",
                "acao": "Escutando Webhook em /webhook/kiwify para novos depósitos Pix",
                "pos_x": 20, "pos_y": 25
            },
            {
                "id": "agente-03",
                "nome": "3D Model Creator (Hunyuan/Tripo)",
                "tipo": "Produção 3D",
                "status": "Gerando Modelo",
                "acao": "Criando arquivo STL/OBJ para utilitários de organização 3D",
                "pos_x": 80, "pos_y": 30
            },
            {
                "id": "agente-04",
                "nome": "3D Marketplace Seller",
                "tipo": "Vendas Massivas",
                "status": "Publicando",
                "acao": "Postando modelo no Cults3D & CGTrader a R$ 9,90 para venda rápida",
                "pos_x": 75, "pos_y": 75
            }
        ]
    }

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
    <title>DANIEL RODRIGUES — Cérebro Autônomo de IA</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #0b0f19; color: #f8fafc; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
        .card-custom {{ background-color: #161e2e; border: 1px solid #2d3748; border-radius: 12px; margin-bottom: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.3); }}
        .badge-online {{ background-color: #10b981; color: white; padding: 6px 14px; border-radius: 20px; font-size: 0.85rem; font-weight: 600; box-shadow: 0 0 10px rgba(16,185,129,0.4); }}
        
        /* ÁREA DO CÉREBRO NEURAL */
        .brain-container {{
            position: relative;
            width: 100%;
            height: 380px;
            background: radial-gradient(circle, #1e293b 0%, #0b0f19 80%);
            border: 2px solid #3b82f6;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: inset 0 0 30px rgba(59,130,246,0.2);
        }}
        .node {{
            position: absolute;
            width: 65px;
            height: 65px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.4rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 0 15px rgba(255,255,255,0.2);
            z-index: 2;
        }}
        .node:hover {{ transform: scale(1.18); z-index: 10; box-shadow: 0 0 25px #3b82f6; }}
        .node-main {{ background: linear-gradient(135deg, #ef4444, #8b5cf6); border: 3px solid #ffffff; animation: pulse 2s infinite; }}
        .node-agent {{ background: linear-gradient(135deg, #3b82f6, #06b6d4); border: 2px solid #60a5fa; }}
        .node-3d {{ background: linear-gradient(135deg, #f59e0b, #10b981); border: 2px solid #fcd34d; }}

        @keyframes pulse {{
            0% {{ box-shadow: 0 0 0 0 rgba(139, 92, 246, 0.7); }}
            70% {{ box-shadow: 0 0 0 18px rgba(139, 92, 246, 0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(139, 92, 246, 0); }}
        }}

        pre {{ white-space: pre-wrap; font-family: inherit; font-size: 0.95rem; color: #cbd5e1; }}
    </style>
    <script>
        // Atualização automática a cada 5 segundos
        setInterval(function() {{
            fetch('/api/status')
                .then(response => response.json())
                .then(data => {{
                    document.getElementById('total-arrecadado').innerText = 'R$ ' + data.total_arrecadado.toFixed(2);
                    document.getElementById('total-vendas').innerText = data.total_vendas + ' Vendas';
                    document.getElementById('qtd-agentes').innerText = data.agentes_criados.length + ' Agentes';
                }});
        }}, 5000);

        function abrirDetalhesAgente(nome, tipo, status, acao) {{
            document.getElementById('modal-nome').innerText = nome;
            document.getElementById('modal-tipo').innerText = tipo;
            document.getElementById('modal-status').innerText = status;
            document.getElementById('modal-acao').innerText = acao;
            var myModal = new bootstrap.Modal(document.getElementById('agenteModal'));
            myModal.show();
        }}
    </script>
</head>
<body class="py-4">
    <div class="container">
        <!-- HEADER -->
        <div class="d-flex justify-content-between align-items-center mb-4 pb-3 border-bottom border-secondary">
            <div>
                <h2 class="fw-bold mb-0 text-white"><i class="fa-solid fa-brain text-primary me-2"></i>DANIEL RODRIGUES</h2>
                <small class="text-info fw-semibold">"Daniel AI: Inteligência Escalável, Execução Autônoma, Lucro Contínuo."</small>
            </div>
            <div>
                <span class="badge-online me-2"><i class="fa-solid fa-circle me-1"></i> MATRIZ ATIVA</span>
                <button onclick="location.reload()" class="btn btn-sm btn-outline-light"><i class="fa-solid fa-rotate-right me-1"></i> Atualizar Agora</button>
            </div>
        </div>

        <!-- MÉTRICAS -->
        <div class="row mb-4">
            <div class="col-md-4">
                <div class="card card-custom p-3 border-start border-success border-4">
                    <small class="text-muted d-block">Receita Total Acumulada</small>
                    <h3 class="fw-bold mb-0 text-success" id="total-arrecadado">R$ {total_arrecadado:.2f}</h3>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card card-custom p-3 border-start border-warning border-4">
                    <small class="text-muted d-block">Vendas Realizadas (Kiwify/3D)</small>
                    <h3 class="fw-bold mb-0 text-warning" id="total-vendas">{total_vendas} Vendas</h3>
                </div>
            </div>
            <div class="col-md-4">
                <div class="card card-custom p-3 border-start border-primary border-4">
                    <small class="text-muted d-block">Agentes Proliferados na Rede</small>
                    <h3 class="fw-bold mb-0 text-primary" id="qtd-agentes">{qtd_agentes} Agentes Ativos</h3>
                </div>
            </div>
        </div>

        <!-- MAPA NEURAL DO CÉREBRO -->
        <div class="row mb-4">
            <div class="col-12">
                <div class="card card-custom p-3">
                    <div class="d-flex justify-content-between align-items-center mb-2">
                        <h5 class="fw-bold text-primary mb-0"><i class="fa-solid fa-network-wired me-2"></i>Matriz Neural de Agentes (Clique em um nó para inspecionar)</h5>
                        <small class="text-muted"><i class="fa-solid fa-arrows-rotate fa-spin me-1"></i>Sincronização em Tempo Real</small>
                    </div>
                    <div class="brain-container" id="brain-map">
                        <!-- Nó Cérebro Central -->
                        <div class="node node-main" style="top: 40%; left: 45%;" onclick="abrirDetalhesAgente('Cérebro Mãe (Daniel AI)', 'Orquestrador Supremo', 'Operacional', 'Distribuindo tarefas para criação de modelos 3D e vendas Kiwify')">
                            <i class="fa-solid fa-brain"></i>
                        </div>
                        <!-- Nós Filhos / Sub-Agentes -->
                        <div class="node node-agent" style="top: 15%; left: 20%;" onclick="abrirDetalhesAgente('Agente Kiwify (Vendas)', 'Financeiro', 'Escutando Webhook', 'Capturando notificações de compras Pix')">
                            <i class="fa-solid fa-receipt"></i>
                        </div>
                        <div class="node node-3d" style="top: 20%; left: 75%;" onclick="abrirDetalhesAgente('Agente 3D Hunyuan', 'Gerador 3D', 'Ativo (Hunyuan/Tripo)', 'Convertendo prompts em malhas STL para impressão FDM')">
                            <i class="fa-solid fa-cube"></i>
                        </div>
                        <div class="node node-3d" style="top: 70%; left: 70%;" onclick="abrirDetalhesAgente('Agente Cults3D/CGTrader', 'Vendedor Massivo', 'Publicando', 'Postando modelos a R$ 9,90 para liquidação rápida')">
                            <i class="fa-solid fa-store"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- RELATÓRIO DA GROQ -->
        <div class="row">
            <div class="col-12">
                <div class="card card-custom p-3">
                    <h5 class="fw-bold text-success mb-3 border-bottom pb-2"><i class="fa-solid fa-microchip me-2"></i>Plano Estratégico de Expansão (Groq Intelligence)</h5>
                    <div class="p-3 bg-dark rounded border border-secondary" style="max-height: 400px; overflow-y: auto;">
                        <pre>{conteudo_oportunidade}</pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- MODAL DE INSPEÇÃO DO AGENTE -->
    <div class="modal fade" id="agenteModal" tabindex="-1" aria-hidden="true">
        <div class="modal-dialog modal-dialog-centered">
            <div class="modal-content bg-dark text-white border-primary">
                <div class="modal-header border-secondary">
                    <h5 class="modal-title text-primary"><i class="fa-solid fa-robot me-2"></i>Inspeção de Agente</h5>
                    <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
                </div>
                <div class="modal-body">
                    <p><strong>Nome:</strong> <span id="modal-nome" class="text-info"></span></p>
                    <p><strong>Tipo/Função:</strong> <span id="modal-tipo" class="text-warning"></span></p>
                    <p><strong>Status Operacional:</strong> <span id="modal-status" class="badge bg-success"></span></p>
                    <hr class="border-secondary">
                    <h6>Atividade Atual em Execução:</h6>
                    <p id="modal-acao" class="bg-secondary p-2 rounded text-light"></p>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/webhook/kiwify":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "ok", "message": "Webhook Kiwify Ativo"}).encode("utf-8"))
            return

        if self.path == "/api/status":
            dados_vendas = carregar_dados_vendas()
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(dados_vendas).encode("utf-8"))
            return

        try:
            dados_vendas = carregar_dados_vendas()

            resultado = analisar_oportunidade(
                """
                Apresente o progresso do ecossistema Daniel AI focado em:
                1. Geração massiva de modelos 3D via IA (Hunyuan3D/Tripo3D).
                2. Estratégia de venda rápida em marketplaces (Cults3D, CGTrader, MakerWorld) por valores acessíveis.
                3. Estruturação do Cérebro Multiagente operando de forma 100% autônoma.
                """
            )

            pagina_html = HTML_TEMPLATE.format(
                total_arrecadado=dados_vendas.get("total_arrecadado", 0.0),
                total_vendas=dados_vendas.get("total_vendas", 0),
                qtd_agentes=len(dados_vendas.get("agentes_criados", [])),
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
            erro_msg = f"<h1>Erro no Dashboard:</h1><p>{str(e)}</p>"
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
                        "produto": payload.get("Product", {}).get("product_name", "Modelo 3D / Infoproduto"),
                        "valor": valor_reais,
                        "email": payload.get("Customer", {}).get("email", "N/A")
                    })
                    salvar_dados_vendas(dados)

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success"}).encode("utf-8"))
            except Exception as e:
                self.send_response(200)
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
print("DANIEL RODRIGUES AI — CÉREBRO MULTIAGENTE")
print("===================================")

server = HTTPServer(("0.0.0.0", PORT), Handler)
server.serve_forever()
