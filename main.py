import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from groq import Groq

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
                "acao": "Gerenciando rede de vendas, entrega automática de infoprodutos e webhooks.",
                "logs": ["Matriz Operacional ativa", "Geração de E-book vinculada na rota /ebook/download"],
                "icon": "fa-brain"
            },
            {
                "id": "agente-02",
                "nome": "GATEWAY FINANCEIRO (KIWIFY PIX)",
                "tipo": "Processador de Capital",
                "status": "MONITORANDO WEBHOOK",
                "acao": "Escutando notificações de pagamento Pix/Cartão para liberar acesso.",
                "logs": ["Webhook registrado e validado em 200 OK", "Aguardando novas vendas Kiwify"],
                "icon": "fa-bolt"
            },
            {
                "id": "agente-03",
                "nome": "SUB-AGENTE AUTOR (E-BOOK BUILDER)",
                "tipo": "Gerador de Conteúdo",
                "status": "E-BOOK PUBLICADO",
                "acao": "Guia Definitivo de Impressão 3D + IA compilado e pronto na rota /ebook/download.",
                "logs": ["Conteúdo estático de alta velocidade compilado", "Download em PDF habilitado"],
                "icon": "fa-book"
            }
        ]
    }

def salvar_dados_vendas(dados):
    try:
        with open(VENDAS_FILE, "w") as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar vendas: {e}")

