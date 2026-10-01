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
                "acao": "Gerenciando entrega do e-book completo de 15 capítulos e Webhook Kiwify.",
                "logs": ["Matriz Operacional ativa", "Apostila de 15 capítulos disponível em /ebook/download"],
                "icon": "fa-brain"
            },
            {
                "id": "agente-02",
                "nome": "GATEWAY FINANCEIRO (KIWIFY PIX)",
                "tipo": "Processador de Capital",
                "status": "MONITORANDO WEBHOOK",
                "acao": "Escutando requisições na rota /webhook/kiwify para liberação automática.",
                "logs": ["Webhook 200 OK", "Aguardando confirmações de pagamento"],
                "icon": "fa-bolt"
            },
            {
                "id": "agente-03",
                "nome": "SUB-AGENTE AUTOR (LIVRO COMPLETO)",
                "tipo": "Gerador de Conteúdo",
                "status": "APOSTILA 15 CAPÍTULOS ATIVA",
                "acao": "Manual Completo de Impressão 3D + IA ativo na rota /ebook/download.",
                "logs": ["Guia estático denso gerado com sucesso", "Download em PDF ativo"],
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

EBOOK_HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GUIA DEFINITIVO: IMPRESSÃO 3D + INTELIGÊNCIA ARTIFICIAL (15 CAPÍTULOS)</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #0f172a; color: #e2e8f0; line-height: 1.8; }
        .ebook-container { max-width: 950px; margin: 40px auto; background: #1e293b; padding: 60px; border-radius: 16px; box-shadow: 0 20px 40px rgba(0,0,0,0.5); border: 1px solid #334155; }
        .hero-banner { background: linear-gradient(135deg, #0284c7 0%, #0f766e 100%); color: #ffffff; padding: 50px; border-radius: 12px; margin-bottom: 40px; border: 1px solid #38bdf8; }
        h1 { font-weight: 800; font-size: 2.4rem; letter-spacing: -0.5px; }
        h2 { font-weight: 700; color: #38bdf8; margin-top: 45px; border-bottom: 2px solid #334155; padding-bottom: 10px; }
        h3 { font-weight: 600; color: #f1f5f9; margin-top: 25px; }
        .highlight-box { background-color: rgba(14, 165, 233, 0.1); border-left: 4px solid #38bdf8; padding: 20px; border-radius: 8px; margin: 25px 0; border: 1px solid rgba(56, 189, 248, 0.2); }
        .alert-box { background-color: rgba(239, 68, 68, 0.1); border-left: 4px solid #ef4444; padding: 20px; border-radius: 8px; margin: 25px 0; border: 1px solid rgba(239, 68, 68, 0.2); }
        .code-block { background-color: #090d16; font-family: 'JetBrains Mono', monospace; color: #38bdf8; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; font-size: 0.9rem; }
        .btn-download { background-color: #10b981; color: white; font-weight: 700; padding: 14px 28px; border-radius: 8px; text-decoration: none; border: none; font-size: 1.1rem; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4); }
        .btn-download:hover { background-color: #059669; color: white; }
        .tech-table { border-color: #334155; color: #cbd5e1; }
        .tech-table th { background-color: #0f172a; color: #38bdf8; }
        .toc-box { background: #090d16; border: 1px solid #0284c7; padding: 25px; border-radius: 12px; margin-bottom: 40px; }
        .toc-box a { color: #38bdf8; text-decoration: none; font-weight: 600; }
        .toc-box a:hover { text-decoration: underline; color: #ffffff; }
        @media print {
            .no-print { display: none !important; }
            body { background-color: #ffffff; color: #000000; }
            .ebook-container { background: #ffffff; color: #000000; box-shadow: none; border: none; padding: 0; margin: 0; }
            h2 { color: #0284c7; border-color: #ccc; }
            .toc-box { background: #f8fafc; border-color: #ccc; }
            .toc-box a { color: #0284c7; }
        }
    </style>
</head>
<body>
    <div class="text-center my-4 no-print">
        <button onclick="window.print()" class="btn-download"><i class="fa-solid fa-file-pdf me-2"></i> Baixar / Imprimir Apostila Completa em PDF</button>
    </div>

    <div class="ebook-container">
        <div class="hero-banner text-center">
            <span class="badge bg-dark text-info mb-2 font-monospace border border-info">MANUAL COMPLETO // EDICAO DE REFERENCIA (15 CAPITULOS)</span>
            <h1>GUIA DEFINITIVO: IMPRESSÃO 3D + INTELIGÊNCIA ARTIFICIAL</h1>
            <p class="lead mb-0 text-light">Engenharia de Prompts, Troubleshooting de Oficina, Fatiamento Avançado e Monetização Massiva</p>
        </div>

        <div class="d-flex justify-content-between text-muted mb-4 fs-6">
            <span><strong>Autor:</strong> Daniel Rodrigues & Daniel AI Matrix</span>
            <span><strong>Páginas Estimadas:</strong> 15 a 20 Páginas (Formatado)</span>
        </div>

        <!-- ÍNDICE NAVEGÁVEL -->
        <div class="toc-box">
            <h4 class="text-info fw-bold mb-3"><i class="fa-solid fa-list-ol me-2"></i>Sumário Geral dos 15 Capítulos:</h4>
            <div class="row">
                <div class="col-md-6">
                    <ol>
                        <li><a href="#cap1">A Revolução da IA Generativa na Impressão 3D</a></li>
                        <li><a href="#cap2">Engenharia de Prompts para Geometrias 3D</a></li>
                        <li><a href="#cap3">O Fluxo Completo: Do Conceito 2D à Matriz 3D</a></li>
                        <li><a href="#cap4">Validação de Malhas e Reparo de Geometrias</a></li>
                        <li><a href="#cap5">Engenharia de Fatiamento FDM Avançada</a></li>
                        <li><a href="#cap6">Engenharia de Fatiamento para Resina (SLA/DLP)</a></li>
                        <li><a href="#cap7">Troubleshooting Prático: Warping e Adesão</a></li>
                        <li><a href="#cap8">Desentupimento de Bico e Cold Pull</a></li>
                    </ol>
                </div>
                <div class="col-md-6">
                    <ol start="9">
                        <li><a href="#cap9">Otimização de Qualidade via Visão Computacional</a></li>
                        <li><a href="#cap10">Materiais Avançados (PLA, PETG, ABS, TPU, Nylon)</a></li>
                        <li><a href="#cap11">Pós-Processamento e Acabamento Profissional</a></li>
                        <li><a href="#cap12">Modelagem Paramétrica Otimizada para Peças</a></li>
                        <li><a href="#cap13">Automação de Print Farms (Klipper/OctoPrint)</a></li>
                        <li><a href="#cap14">Estratégias de Venda e Precificação Massiva</a></li>
                        <li><a href="#cap15">O Futuro dos Modelos Fundacionais 3D</a></li>
                    </ol>
                </div>
            </div>
        </div>

        <hr class="border-secondary">

        <!-- CONTEÚDO DOS CAPÍTULOS -->
        <div id="cap1">
            <h2>Capítulo 1: A Revolução da IA Generativa na Impressão 3D</h2>
            <p>A impressão 3D tradicional dependia exclusivamente da criação manual em softwares como Blender, Fusion 360 ou ZBrush. A IA Generativa elimina esse gargalo, permitindo converter texto e imagem em malhas 3D prontas para fatiamento em questão de minutos.</p>
        </div>

        <div id="cap2">
            <h2>Capítulo 2: Engenharia de Prompts para Geometrias 3D</h2>
            <p>Aprenda a estruturar prompts que geram topologia limpa, bases planas e ausência de balanços críticos (overhangs).</p>
            <div class="code-block my-2">
                Prompt Exemplo: "Parametric mechanical bracket, clean topology, watertight manifold STL, flat mounting base, no overhangs, high resolution 3d model."
            </div>
        </div>

        <div id="cap3">
            <h2>Capítulo 3: O Fluxo Completo: Do Conceito 2D à Matriz 3D</h2>
            <p>Como integrar Midjourney / DALL-E para criar imagens 2D limpas em fundo branco e convertê-las em modelos 3D usando <strong>Hunyuan3D, Tripo3D e Meshy</strong>.</p>
        </div>

        <div id="cap4">
            <h2>Capítulo 4: Validação de Malhas e Reparo de Geometrias</h2>
            <p>Procedimentos para corrigir furos na malha, normais invertidas e garantir que a peça seja <em>Watertight</em> e <em>Manifold</em> usando Autodesk Netfabb e 3D Builder.</p>
        </div>

        <div id="cap5">
            <h2>Capítulo 5: Engenharia de Fatiamento FDM Avançada</h2>
            <p>Configuração de perímetros, padrões de preenchimento (Gyroid x Grid), altura de camada adaptativa e calibração de fluxo (Flow Rate) no Cura, PrusaSlicer e Bambu Studio.</p>
        </div>

        <div id="cap6">
            <h2>Capítulo 6: Engenharia de Fatiamento para Resina (SLA/DLP/LCD)</h2>
            <p>Técnicas de esvaziamento (Hollow), criação de furos de drenagem para evitar efeito ventosa e posicionamento de suportes em ângulos de 45°.</p>
        </div>

        <div id="cap7">
            <h2>Capítulo 7: Troubleshooting Prático: Warping e Adesão</h2>
            <div class="alert-box">
                <h5>Como Eliminar o Warping em Impressões FDM:</h5>
                <p>1. Ajuste fino do Z-Offset na primeira camada.<br>2. Calibração da temperatura da mesa (PLA: 60°C | PETG: 80°C | ABS: 105°C).<br>3. Uso de aditivos de adesão (PVP/Spray) e ativação de Brim de 8mm no fatiador.</p>
            </div>
        </div>

        <div id="cap8">
            <h2>Capítulo 8: Desentupimento de Bico e Cold Pull</h2>
            <div class="highlight-box">
                <h5>Passo a Passo do Cold Pull (Puxada a Frio):</h5>
                <p>Aqueça o hotend a 210°C, insira o filamento, deixe esfriar até 90°C (PLA) e puxe com firmeza para expelir toda a sujeira incrustada no bico.</p>
            </div>
        </div>

        <div id="cap9">
            <h2>Capítulo 9: Otimização de Qualidade via Visão Computacional</h2>
            <p>Como tirar fotos de falhas na peça e usar prompts de visão em modelos de IA para receber os parâmetros exatos de correção no fatiador.</p>
        </div>

        <div id="cap10">
            <h2>Capítulo 10: Materiais Avançados (PLA, PETG, ABS, TPU, Nylon)</h2>
            <p>Propriedades mecânicas, resistência térmica, absorção de umidade e requisitos de secagem para cada tipo de filamento técnico.</p>
        </div>

        <div id="cap11">
            <h2>Capítulo 11: Pós-Processamento e Acabamento Profissional</h2>
            <p>Técnicas de lixamento progressivo, primer preenchedor, banho de vapor de acetona para ABS e pintura com aerógrafo.</p>
        </div>

        <div id="cap12">
            <h2>Capítulo 12: Modelagem Paramétrica Otimizada para Peças</h2>
            <p>Como usar scripts em Python e OpenSCAD combinados com IA para gerar peças personalizadas em lote com dimensões exatas.</p>
        </div>

        <div id="cap13">
            <h2>Capítulo 13: Automação de Print Farms (Klipper/OctoPrint)</h2>
            <p>Configuração de servidores de impressão remota, câmeras com detecção de falha por IA (Obico/Spaghetti Detective) e envio automático de arquivos.</p>
        </div>

        <div id="cap14">
            <h2>Capítulo 14: Estratégias de Venda e Precificação Massiva</h2>
            <p>Fórmula de cálculo de custo por hora de máquina + grama de filamento + margem de lucro, e posicionamento de arquivos no Cults3D, CGTrader e Kiwify.</p>
        </div>

        <div id="cap15">
            <h2>Capítulo 15: O Futuro dos Modelos Fundacionais 3D</h2>
            <p>Para onde caminha a tecnologia de inteligência artificial espacial, geração nativa em voxel e o impacto na manufatura aditiva global.</p>
        </div>

        <div class="text-center mt-5 text-muted">
            <p class="mb-1">DANIEL AI MATRIX — SISTEMA AUTÔNOMO DE CONTEÚDO E VENDAS</p>
            <small>© Todos os direitos reservados. Daniel Rodrigues.</small>
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
        body {{ background-color: #030712; color: #38bdf8; font-family: 'Rajdhani', sans-serif; }}
        .hud-card {{ background: rgba(15, 23, 42, 0.85); border: 1px solid #0284c7; box-shadow: 0 0 15px rgba(2, 132, 199, 0.25); border-radius: 8px; }}
        .cyber-brain-canvas {{ position: relative; width: 100%; height: 380px; background: radial-gradient(circle, rgba(14,165,233,0.12) 0%, rgba(3,7,18,0.95) 80%); border: 1px solid #0284c7; border-radius: 12px; overflow: hidden; }}
        .cyber-node {{ position: absolute; width: 70px; height: 70px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.6rem; color: #00f0ff; cursor: pointer; background: rgba(15, 23, 42, 0.9); border: 2px solid #00f0ff; box-shadow: 0 0 15px #00f0ff; }}
        .cyber-node-main {{ width: 90px; height: 90px; font-size: 2.2rem; color: #ff007f; border-color: #ff007f; box-shadow: 0 0 25px #ff007f; }}
        .hud-drawer {{ position: fixed; top: 0; right: -420px; width: 400px; height: 100vh; background: rgba(3, 7, 18, 0.95); border-left: 2px solid #00f0ff; box-shadow: -10px 0 30px rgba(0, 240, 255, 0.3); z-index: 9999; transition: right 0.4s; padding: 25px; overflow-y: auto; }}
        .hud-drawer.active {{ right: 0; }}
        .badge-neon {{ background: rgba(0, 240, 255, 0.1); color: #00f0ff; border: 1px solid #00f0ff; padding: 4px 10px; border-radius: 4px; }}
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
                <a href="/ebook/download" target="_blank" class="btn btn-sm btn-success fw-bold"><i class="fa-solid fa-book me-1"></i> Ver Apostila (15 Capítulos)</a>
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
                        <div class="cyber-node cyber-node-main" style="top: 50%; left: 50%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('CÉREBRO MATRIZ (DANIEL AI)', 'Orquestrador Neural', 'OPERACIONAL', 'Coordenando fluxo de vendas Kiwify e entrega da apostila completa de 15 capítulos.', ['Matriz iniciada', 'Apostila completa publicada em /ebook/download'])">
                            <i class="fa-solid fa-brain"></i>
                        </div>

                        <div class="cyber-node" style="top: 30%; left: 20%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('GATEWAY FINANCIAL (KIWIFY)', 'Agente de Capital', 'MONITORANDO WEBHOOK', 'Escutando /webhook/kiwify para crédito imediato.', ['Webhook 200 OK', 'Pronto para novas transações'])">
                            <i class="fa-solid fa-bolt"></i>
                        </div>

                        <div class="cyber-node" style="top: 30%; left: 80%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('SUB-AGENTE AUTOR (APOSTILA)', 'Gerador de Conteúdo', 'APOSTILA 15 CAPÍTULOS ATIVA', 'Manual completo de Impressão 3D + IA ativo na rota /ebook/download.', ['15 capítulos compilados com sucesso', 'Apostila profissional liberada aos alunos'])">
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
        function abrirInspector(nome, tipo, status, acao, logs) {{
            document.getElementById('drawer-nome').innerText = nome;
            document.getElementById('drawer-tipo').innerText = tipo;
            document.getElementById('drawer-status').innerText = status;
            document.getElementById('drawer-acao').innerText = acao;
            document.getElementById('hudDrawer').classList.add('active');
        }}
        function fecharInspector() {{
            document.getElementById('hudDrawer').classList.remove('active');
        }}
    </script>
</body>
</html>
"""

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
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
