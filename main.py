import os
import json
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
                "nome": "CÉREBRO MATRIZ (DANIEL AI)",
                "tipo": "Orquestrador Neural",
                "status": "OPERACIONAL",
                "acao": "Coordenando proliferação de agentes e distribuindo prompts na Groq API.",
                "logs": ["13:30:00 - Matriz carregada", "13:31:12 - Distribuindo tarefas para o módulo 3D"],
                "icon": "fa-brain",
                "x": 50, "y": 50
            },
            {
                "id": "agente-02",
                "nome": "GATEWAY FINACEIRO (KIWIFY PIX)",
                "tipo": "Processador de Capital",
                "status": "MONITORANDO WEBHOOK",
                "acao": "Escutando requisições na porta /webhook/kiwify para crédito imediato.",
                "logs": ["13:28:10 - Webhook validado em 200 OK", "Aguardando notificações de compra"],
                "icon": "fa-bolt",
                "x": 20, "y": 30
            },
            {
                "id": "agente-03",
                "nome": "SINTETIZADOR 3D (HUNYUAN / TRIPO3D)",
                "tipo": "Gerador de Geometria",
                "status": "GERANDO MALHAS STL",
                "acao": "Gerando utilitários organizadores 3D e peças funcionais via API.",
                "logs": ["13:32:05 - Prompt processado no Hunyuan3D", "Arquivo .STL otimizado para FDM/SLA"],
                "icon": "fa-cube",
                "x": 80, "y": 30
            },
            {
                "id": "agente-04",
                "nome": "MARKETPLACE AGENT (CULTS3D / CGTRADER)",
                "tipo": "Vendas Massivas",
                "status": "LIQUIDAÇÃO ATIVA",
                "acao": "Postando novos modelos a R$ 9,90 para alta rotatividade de vendas.",
                "logs": ["13:33:10 - Anúncio criado no Cults3D", "Sincronizando vitrine no MakerWorld"],
                "icon": "fa-store",
                "x": 80, "y": 75
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
    <title>DANIEL RODRIGUES — NEURAL AI MATRIX</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;600;800;900&family=Rajdhani:wght@500;600;700&display=swap');

        body {{
            background-color: #030712;
            color: #38bdf8;
            font-family: 'Rajdhani', sans-serif;
            background-image: 
                radial-gradient(rgba(14, 165, 233, 0.15) 1px, transparent 0),
                radial-gradient(rgba(14, 165, 233, 0.1) 1px, #030712 100%);
            background-size: 24px 24px, 100% 100%;
            overflow-x: hidden;
        }}

        h1, h2, h3, h4, h5, h6, .font-orbitron {{
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 1.5px;
        }}

        .hud-card {{
            background: rgba(15, 23, 42, 0.85);
            border: 1px solid #0284c7;
            box-shadow: 0 0 15px rgba(2, 132, 199, 0.25), inset 0 0 15px rgba(2, 132, 199, 0.1);
            border-radius: 8px;
            backdrop-filter: blur(8px);
            position: relative;
        }}
        .hud-card::before {{
            content: '';
            position: absolute;
            top: -2px; left: -2px;
            width: 10px; height: 10px;
            border-top: 2px solid #38bdf8;
            border-left: 2px solid #38bdf8;
        }}
        .hud-card::after {{
            content: '';
            position: absolute;
            bottom: -2px; right: -2px;
            width: 10px; height: 10px;
            border-bottom: 2px solid #38bdf8;
            border-right: 2px solid #38bdf8;
        }}

        /* ÁREA DO CÉREBRO NEURAL SCI-FI */
        .cyber-brain-canvas {{
            position: relative;
            width: 100%;
            height: 420px;
            background: radial-gradient(circle, rgba(14,165,233,0.12) 0%, rgba(3,7,18,0.95) 80%);
            border: 1px solid #0284c7;
            border-radius: 12px;
            overflow: hidden;
            box-shadow: 0 0 25px rgba(14,165,233,0.2);
        }}

        svg.connections {{
            position: absolute;
            top: 0; left: 0;
            width: 100%; height: 100%;
            z-index: 1;
            pointer-events: none;
        }}

        .line-glow {{
            stroke: #00f0ff;
            stroke-width: 2;
            stroke-dasharray: 6 4;
            animation: dash 15s linear infinite;
            filter: drop-shadow(0 0 6px #00f0ff);
        }}

        @keyframes dash {{
            to {{ stroke-dashoffset: -100; }}
        }}

        /* NÓS DOS AGENTES */
        .cyber-node {{
            position: absolute;
            width: 70px;
            height: 70px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.6rem;
            color: #00f0ff;
            cursor: pointer;
            z-index: 5;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            background: rgba(15, 23, 42, 0.9);
            border: 2px solid #00f0ff;
            box-shadow: 0 0 15px #00f0ff, inset 0 0 10px #00f0ff;
        }}

        .cyber-node:hover {{
            transform: scale(1.25) translate(-50%, -50%) !important;
            box-shadow: 0 0 30px #00f0ff, inset 0 0 20px #00f0ff;
            border-color: #ffffff;
            color: #ffffff;
        }}

        .cyber-node-main {{
            width: 90px;
            height: 90px;
            font-size: 2.2rem;
            color: #ff007f;
            border-color: #ff007f;
            box-shadow: 0 0 25px #ff007f, inset 0 0 15px #ff007f;
            animation: pulse-red 2s infinite alternate;
        }}

        @keyframes pulse-red {{
            0% {{ box-shadow: 0 0 15px #ff007f; }}
            100% {{ box-shadow: 0 0 35px #ff007f, 0 0 10px #00f0ff; }}
        }}

        /* DRAWER LATERAL DE INSPEÇÃO (HUD) */
        .hud-drawer {{
            position: fixed;
            top: 0; right: -420px;
            width: 400px; height: 100vh;
            background: rgba(3, 7, 18, 0.95);
            border-left: 2px solid #00f0ff;
            box-shadow: -10px 0 30px rgba(0, 240, 255, 0.3);
            z-index: 9999;
            transition: right 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            padding: 25px;
            overflow-y: auto;
            backdrop-filter: blur(12px);
        }}
        .hud-drawer.active {{ right: 0; }}

        .badge-neon {{
            background: rgba(0, 240, 255, 0.1);
            color: #00f0ff;
            border: 1px solid #00f0ff;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.8rem;
        }}
        
        pre {{ color: #a5f3fc; white-space: pre-wrap; font-family: 'Rajdhani', sans-serif; font-size: 1.05rem; }}
    </style>
</head>
<body class="py-4">
    <div class="container-fluid px-4">
        <!-- HEADER -->
        <div class="d-flex justify-content-between align-items-center mb-4 pb-3 border-bottom border-info">
            <div>
                <h1 class="fw-bold mb-0 text-white font-orbitron"><i class="fa-solid fa-microchip text-info me-2"></i>DANIEL RODRIGUES</h1>
                <p class="text-info mb-0 font-orbitron fs-6">DANIEL AI: INTELIGÊNCIA ESCALÁVEL // EXECUÇÃO AUTÔNOMA // LUCRO CONTÍNUO</p>
            </div>
            <div class="text-end">
                <span class="badge-neon me-2"><i class="fa-solid fa-circle-dot me-1 text-success"></i> MATRIZ NEURAL ONLINE</span>
                <button onclick="location.reload()" class="btn btn-sm btn-outline-info font-orbitron"><i class="fa-solid fa-rotate me-1"></i> RE-SYNC</button>
            </div>
        </div>

        <!-- MÉTRICAS SCI-FI -->
        <div class="row mb-4">
            <div class="col-md-4">
                <div class="hud-card p-3">
                    <small class="text-info d-block font-orbitron">RECEITA TOTAL ACUMULADA</small>
                    <h2 class="fw-bold mb-0 text-success font-orbitron" id="total-arrecadado">R$ {total_arrecadado:.2f}</h2>
                </div>
            </div>
            <div class="col-md-4">
                <div class="hud-card p-3">
                    <small class="text-info d-block font-orbitron">TRANSAÇÕES & VENDAS (KIWIFY / 3D)</small>
                    <h2 class="fw-bold mb-0 text-warning font-orbitron" id="total-vendas">{total_vendas} CONCLUÍDAS</h2>
                </div>
            </div>
            <div class="col-md-4">
                <div class="hud-card p-3">
                    <small class="text-info d-block font-orbitron">SUB-AGENTES PROLIFERADOS</small>
                    <h2 class="fw-bold mb-0 text-cyan font-orbitron" id="qtd-agentes">{qtd_agentes} AGENTES ATIVOS</h2>
                </div>
            </div>
        </div>

        <!-- VISUALIZADOR CÉREBRO SCI-FI COM CANVAS SVG -->
        <div class="row mb-4">
            <div class="col-12">
                <div class="hud-card p-3">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="fw-bold text-info font-orbitron mb-0"><i class="fa-solid fa-network-wired me-2"></i>CÉREBRO MATRIZ & REDE DE AGENTES</h5>
                        <small class="text-muted"><i class="fa-solid fa-hand-pointer me-1 text-info"></i> CLIQUE EM UM NÓ PARA INSPECIONAR LOGS AO VIVO</small>
                    </div>

                    <div class="cyber-brain-canvas" id="cyber-canvas">
                        <!-- Conexões SVG de Circuitos -->
                        <svg class="connections">
                            <line x1="50%" y1="50%" x2="20%" y2="30%" class="line-glow" />
                            <line x1="50%" y1="50%" x2="80%" y2="30%" class="line-glow" />
                            <line x1="50%" y1="50%" x2="80%" y2="75%" class="line-glow" />
                        </svg>

                        <!-- CÉREBRO MATRIZ CENTRAL -->
                        <div class="cyber-node cyber-node-main" style="top: 50%; left: 50%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('CÉREBRO MATRIZ (DANIEL AI)', 'Orquestrador Neural', 'OPERACIONAL', 'Gerenciando rede multi-agente, alocação de chaves Groq e rotas de vendas.', ['13:30:00 - Matriz iniciada', '13:34:12 - Sincronização de rotas OK'])">
                            <i class="fa-solid fa-brain"></i>
                        </div>

                        <!-- SUB-AGENTE 1: KIWIFY -->
                        <div class="cyber-node" style="top: 30%; left: 20%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('GATEWAY FINANCIAL (KIWIFY)', 'Agente de Capital', 'MONITORANDO WEBHOOK', 'Escutando /webhook/kiwify para registrar compras em tempo real.', ['13:28:10 - Webhook validado 200 OK', 'Aguardando notificações de transação'])">
                            <i class="fa-solid fa-bolt"></i>
                        </div>

                        <!-- SUB-AGENTE 2: SINTETIZADOR 3D -->
                        <div class="cyber-node" style="top: 30%; left: 80%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('SINTETIZADOR 3D (HUNYUAN/TRIPO3D)', 'Gerador de Geometria', 'SINTETIZANDO MODELOS', 'Gerando peças funcionais e colecionáveis em STL/OBJ.', ['13:32:05 - Prompt enviado ao Hunyuan3D', 'Malha STL limpa e pronta para FDM'])">
                            <i class="fa-solid fa-cube"></i>
                        </div>

                        <!-- SUB-AGENTE 3: CULTS3D / CGTRADER -->
                        <div class="cyber-node" style="top: 75%; left: 80%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('MARKETPLACE SELLER (CULTS3D/CGTRADER)', 'Automação de Vendas', 'PUBLICANDO PRODUTOS', 'Publicando modelos a R$ 9,90 para vendas de alto volume.', ['13:33:10 - Anúncio gerado no Cults3D', 'Render promocional publicado'])">
                            <i class="fa-solid fa-store"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- RELATÓRIO DA GROQ -->
        <div class="row">
            <div class="col-12">
                <div class="hud-card p-3">
                    <h5 class="fw-bold text-info font-orbitron mb-3"><i class="fa-solid fa-terminal me-2"></i>DIRETRIZES DE EXPANSAO DA INTELIGENCIA</h5>
                    <div class="p-3 bg-dark rounded border border-info" style="max-height: 350px; overflow-y: auto;">
                        <pre>{conteudo_oportunidade}</pre>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- HUD DRAWER LATERAL DE INSPEÇÃO -->
    <div class="hud-drawer" id="hudDrawer">
        <div class="d-flex justify-content-between align-items-center mb-4 pb-2 border-bottom border-info">
            <h5 class="fw-bold text-info font-orbitron mb-0"><i class="fa-solid fa-sliders me-2"></i>INSPECTOR HUD</h5>
            <button onclick="fecharInspector()" class="btn btn-sm btn-outline-info"><i class="fa-solid fa-xmark"></i></button>
        </div>

        <div class="mb-3">
            <small class="text-muted d-block font-orbitron">NOME DO AGENTE</small>
            <h4 class="fw-bold text-white font-orbitron" id="drawer-nome">-</h4>
        </div>

        <div class="mb-3">
            <small class="text-muted d-block font-orbitron">TIPO / ARQUITETURA</small>
            <span class="badge-neon" id="drawer-tipo">-</span>
        </div>

        <div class="mb-3">
            <small class="text-muted d-block font-orbitron">STATUS DE EXECUÇÃO</small>
            <span class="badge bg-success font-orbitron" id="drawer-status">-</span>
        </div>

        <div class="mb-4">
            <small class="text-muted d-block font-orbitron">TAREFA EM ANDAMENTO</small>
            <p class="p-2 bg-dark rounded text-info border border-secondary" id="drawer-acao">-</p>
        </div>

        <div>
            <small class="text-muted d-block font-orbitron mb-2">LOGS DE EXECUÇÃO AO VIVO</small>
            <ul class="list-group list-group-flush bg-dark rounded border border-secondary" id="drawer-logs">
            </ul>
        </div>
    </div>

    <script>
        function abrirInspector(nome, tipo, status, acao, logs) {{
            document.getElementById('drawer-nome').innerText = nome;
            document.getElementById('drawer-tipo').innerText = tipo;
            document.getElementById('drawer-status').innerText = status;
            document.getElementById('drawer-acao').innerText = acao;
            
            var logsContainer = document.getElementById('drawer-logs');
            logsContainer.innerHTML = '';
            logs.forEach(function(log) {{
                var li = document.createElement('li');
                li.className = 'list-group-item bg-transparent text-info border-secondary font-monospace fs-6';
                li.innerHTML = '<i class="fa-solid fa-angle-right me-2 text-warning"></i>' + log;
                logsContainer.appendChild(li);
            }});

            document.getElementById('hudDrawer').classList.add('active');
        }}

        function fecharInspector() {{
            document.getElementById('hudDrawer').classList.remove('active');
        }}

        // Atualização automática via API
        setInterval(function() {{
            fetch('/api/status')
                .then(response => response.json())
                .then(data => {{
                    document.getElementById('total-arrecadado').innerText = 'R$ ' + data.total_arrecadado.toFixed(2);
                    document.getElementById('total-vendas').innerText = data.total_vendas + ' CONCLUÍDAS';
                    document.getElementById('qtd-agentes').innerText = data.agentes_criados.length + ' AGENTES ATIVOS';
                }});
        }}, 4000);
    </script>
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
                Apresente o plano de expansão autônoma da matriz Daniel AI focado em:
                1. Síntese massiva de peças e utilitários 3D via Hunyuan3D / Tripo3D.
                2. Liquidação acelerada em marketplaces (Cults3D, CGTrader, MakerWorld) por preços de R$ 5 a R$ 15.
                3. Proliferação de novos sub-agentes sem intervenção humana.
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
            erro_msg = f"<h1>Erro Matrix:</h1><p>{str(e)}</p>"
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
print("DANIEL RODRIGUES — CYBER NEURAL MATRIX")
print("===================================")

server = HTTPServer(("0.0.0.0", PORT), Handler)
server.serve_forever()
