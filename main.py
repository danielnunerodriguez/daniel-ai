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
                "status": "E-BOOK AVANÇADO PUBLICADO",
                "acao": "Manual Técnico Profissional compilado na rota /ebook/download.",
                "logs": ["Guia prático de depuração, Warping, Desentupimento e IA adicionado", "Download em PDF habilitado"],
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

# CONTEÚDO COMPLETO E PROFUNDO DO E-BOOK
EBOOK_HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MANUAL TÉCNICO: IMPRESSÃO 3D + INTELIGÊNCIA ARTIFICIAL</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #0f172a; color: #e2e8f0; line-height: 1.8; }
        .ebook-container { max-width: 900px; margin: 40px auto; background: #1e293b; padding: 50px; border-radius: 16px; box-shadow: 0 20px 40px rgba(0,0,0,0.5); border: 1px solid #334155; }
        .hero-banner { background: linear-gradient(135deg, #0284c7 0%, #0f766e 100%); color: #ffffff; padding: 45px; border-radius: 12px; margin-bottom: 40px; border: 1px solid #38bdf8; }
        h1 { font-weight: 800; font-size: 2.3rem; letter-spacing: -0.5px; }
        h2 { font-weight: 700; color: #38bdf8; margin-top: 40px; border-bottom: 2px solid #334155; padding-bottom: 10px; }
        h3 { font-weight: 600; color: #f1f5f9; margin-top: 25px; }
        .highlight-box { background-color: rgba(14, 165, 233, 0.1); border-left: 4px solid #38bdf8; padding: 20px; border-radius: 8px; margin: 25px 0; border: 1px solid rgba(56, 189, 248, 0.2); }
        .alert-box { background-color: rgba(239, 68, 68, 0.1); border-left: 4px solid #ef4444; padding: 20px; border-radius: 8px; margin: 25px 0; border: 1px solid rgba(239, 68, 68, 0.2); }
        .code-block { background-color: #090d16; font-family: 'JetBrains Mono', monospace; color: #38bdf8; padding: 15px; border-radius: 8px; border: 1px solid #1e293b; font-size: 0.9rem; }
        .btn-download { background-color: #10b981; color: white; font-weight: 700; padding: 14px 28px; border-radius: 8px; text-decoration: none; border: none; font-size: 1.1rem; box-shadow: 0 4px 14px rgba(16, 185, 129, 0.4); }
        .btn-download:hover { background-color: #059669; color: white; }
        .tech-table { border-color: #334155; color: #cbd5e1; }
        .tech-table th { background-color: #0f172a; color: #38bdf8; }
        @media print {
            .no-print { display: none !important; }
            body { background-color: #ffffff; color: #000000; }
            .ebook-container { background: #ffffff; color: #000000; box-shadow: none; border: none; padding: 0; margin: 0; }
            h2 { color: #0284c7; border-color: #ccc; }
            .highlight-box { background: #f0f9ff; border-left-color: #0284c7; color: #000; }
            .code-block { background: #f8fafc; color: #0284c7; border-color: #ccc; }
        }
    </style>
</head>
<body>
    <div class="text-center my-4 no-print">
        <button onclick="window.print()" class="btn-download"><i class="fa-solid fa-file-pdf me-2"></i> Baixar / Imprimir Manual em PDF</button>
    </div>

    <div class="ebook-container">
        <!-- CAPA -->
        <div class="hero-banner text-center">
            <span class="badge bg-dark text-info mb-2 font-monospace border border-info">MANUAL DE ENGENHARIA DE IMPRESSÃO 3D + IA</span>
            <h1>GUIA DEFINITIVO: MODELAGEM, TROUBLESHOOTING E MONETIZAÇÃO COM IA</h1>
            <p class="lead mb-0 text-light">Soluções para Falhas de Impressão, Criação 2D-para-3D e Calibração por Visão Computacional</p>
        </div>

        <div class="d-flex justify-content-between text-muted mb-4 fs-6">
            <span><strong>Autor:</strong> Daniel Rodrigues & Daniel AI Matrix</span>
            <span><strong>Versão:</strong> 2.0 (Avançado)</span>
        </div>

        <hr class="border-secondary">

        <!-- MÓDULO 1 -->
        <h2>Módulo 1: O Fluxo Integrado de Criação (Imagem 2D ➔ Modelo 3D via IA)</h2>
        <p>Criar arquivos 3D a partir do zero não exige mais domínio complexo de CAD. O fluxo moderno utiliza IAs geradoras de imagem para definir o conceito e plataformas 3D por IA para sintetizar a geometria tridimensional pronta para impressão.</p>

        <h3>Etapa 1: Gerando a Imagem de Referência Otimizada (2D)</h3>
        <p>Para obter modelos 3D limpos em IAs como <strong>Hunyuan3D, Tripo3D ou Meshy</strong>, a imagem de origem deve seguir parâmetros rígidos:</p>
        <ul>
            <li>Fundo neutro e isolado (de preferência branco ou transparente).</li>
            <li>Iluminação homogênea sem sombras duras que possam confundir a profundidade.</li>
            <li>Vista em perspectiva isométrica ou visão frontal plana.</li>
        </ul>

        <div class="code-block my-3">
            <strong>Prompt Exemplo (Midjourney / DALL-E 3 / Leonardo AI):</strong><br>
            "A clean 3D isometric concept of a mechanical cable organizer gear, studio lighting, isolated on solid white background, high contrast, clean vector style, orthographic view --no shadows"
        </div>

        <h3>Etapa 2: Importação e Conversão no Gerador 3D</h3>
        <ol>
            <li>Acesse a plataforma de IA 3D de sua preferência (ex: <strong>Hunyuan3D / Tripo3D</strong>).</li>
            <li>Faça o upload da imagem 2D gerada na etapa anterior no módulo <em>Image-to-3D</em>.</li>
            <li>Ajuste a densidade do polígono (Polycount) para nível Médio/Alto para preservar os detalhes funcionais.</li>
            <li>Exporte o arquivo resultante no formato <strong>.STL</strong> ou <strong>.OBJ</strong>.</li>
        </ol>

        <!-- MÓDULO 2 -->
        <h2>Módulo 2: Resolução de Falhas Críticas de Impressão (Troubleshooting)</h2>
        <p>Mesmo com uma boa modelagem, falhas físicas na impressora 3D podem inutilizar a peça. Abaixo estão os procedimentos exatos para diagnosticar e corrigir as duas principais falhas de oficinas 3D.</p>

        <h3>1. Como Diagnosticar e Corrigir o WARPING (Descolamento das Bordas)</h3>
        <p>O <em>Warping</em> ocorre quando o plástico esfria de forma desigual, encolhe e puxa as extremidades da peça para cima, soltando-a da mesa de impressão.</p>

        <div class="alert-box">
            <h5 class="text-danger fw-bold"><i class="fa-solid fa-triangle-exclamation me-2"></i>Passos Obrigatórios para Eliminar o Warping:</h5>
            <ol class="mb-0">
                <li><strong>Calibração do Z-Offset (Primeira Camada):</strong> Garanta que o bico esteja levemente esmagando o filamento sobre a mesa. Se o fio de plástico ficar redondo em vez de achatado, o Z-Offset está muito alto.</li>
                <li><strong>Temperatura Correta da Mesa (Bed Temp):</strong>
                    <ul>
                        <li><strong>PLA:</strong> 55°C a 65°C</li>
                        <li><strong>PETG:</strong> 70°C a 85°C</li>
                        <li><strong>ABS/TRITAN:</strong> 100°C a 110°C (Exige impressora fechada/enclosure).</li>
                    </ul>
                </li>
                <li><strong>Uso de Aditivos de Adesão:</strong> Aplique cola bastão (PVP) ou spray de fixação próprio para impressão 3D na mesa limpa com álcool isopropílico (IPA 99%).</li>
                <li><strong>Adição de Brim no Fatiador:</strong> Ative a borda de adesão (<em>Brim</em>) com largura de 5mm a 10mm no fatiador para aumentar a área de contato com a mesa.</li>
                <li><strong>Correntes de Ar:</strong> Desligue ventiladores de ambiente próximos à impressora e desative o cooler de peça nas primeiras 3 camadas.</li>
            </ol>
        </div>

        <h3>2. Como Resolver Bico Entupido (Nozzle Clog) e Sub-extrusão</h3>
        <p>O entupimento pode ocorrer por acúmulo de resíduos, filamento de má qualidade ou retenção de calor acima do gargalo (<em>Heat Creep</em>).</p>

        <div class="highlight-box">
            <h5 class="text-info fw-bold"><i class="fa-solid fa-wrench me-2"></i>Técnica Eficiente: Puxada a Frio (Cold Pull / Atomic Pull)</h5>
            <p>Este método remove resíduos carbonizados de dentro do Bico/Hotend sem precisar desmontar o conjunto:</p>

            <ol>
                <li>Aqueça o hotend até a temperatura de fusão do filamento atual (ex: 210°C para PLA ou 240°C para PETG).</li>
                <li>Empurre manualmente um pedaço de filamento (preferencialmente Nylon ou PLA claro) até sair um pouco pelo bico.</li>
                <li>Desligue o aquecimento e deixe o hotend esfriar até cerca de <strong>90°C (para PLA)</strong> ou <strong>130°C (para Nylon)</strong>.</li>
                <li>Com o plástico no estado semi-sólido, puxe o filamento firmemente para cima.</li>
                <li>O filamento sairá com o exato formato interno do bico, trazendo toda a sujeira incrustada. Repita até a ponta sair limpa.</li>
            </ol>
            <p class="mb-0"><strong>Dica extra:</strong> Use uma micro-agulha de 0.4mm aquecida inserida por baixo do bico para desobstruir partículas maiores antes do Cold Pull.</p>
        </div>

        <!-- MÓDULO 3 -->
        <h2>Módulo 3: Utilizando Inteligência Artificial para Maximizar a Qualidade</h2>
        <p>Você pode transformar modelos de IA avançados (como o ChatGPT Plus / Groq Vision) em um **Engenheiro de Fatiamento Pessoal** para ajustar os parâmetros da sua impressora.</p>

        <h3>Diagnóstico por Imagem e Visão Computacional</h3>
        <p>Ao se deparar com uma falha visual na peça impresso (ex: teias de aranha / *stringing*, linhas desalinhadas ou falta de preenchimento):</p>
        <ol>
            <li>Tire uma foto bem iluminada e aproximada (Macro) do defeito da peça.</li>
            <li>Envie a foto para a IA acompanhada do prompt de diagnóstico técnico.</li>
        </ol>

        <div class="code-block my-3">
            <strong>Prompt Mestre para Diagnóstico de Impressão 3D:</strong><br>
            "Atue como um Engenheiro Especialista em Impressão 3D e Fatiamento FDM. Analise esta foto da minha impressão. Identifique se o defeito é Stringing, Overheating, Ghosting ou Under-extrusion. Indique os 3 parâmetros exatos do fatiador (Cura/PrusaSlicer/Bambu) que devo alterar (ex: Distância de Retração, Velocidade, Fluxo ou Temperatura) para solucionar o problema."
        </div>

        <!-- MÓDULO 4 -->
        <h2>Módulo 4: Tabela de Referência Rápida de Parâmetros</h2>
        <table class="table table-bordered tech-table my-3">
            <thead>
                <tr>
                    <th>Sintoma Visual</th>
                    <th>Causa Provável</th>
                    <th>Ação Corretiva no Fatiador / Hardware</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Bordas soltando da mesa</strong></td>
                    <td>Falta de adesão / Resfriamento rápido</td>
                    <td>Aumentar mesa em +5°C, usar Brim 8mm, aplicar cola PVP.</td>
                </tr>
                <tr>
                    <td><strong>Teias de aranha (Stringing)</strong></td>
                    <td>Retração insuficiente ou Bico muito quente</td>
                    <td>Aumentar distância de retração ( DirectDrive: 0.8-1.5mm | Bowden: 4-6mm ) e baixar temp em 5°C.</td>
                </tr>
                <tr>
                    <td><strong>Falhas no meio das camadas</strong></td>
                    <td>Sub-extrusão ou Bico parcialmente entupido</td>
                    <td>Executar Cold Pull, calibrar os E-Steps do Extrusor e checar vazamento no gargalo.</td>
                </tr>
                <tr>
                    <td><strong>Camadas desalinhadas (Layer Shift)</strong></td>
                    <td>Correias frouxas ou motor superaquecido</td>
                    <td>Esticar correias dos eixos X/Y e checar tensão V-Ref dos drivers na placa.</td>
                </tr>
            </tbody>
        </table>

        <!-- CONCLUSÃO -->
        <div class="highlight-box border-success text-light mt-5">
            <h5 class="text-success fw-bold"><i class="fa-solid fa-circle-check me-2"></i>Conclusão do Manual:</h5>
            <p class="mb-0">Integrar o diagnóstico por IA com o domínio do troubleshooting físico transforma seu estúdio de impressão 3D em uma operação de alta eficiência, reduzindo o desperdício de filamento a zero e garantindo peças com padrão profissional prontas para venda imediata.</p>
        </div>

        <div class="text-center mt-5 text-muted">
            <p class="mb-1">DANIEL AI MATRIX — SISTEMA AUTÔNOMO DE GERAÇÃO E ENTREGA DE CONTEÚDO</p>
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
        body {{
            background-color: #030712; color: #38bdf8; font-family: 'Rajdhani', sans-serif;
            background-image: radial-gradient(rgba(14, 165, 233, 0.15) 1px, transparent 0), radial-gradient(rgba(14, 165, 233, 0.1) 1px, #030712 100%);
            background-size: 24px 24px, 100% 100%; overflow-x: hidden;
        }}
        .hud-card {{
            background: rgba(15, 23, 42, 0.85); border: 1px solid #0284c7;
            box-shadow: 0 0 15px rgba(2, 132, 199, 0.25); border-radius: 8px; backdrop-filter: blur(8px);
        }}
        .cyber-brain-canvas {{
            position: relative; width: 100%; height: 380px;
            background: radial-gradient(circle, rgba(14,165,233,0.12) 0%, rgba(3,7,18,0.95) 80%);
            border: 1px solid #0284c7; border-radius: 12px; overflow: hidden;
        }}
        .cyber-node {{
            position: absolute; width: 70px; height: 70px; border-radius: 50%;
            display: flex; align-items: center; justify-content: center; font-size: 1.6rem;
            color: #00f0ff; cursor: pointer; z-index: 5; transition: all 0.3s;
            background: rgba(15, 23, 42, 0.9); border: 2px solid #00f0ff; box-shadow: 0 0 15px #00f0ff;
        }}
        .cyber-node-main {{ width: 90px; height: 90px; font-size: 2.2rem; color: #ff007f; border-color: #ff007f; box-shadow: 0 0 25px #ff007f; }}
        .hud-drawer {{
            position: fixed; top: 0; right: -420px; width: 400px; height: 100vh;
            background: rgba(3, 7, 18, 0.95); border-left: 2px solid #00f0ff;
            box-shadow: -10px 0 30px rgba(0, 240, 255, 0.3); z-index: 9999;
            transition: right 0.4s; padding: 25px; overflow-y: auto;
        }}
        .hud-drawer.active {{ right: 0; }}
        .badge-neon {{ background: rgba(0, 240, 255, 0.1); color: #00f0ff; border: 1px solid #00f0ff; padding: 4px 10px; border-radius: 4px; }}
        svg.connections {{ position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; pointer-events: none; }}
        .line-glow {{ stroke: #00f0ff; stroke-width: 2; stroke-dasharray: 6 4; }}
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
                <a href="/ebook/download" target="_blank" class="btn btn-sm btn-success fw-bold"><i class="fa-solid fa-book me-1"></i> Ver Manual Avançado</a>
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
                             onclick="abrirInspector('CÉREBRO MATRIZ (DANIEL AI)', 'Orquestrador Neural', 'OPERACIONAL', 'Coordenando fluxo de vendas Kiwify e entrega do manual técnico.', ['Matriz iniciada', 'Manual técnico atualizado em /ebook/download'])">
                            <i class="fa-solid fa-brain"></i>
                        </div>

                        <div class="cyber-node" style="top: 30%; left: 20%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('GATEWAY FINANCIAL (KIWIFY)', 'Agente de Capital', 'MONITORANDO WEBHOOK', 'Escutando /webhook/kiwify para crédito imediato.', ['Webhook 200 OK', 'Pronto para novas transações'])">
                            <i class="fa-solid fa-bolt"></i>
                        </div>

                        <div class="cyber-node" style="top: 30%; left: 80%; transform: translate(-50%, -50%);"
                             onclick="abrirInspector('SUB-AGENTE AUTOR (E-BOOK)', 'Gerador de Conteúdo', 'MANUAL TÉCNICO V2.0 ATIVO', 'Guia avançado de Impressão 3D + IA ativo na rota /ebook/download.', ['Cold Pull, Warping e Visão Computacional compilados', 'Ativo para clientes'])">
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
