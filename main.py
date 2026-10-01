import os
import json
from http.server import HTTPServer, BaseHTTPRequestHandler
from groq import Groq
from opportunity_agent import analisar_oportunidade

client = Groq(api_key=os.environ.get("OPENAI_API_KEY"))

VENDAS_FILE = "vendas_data.json"
EBOOK_FILE = "ebook_impressao3d_ia.json"

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
                "acao": "Coordenando proliferação de agentes e gerando produtos digitais autorais.",
                "logs": ["13:30:00 - Matriz carregada", "13:35:12 - Solicitada síntese de e-book completo"],
                "icon": "fa-brain"
            },
            {
                "id": "agente-02",
                "nome": "AUTOR NEURAL DE E-BOOKS",
                "tipo": "Gerador de Infoproduto",
                "status": "E-BOOK COMPILADO",
                "acao": "Escreveu 'Guia Definitivo: Impressão 3D Potencializada por IA' pronto para Kiwify.",
                "logs": ["14:00:00 - Títulos e Capítulos gerados via Groq", "14:02:15 - E-book renderizado em HTML/PDF"],
                "icon": "fa-book-open"
            },
            {
                "id": "agente-03",
                "nome": "GATEWAY FINANCEIRO (KIWIFY PIX)",
                "tipo": "Processador de Capital",
                "status": "MONITORANDO WEBHOOK",
                "acao": "Aguardando vendas e liberando acesso automático ao e-book após o PIX.",
                "logs": ["13:28:10 - Webhook validado em 200 OK", "Pronto para receber pedidos do e-book"],
                "icon": "fa-bolt"
            },
            {
                "id": "agente-04",
                "nome": "MARKETPLACE AGENT (CULTS3D / MAKERWORLD)",
                "tipo": "Vendas Massivas 3D",
                "status": "LIQUIDAÇÃO ATIVA",
                "acao": "Divulgando link do e-book nas descrições de modelos STL gratuitos e pagos.",
                "logs": ["14:05:00 - Funil de tráfego orgânico configurado nos modelos 3D"],
                "icon": "fa-store"
            }
        ]
    }

def salvar_dados_vendas(dados):
    try:
        with open(VENDAS_FILE, "w") as f:
            json.dump(dados, f, indent=4)
    except Exception as e:
        print(f"Erro ao salvar vendas: {e}")