# CONTEÚDO COMPLETO DO E-BOOK FORMATADO
EBOOK_HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GUIA DEFINITIVO: IMPRESSÃO 3D + INTELIGÊNCIA ARTIFICIAL</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #1e293b; line-height: 1.7; }
        .ebook-container { max-width: 850px; margin: 40px auto; background: #ffffff; padding: 50px; border-radius: 16px; box-shadow: 0 10px 25px rgba(0,0,0,0.08); border: 1px solid #e2e8f0; }
        .hero-banner { background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #ffffff; padding: 40px; border-radius: 12px; margin-bottom: 40px; }
        h1 { font-weight: 800; font-size: 2.2rem; }
        h2 { font-weight: 700; color: #0284c7; margin-top: 35px; border-bottom: 2px solid #e2e8f0; padding-bottom: 8px; }
        h3 { font-weight: 600; color: #334155; margin-top: 20px; }
        .highlight-box { background-color: #f0f9ff; border-left: 4px solid #0284c7; padding: 20px; border-radius: 8px; margin: 25px 0; }
        .btn-download { background-color: #10b981; color: white; font-weight: 700; padding: 14px 28px; border-radius: 8px; text-decoration: none; border: none; }
        .btn-download:hover { background-color: #059669; color: white; }
        @media print {
            .no-print { display: none !important; }
            .ebook-container { box-shadow: none; border: none; padding: 0; margin: 0; }
        }
    </style>
</head>
<body>
    <div class="text-center my-4 no-print">
        <button onclick="window.print()" class="btn-download"><i class="fa-solid fa-file-pdf me-2"></i> Baixar / Imprimir em PDF</button>
    </div>

    <div class="ebook-container">
        <!-- CAPA / HERO -->
        <div class="hero-banner text-center">
            <span class="badge bg-light text-primary mb-2 font-monospace">EDICAO OFICIAL // DANIEL AI MATRIX</span>
            <h1>GUIA DEFINITIVO: IMPRESSÃO 3D + INTELIGÊNCIA ARTIFICIAL</h1>
            <p class="lead mb-0">Como Criar, Otimizar e Lucrar Vendendo Peças e Modelos do Zero com IAs Generativas</p>
        </div>

        <div class="mb-4">
            <p><strong>Autor:</strong> Daniel Rodrigues & Daniel AI Matrix</p>
            <p><strong>Formato:</strong> Manual Prático de Implementação e Monetização</p>
        </div>

        <hr>

        <!-- CAPÍTULO 1 -->
        <h2>Capítulo 1: A Revolução da IA Generativa na Impressão 3D</h2>
        <p>A impressão 3D tradicional sempre enfrentou um gargalo crítico: a dependência de softwares CAD complexos e o tempo exigido para modelagem do zero. Ferramentas como Blender, ZBrush ou Fusion 360 demandam centenas de horas de estudo até que o designer consiga produzir malhas funcionais.</p>
        <p>A Inteligência Artificial Generativa elimina essa barreira. Com o surgimento de algoritmos de <strong>Text-to-3D</strong> e <strong>Image-to-3D</strong>, tornou-se possível converter prompts em linguagem natural ou fotos de referência em malhas tridimensionais (STL, OBJ, GLB) prontas para fatiamento em questão de minutos.</p>

        <div class="highlight-box">
            <h5>💡 As Principais Ferramentas do Mercado Atual:</h5>
            <ul>
                <li><strong>Hunyuan3D (Tencent):</strong> Excelente para geração rápida de formas orgânicas e estruturas volumétricas a partir de imagens.</li>
                <li><strong>Tripo3D:</strong> Alta velocidade na conversão de textos em modelos 3D com malhas limpas e topologia simplificada.</li>
                <li><strong>Meshy.ai:</strong> Especializada em texturização e geração de colecionáveis detalhados.</li>
            </ul>
        </div>

        <!-- CAPÍTULO 2 -->
        <h2>Capítulo 2: Do Texto/Imagem ao Arquivo STL Impresso</h2>
        <p>Para obter peças com alta qualidade de impressão FDM ou Resina, siga o fluxo de trabalho recomendado:</p>

        <h3>1. Engenharia de Prompts para Modelagem 3D</h3>
        <p>Evite descrições genéricas. Quanto mais especificações geométricas você fornecer, melhor será a geometria gerada:</p>
        <ul>
            <li>❌ <em>Prompt Fraco:</em> "Um vaso de planta"</li>
            <li>✅ <em>Prompt Eficiente:</em> "A minimalist geometric parametric vase for 3D printing, flat stable base, watertight manifold mesh, clean topology, smooth surfaces, no overhangs, high resolution STL"</li>
        </ul>

        <h3>2. Validação da Malha (Geometria Estanque / Manifold)</h3>
        <p>Modelos gerados por IA podem conter falhas como normais invertidas ou furos na malha. Antes de enviar para o fatiador (Creality Print, Cura, PrusaSlicer ou Bambu Studio):</p>
        <ol>
            <li>Importe o arquivo no software gratuito <strong>Autodesk Netfabb</strong> ou use o reparo automático do <strong>3D Builder (Windows)</strong>.</li>
            <li>Garanta que a peça seja <em>Watertight</em> (completamente fechada, sem buracos internos).</li>
            <li>Ajuste a orientação na mesa para minimizar a necessidade de suportes.</li>
        </ol>

        <!-- CAPÍTULO 3 -->
        <h2>Capítulo 3: Configurações Ideais para Fatiamento FDM e Resina</h2>
        <table class="table table-bordered my-3">
            <thead class="table-dark">
                <tr>
                    <th>Parâmetro</th>
                    <th>Impressão FDM (Filamento)</th>
                    <th>Impressão SLA (Resina)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Altura de Camada</strong></td>
                    <td>0.16mm - 0.20mm (Peças Funcionais)</td>
                    <td>0.03mm - 0.05mm (Alta Precisão)</td>
                </tr>
                <tr>
                    <td><strong>Paredes / Perímetros</strong></td>
                    <td>3 a 4 linhas (Para maior resistência)</td>
                    <td>Espessura de casca de 2.0mm</td>
                </tr>
                <tr>
                    <td><strong>Preenchimento (Infill)</strong></td>
                    <td>15% a 25% (Gyroid ou Grid)</td>
                    <td>Esvaziado (Hollow) + Furos de Drenagem</td>
                </tr>
            </tbody>
        </table>

        <!-- CAPÍTULO 4 -->
        <h2>Capítulo 4: Estratégias de Monetização e Venda Rápida</h2>
        <p>Existem dois caminhos principais para faturar com esse modelo de negócio:</p>

        <h3>Estratégia A: Venda de Arquivos Digitais (Lucro Passivo Escalonável)</h3>
        <p>Publique os arquivos STL/OBJ em marketplaces especializados como <strong>Cults3D, CGTrader, MakerWorld e Printables</strong>. A chave é precificar entre <strong>R$ 5,00 e R$ 15,00 (US$ 1,00 a US$ 3,00)</strong> para gerar um alto volume de vendas impulsivas por compradores globais.</p>

        <h3>Estratégia B: Infoprodutos e Packs Exclusivos na Kiwify</h3>
        <p>Empacote coleções de modelos organizados por nichos específicos (ex: *Pack Utilitários de Oficina*, *Pack Vasos Decorativos*, *Pack Suportes para Setup Gaming*) e venda o acesso ao Drive com o checkout da Kiwify.</p>

        <div class="highlight-box bg-light border-success">
            <h5 class="text-success">🚀 Resumo da Operação Autônoma:</h5>
            <p class="mb-0">A IA cria o conteúdo e os arquivos digitais ➔ A Kiwify processa o pagamento via Pix/Cartão ➔ O cliente recebe o acesso imediato via Webhook ➔ Você acumula receita 100% no piloto automático.</p>
        </div>

        <div class="text-center mt-5">
            <p class="text-muted mb-1">DANIEL AI MATRIX — SISTEMA AUTÔNOMO DE GERAÇÃO DE RENDA</p>
            <small class="text-secondary">© Todos os direitos reservados.</small>
        </div>
    </div>
</body>
</html>
"""

HTML_DASHBOARD = """
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
        body {
            background-color: #030712; color: #38bdf8; font-family: 'Rajdhani', sans-serif;
            background-image: radial-gradient(rgba(14, 165, 233, 0.15) 1px, transparent 0), radial-gradient(rgba(14, 165, 233, 0.1) 1px, #030712 100%);
            background-size: 24px 24px, 100% 100%; overflow-x: hidden;
        }
        .hud-card {
            background: rgba(15, 23, 42, 0.85); border: 1px solid #0284c7;
            box-shadow: 0 0 15px rgba(2, 132, 199, 0.25); border-radius: 8px; backdrop-filter: blur(8px);
        }
        .cyber-brain-canvas {
            position: relative; width: 100%; height: 380px;
            background: radial-gradient(circle, rgba(14,165,233,0.12) 0%, rgba(3,7,18,0.95) 80%);
            border: 1px solid #0284c7; border-radius: 12px; overflow: hidden;
        }
        .cyber-node {
            position: absolute; width: 70px; height: 70px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center; font-size: 1.6rem;
            color: #00f0ff; cursor: pointer; z-index: 5; transition: all 0.3s;
            background: rgba(15, 23, 42, 0.9); border: 2px solid #00f0ff; box-shadow: 0 0 15px #00f0ff;
        }
        .cyber-node-main { width: 90px; height: 90px; font-size: 2.2rem; color: #ff007f; border-color: #ff007f; box-shadow: 0 0 25px #ff007f; }
        .hud-drawer {
            position: fixed; top: 0; right: -420px; width: 400px; height: 100vh;
            background: rgba(3, 7, 18, 0.95); border-left: 2px solid #00f0ff;
            box-shadow: -10px 0 30px rgba(0, 240, 255, 0.3); z-index: 9999;
            transition: right 0.4s; padding: 25px; overflow-y: auto;
        }
        .hud-drawer.active { right: 0; }
        .badge-neon { background: rgba(0, 240, 255, 0.1); color: #00f0ff; border: 1px solid #00f0ff; padding: 4px 10px; border-radius: 4px; }
        svg.connections { position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; }
        .line-glow { stroke: #00f0ff; stroke-width: 2; stroke-dasharray: 6 4; }
    </style>
</head>
<body class="py-4">
    <div class="container-fluid px-4">
        <div class="d-flex justify-content-between align-items-center mb-4 pb-3 border-bottom border-info">
            <div>
                <h1 class="fw-bold mb-0 text-white"><i class="fa-solid fa-microchip text-info me-2"></i>DANIEL RODRIGUES</h1>
                <p class="text-info mb-0 fs-6">DANIEL AI: INTELIGÊNCIA ESCALÁVEL // EXECUÇÃO AUTÔNOMA // LUCRO CONTÍNUO</p>
            </div>
            <div>
                <span class="badge-neon me-2"><i class="fa-solid fa-circle-dot me-1 text-success"></i> MATRIZ NEURAL ONLINE</span>
                <a href="/ebook/download" target="_blank" class="btn btn-sm btn-success fw-bold"><i class="fa-solid fa-book me-1"></i> Ver E-book Gerado</a>
            </div>
        </div>

        <div class="row mb-4">
            <div class="col-md-4">
                <div class="hud-card p-3">
                    <small class="text-info d-block">RECEITA TOTAL ACUMULADA</small>
                    <h2 class="fw-bold mb-0 text-success" id="total-arrecadado">R$ {total_arrecadado:.2f}</h2>
                </div>
            </div>
            <div class="col-md-4">
                <div class="hud-card p-3">
                    <small class="text-info d-block">TRANSAÇÕES KIWIFY</small>
                    <h2 class="fw-bold mb-0 text-warning" id="total-vendas">{total_vendas} CONCLUÍDAS</h2>
                </div>
            </div>
            <div class="col-md-4">
                <div class="hud-card p-3">
                    <small class="text-info d-block">SUB-AGENTES PROLIFERADOS</small>
                    <h2 class="fw-bold mb-0 text-info" id="qtd-agentes">{qtd_agentes} AGENTES ATIVOS</h2>
                </div>
            </div>
        </div>

        <div class="row mb-4">
            <div class="col-12">
                <div class="hud-card p-3">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="fw-bold text-info mb-0"><i class="fa-solid fa-network-wired me-2"></i>MATRIZ NEURAL DE AGENTES</h5>
                        <small class="text-muted"><i class="fa-solid fa-hand-pointer me-1 text-info"></i> CLIQUE NOS NÓS PARA INSPECIONAR</small>
                    </div>

                    <div class="cyber-brain-canvas">
                        <svg class="connections">
                            <line x1="50%" y1="50%" x2="20%" y2="30%" class="line-glow" />
                            <line x1="50%" y1="50%" x2="80%" y2="30%" class="line-glow" />
                        </svg>

                        <div class="cyber-node cyber-node-main" style="top: 50%; left: 50%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('CÉREBRO MATRIZ (DANIEL AI)', 'Orquestrador Neural', 'OPERACIONAL', 'Coordenando fluxo de vendas Kiwify e disponibilização do e-book.', ['Matriz iniciada', 'E-book em /ebook/download'])">
                            <i class="fa-solid fa-brain"></i>
                        </div>

                        <div class="cyber-node" style="top: 30%; left: 20%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('GATEWAY FINANCIAL (KIWIFY)', 'Agente de Capital', 'MONITORANDO WEBHOOK', 'Escutando /webhook/kiwify para crédito imediato.', ['Webhook 200 OK', 'Pronto para novas transações'])">
                            <i class="fa-solid fa-bolt"></i>
                        </div>

                        <div class="cyber-node" style="top: 30%; left: 80%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('SUB-AGENTE AUTOR (E-BOOK)', 'Gerador de Conteúdo', 'PUBLICADO', 'E-book de Impressão 3D + IA ativo na rota /ebook/download.', ['Conteúdo estático de alta velocidade compilado', 'Ativo para os clientes'])">
                            <i class="fa-solid fa-book"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <div class="hud-drawer" id="hudDrawer">
        <div class="d-flex justify-content-between align-items-center mb-4 border-bottom border-info pb-2">
            <h5 class="fw-bold text-info mb-0">INSPECTOR HUD</h5>
            <button onclick="fecharInspector()" class="btn btn-sm btn-outline-info"><i class="fa-solid fa-xmark"></i></button>
        </div>
        <div class="mb-3">
            <small class="text-muted d-block">AGENTE</small>
            <h4 class="fw-bold text-white" id="drawer-nome">-</h4>
        </div>
        <div class="mb-3">
            <small class="text-muted d-block">TIPO</small>
            <span class="badge-neon" id="drawer-tipo">-</span>
        </div>
        <div class="mb-3">
            <small class="text-muted d-block">STATUS</small>
            <span class="badge bg-success" id="drawer-status">-</span>
        </div>
        <div class="mb-4">
            <small class="text-muted d-block">AÇÃO ATUAL</small>
            <p class="p-2 bg-dark text-info rounded border border-secondary" id="drawer-acao">-</p>
        </div>
    </div>

    <script>
        function abrirInspector(nome, tipo, status, acao, logs) {
            document.getElementById('drawer-nome').innerText = nome;
            document.getElementById('drawer-tipo').innerText = tipo;
            document.getElementById('drawer-status').innerText = status;
            document.getElementById('drawer-acao').innerText = acao;
            document.getElementById('hudDrawer').classList.add('active');
        }
        function fecharInspector() {
            document.getElementById('hudDrawer').classList.remove('active');
        }
    </script>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # ROTA DO E-BOOK COMPLETO FORMATADO
        if self.path == "/ebook/download":
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(EBOOK_HTML.encode("utf-8"))
            return

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
            pagina_html = HTML_DASHBOARD.format(
                total_arrecadado=dados_vendas.get("total_arrecadado", 0.0),
                total_vendas=dados_vendas.get("total_vendas", 0),
                qtd_agentes=len(dados_vendas.get("agentes_criados", []))
            )
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            self.wfile.write(pagina_html.encode("utf-8"))
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(f"<h1>Erro Matrix:</h1><p>{str(e)}</p>".encode("utf-8"))

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