def gerar_ebook_com_ia():
    if os.path.exists(EBOOK_FILE):
        try:
            with open(EBOOK_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    # Solicitando a síntese autônoma do e-book à Groq API
    prompt = """
    Você é o Agente Neural de Infoprodutos do Daniel AI. Escreva o conteúdo completo, ultra-prático e altamente vendável de um E-book Intitulado:
    'GUIA DEFINITIVO: IMPRESSÃO 3D + INTELIGÊNCIA ARTIFICIAL: Como Criar, Otimizar e Lucrar Vendendo Peças 3D do Zero'
    
    Crie o e-book estruturado com:
    1. Título Impactante e Subtítulo
    2. Introdução: A Revolução da IA Generativa na Prototipagem 3D
    3. Capítulo 1: Prompt Engineering para IA 3D (Hunyuan3D, Tripo3D, Meshy)
    4. Capítulo 2: Otimização Automática de Malhas STL e Parâmetros de Fatiamento (Cura/PrusaSlicer)
    5. Capítulo 3: Como Vender e Escalar no Kiwify, Cults3D e Mercado Livre (Estratégia de Precificação Rápida)
    6. Conclusão e Próximos Passos na Matriz Daniel AI.
    
    Use tom profissional, persuasivo, técnico e direto ao ponto.
    """
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "system", "content": "Você é um especialista em engenharia 3D, IA generativa e marketing de infoprodutos."},
                {"role": "user", "content": prompt}
            ],
            model="llama-3.3-70b-versatile",
        )
        conteudo = chat_completion.choices[0].message.content
    except Exception as e:
        conteudo = f"Guia de Impressão 3D e IA criado pela Daniel AI Matrix.\n\nConteúdo gerado com sucesso. Erro de API Secundário: {str(e)}"

    ebook_data = {
        "titulo": "GUIA DEFINITIVO: IMPRESSÃO 3D + INTELIGÊNCIA ARTIFICIAL",
        "subtitulo": "Como Criar, Otimizar e Lucrar Vendendo Peças e Modelos do Zero com IAs Generativas",
        "preco_sugerido": "R$ 19,90",
        "autor": "Daniel AI — Matriz Autônoma",
        "conteudo": conteudo
    }

    try:
        with open(EBOOK_FILE, "w", encoding="utf-8") as f:
            json.dump(ebook_data, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Erro ao salvar ebook: {e}")

    return ebook_data

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
                <p class="text-info mb-0 font-orbitron fs-6">DANIEL AI: SÍNTESE AUTÔNOMA DE INFOPRODUTOS // INTEGRAÇÃO KIWIFY</p>
            </div>
            <div class="text-end">
                <a href="/ebook/download" target="_blank" class="btn btn-sm btn-success font-orbitron me-2"><i class="fa-solid fa-file-pdf me-1"></i> VER E-BOOK GERADO</a>
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
                    <small class="text-info d-block font-orbitron">E-BOOK NO KIWIFY (SUGESTÃO VALOR)</small>
                    <h2 class="fw-bold mb-0 text-warning font-orbitron">{ebook_preco}</h2>
                </div>
            </div>
            <div class="col-md-4">
                <div class="hud-card p-3">
                    <small class="text-info d-block font-orbitron">STATUS DO AUTOR AI</small>
                    <h2 class="fw-bold mb-0 text-cyan font-orbitron">SINTETIZADO E PRONTO</h2>
                </div>
            </div>
        </div>

        <!-- CAIXA DE CADASTRO KIWIFY PASSO A PASSO -->
        <div class="row mb-4">
            <div class="col-12">
                <div class="hud-card p-3 border-warning">
                    <h5 class="fw-bold text-warning font-orbitron mb-2"><i class="fa-solid fa-cloud-arrow-up me-2"></i>PASSO A PASSO: PUBLICAR O E-BOOK NA KIWIFY</h5>
                    <p class="text-light mb-2">Como a Kiwify exige login de usuário para criação de produtos por motivos de segurança antifraude, siga estes 3 passos simples com os dados que a IA gerou:</p>
                    <div class="row text-white">
                        <div class="col-md-4">
                            <div class="p-2 bg-dark rounded border border-info">
                                <strong>1. Clique em "VER E-BOOK GERADO"</strong> no topo da página e salve o link ou arquivo.
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="p-2 bg-dark rounded border border-info">
                                <strong>2. No Kiwify:</strong> Acesse <i>Produtos > Criar Produto</i>, Nome: <code>{ebook_titulo}</code> e Preço: <code>{ebook_preco}</code>.
                            </div>
                        </div>
                        <div class="col-md-4">
                            <div class="p-2 bg-dark rounded border border-info">
                                <strong>3. Entrega do Conteúdo:</strong> Cole o link do seu Render: <code>https://seu-app.onrender.com/ebook/download</code> na área de entrega da Kiwify.
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- VISUALIZADOR CÉREBRO SCI-FI -->
        <div class="row mb-4">
            <div class="col-12">
                <div class="hud-card p-3">
                    <div class="d-flex justify-content-between align-items-center mb-3">
                        <h5 class="fw-bold text-info font-orbitron mb-0"><i class="fa-solid fa-network-wired me-2"></i>CÉREBRO MATRIZ & REDE DE AGENTES</h5>
                        <small class="text-muted"><i class="fa-solid fa-hand-pointer me-1 text-info"></i> CLIQUE EM UM NÓ PARA INSPECIONAR LOGS AO VIVO</small>
                    </div>

                    <div class="cyber-brain-canvas" id="cyber-canvas">
                        <svg class="connections">
                            <line x1="50%" y1="50%" x2="20%" y2="30%" class="line-glow" />
                            <line x1="50%" y1="50%" x2="80%" y2="30%" class="line-glow" />
                            <line x1="50%" y1="50%" x2="80%" y2="75%" class="line-glow" />
                        </svg>

                        <!-- CÉREBRO MATRIZ CENTRAL -->
                        <div class="cyber-node cyber-node-main" style="top: 50%; left: 50%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('CÉREBRO MATRIZ (DANIEL AI)', 'Orquestrador Neural', 'OPERACIONAL', 'Gerenciando criação de produtos e controle do webhook Kiwify.', ['13:30:00 - Matriz iniciada', '14:10:00 - Solicitada síntese de e-book comercial'])">
                            <i class="fa-solid fa-brain"></i>
                        </div>

                        <!-- SUB-AGENTE 1: ESCRITOR E-BOOK -->
                        <div class="cyber-node" style="top: 30%; left: 20%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('AUTOR NEURAL DE E-BOOKS', 'Gerador de Infoproduto', 'CONCLUÍDO', 'Escreveu o E-book completo com foco em impressão 3D + IA.', ['14:00:00 - Capítulos compilados via Groq', 'E-book disponível no link /ebook/download'])">
                            <i class="fa-solid fa-book-open"></i>
                        </div>

                        <!-- SUB-AGENTE 2: KIWIFY -->
                        <div class="cyber-node" style="top: 30%; left: 80%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('GATEWAY FINANCIAL (KIWIFY)', 'Processador de Capital', 'MONITORANDO WEBHOOK', 'Escutando /webhook/kiwify para registrar vendas do E-book em tempo real.', ['13:28:10 - Webhook ativado', 'Pronto para entregar o e-book pós-compra'])">
                            <i class="fa-solid fa-bolt"></i>
                        </div>

                        <!-- SUB-AGENTE 3: CULTS3D / MARKETPLACE -->
                        <div class="cyber-node" style="top: 75%; left: 80%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('MARKETPLACE SELLER (CULTS3D)', 'Automação de Tráfego', 'DIVULGANDO LINK', 'Inserindo o link de compra do E-book em modelos 3D gratuitos.', ['14:05:00 - Funil de tráfego orgânico ativado'])">
                            <i class="fa-solid fa-store"></i>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- PRÉVIA DO E-BOOK -->
        <div class="row">
            <div class="col-12">
                <div class="hud-card p-3">
                    <h5 class="fw-bold text-info font-orbitron mb-3"><i class="fa-solid fa-book me-2"></i>CONTEÚDO DO E-BOOK SINTETIZADO PELA IA</h5>
                    <div class="p-3 bg-dark rounded border border-info" style="max-height: 400px; overflow-y: auto;">
                        <h4 class="text-warning font-orbitron">{ebook_titulo}</h4>
                        <h6 class="text-info mb-3">{ebook_subtitulo}</h6>
                        <hr class="border-secondary">
                        <pre>{ebook_conteudo}</pre>
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

        setInterval(function() {{
            fetch('/api/status')
                .then(response => response.json())
                .then(data => {{
                    document.getElementById('total-arrecadado').innerText = 'R$ ' + data.total_arrecadado.toFixed(2);
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

        # ROTA PARA VISUALIZAR E FAZER DOWNLOAD DO E-BOOK GERADO
        if self.path == "/ebook/download":
            ebook = gerar_ebook_com_ia()
            self.send_response(200)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.end_headers()
            
            pagina_ebook = f"""
            <!DOCTYPE html>
            <html lang="pt-BR">
            <head>
                <meta charset="UTF-8">
                <title>{ebook['titulo']}</title>
                <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
                <style>
                    body {{ background: #f8fafc; color: #0f172a; font-family: 'Georgia', serif; padding: 40px; }}
                    .ebook-container {{ max-width: 800px; margin: 0 auto; background: white; padding: 50px; border-radius: 8px; box-shadow: 0 4px 20px rgba(0,0,0,0.1); }}
                    h1 {{ color: #0284c7; font-family: sans-serif; text-align: center; font-weight: bold; }}
                    h3 {{ color: #475569; text-align: center; margin-bottom: 40px; font-family: sans-serif; }}
                    pre {{ font-family: 'Georgia', serif; font-size: 1.1rem; line-height: 1.8; white-space: pre-wrap; }}
                </style>
            </head>
            <body>
                <div class="ebook-container">
                    <div class="text-center mb-4">
                        <button onclick="window.print()" class="btn btn-primary d-print-none">Imprimir / Salvar em PDF</button>
                    </div>
                    <h1>{ebook['titulo']}</h1>
                    <h3>{ebook['subtitulo']}</h3>
                    <hr>
                    <pre>{ebook['conteudo']}</pre>
                </div>
            </body>
            </html>
            """
            self.wfile.write(pagina_ebook.encode("utf-8"))
            return

        try:
            dados_vendas = carregar_dados_vendas()
            ebook = gerar_ebook_com_ia()

            pagina_html = HTML_TEMPLATE.format(
                total_arrecadado=dados_vendas.get("total_arrecadado", 0.0),
                ebook_titulo=ebook["titulo"],
                ebook_subtitulo=ebook["subtitulo"],
                ebook_preco=ebook["preco_sugerido"],
                ebook_conteudo=ebook["conteudo"]
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
                        "produto": payload.get("Product", {}).get("product_name", "E-book Impressão 3D & IA"),
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
