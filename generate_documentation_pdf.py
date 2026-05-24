# -*- coding: utf-8 -*-
import os
import sys

# Garante saída UTF-8 no console
sys.stdout.reconfigure(encoding='utf-8')

try:
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.pdfgen import canvas
except ImportError:
    print("Erro: A biblioteca reportlab não está instalada. Por favor, rode 'pip install reportlab' antes de executar este script.")
    sys.exit(1)

# Dimensões da Página A4 Retrato
PAGE_WIDTH, PAGE_HEIGHT = A4

class ABNTCanvas(canvas.Canvas):
    """
    Canvas personalizado para numeração de páginas no canto superior direito,
    de acordo com as normas da ABNT, omitindo na primeira folha (Capa).
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.pages = []
        
    def showPage(self):
        self.pages.append(dict(self.__dict__))
        self._startPage()
        
    def save(self):
        page_count = len(self.pages)
        for page in self.pages:
            self.__dict__.update(page)
            self.draw_abnt_decorations(page_count)
            super().showPage()
        super().save()
        
    def draw_abnt_decorations(self, total_pages):
        self.saveState()
        
        # Normas ABNT: Numeração começa a aparecer no topo direito a partir da pág 2 (Introdução)
        if self._pageNumber > 1:
            self.setFont("Times-Roman", 10)
            self.setFillColor(colors.black)
            # Margem direita 2cm (56.7pt)
            self.drawRightString(PAGE_WIDTH - 56.7, PAGE_HEIGHT - 40, str(self._pageNumber))
            
        self.restoreState()

def build_pdf(filename):
    # Configuração de Margens Estritas ABNT (3cm Esquerda/Superior, 2cm Direita/Inferior)
    # 1cm = 28.35 pontos
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=85.05,   # 3cm
        rightMargin=56.7,   # 2cm
        topMargin=85.05,    # 3cm
        bottomMargin=56.7   # 2cm
    )
    
    styles = getSampleStyleSheet()
    
    # Cores Harmoniosas ABNT
    border_gray = colors.HexColor("#CCCCCC")
    text_dark = colors.HexColor("#000000")
    green_accent = colors.HexColor("#0b592e")
    yellow_bg = colors.HexColor("#FFFDF0")
    yellow_border = colors.HexColor("#D4AF37")
    
    # Estilos Acadêmicos Baseados em Times-Roman (Norma NBR 14724)
    styles.add(ParagraphStyle(
        name='ABNTCapaCentro',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=14,
        leading=18,
        textColor=text_dark,
        alignment=1, # Centralizado
        spaceAfter=12
    ))
    
    styles.add(ParagraphStyle(
        name='ABNTH1',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=12,
        leading=16,
        textColor=text_dark,
        spaceBefore=18,
        spaceAfter=10,
        keepWithNext=True
    ))

    styles.add(ParagraphStyle(
        name='ABNTH2',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=11,
        leading=14,
        textColor=text_dark,
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    ))
    
    styles.add(ParagraphStyle(
        name='ABNTP',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=11,
        leading=16.5, # Espaçamento 1.5
        textColor=text_dark,
        firstLineIndent=35.4, # Recuo de parágrafo 1.25cm
        alignment=4, # Justificado
        spaceAfter=8
    ))
    
    styles.add(ParagraphStyle(
        name='ABNTCitacaoLonga',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9.5,
        leading=11.4, # Espaçamento simples
        textColor=colors.HexColor("#222222"),
        leftIndent=113.4, # Recuo de 4cm à esquerda
        alignment=4, # Justificado
        spaceAfter=12
    ))
    
    styles.add(ParagraphStyle(
        name='ABNTExemploTitulo',
        parent=styles['Normal'],
        fontName='Times-Bold',
        fontSize=9.5,
        leading=12,
        textColor=colors.HexColor("#8A6D3B")
    ))
    
    styles.add(ParagraphStyle(
        name='ABNTExemploCorpo',
        parent=styles['Normal'],
        fontName='Times-Roman',
        fontSize=9,
        leading=12.5,
        textColor=text_dark
    ))

    story = []
    
    # ------------------ FOLHA DE CAPA (ABNT) ------------------
    story.append(Spacer(1, 20))
    story.append(Paragraph("PREFEITURA MUNICIPAL DE ENSINO<br/>SECRETARIA MUNICIPAL DE EDUCAÇÃO<br/>ITINERÁRIO EXTENSIONISTA DOCENTE", styles['ABNTCapaCentro']))
    
    story.append(Spacer(1, 140))
    story.append(Paragraph("ITINERÁRIO EXTENSIONISTA DE CAPACITAÇÃO E LITERACIA DIGITAL ESCOLAR EM PLANILHAS ELETRÔNICAS", styles['ABNTCapaCentro']))
    story.append(Spacer(1, 15))
    story.append(Paragraph("<font size='11'><i>FONTES DE CONSULTA PERMANENTE EM MICROSOFT EXCEL 365<br/>(VERSÃO RESUMIDA EM PADRÃO ABNT ACADÊMICO)</i></font>", ParagraphStyle('SubCapa', parent=styles['ABNTCapaCentro'], fontName='Times-Roman', fontSize=11)))
    
    story.append(Spacer(1, 140))
    story.append(Paragraph("AUTORIA PEDAGÓGICA: JULIANO PRIANTI<br/>(Docente Idealizador e Autor do Itinerário)<br/><br/>DESENVOLVIMENTO & TI: GABRIEL H. RODRIGUES<br/>(Suporte Técnico e Infraestrutura Virtual)", ParagraphStyle('Autores', parent=styles['ABNTCapaCentro'], fontName='Times-Roman', fontSize=10, leading=14)))
    
    story.append(Spacer(1, 120))
    story.append(Paragraph("REDE MUNICIPAL DE ENSINO — BRASIL<br/>2026", styles['ABNTCapaCentro']))
    story.append(PageBreak())
    
    # ------------------ CAPÍTULO 1: INTRODUÇÃO ------------------
    story.append(Paragraph("CAPÍTULO 1 — INTRODUÇÃO E ROTEIRO PEDAGÓGICO", styles['ABNTH1']))
    story.append(Paragraph("O presente itinerário de literacia digital escolar descreve uma abordagem ativa de capacitação de professores da rede pública em planilhas eletrônicas. O desenvolvimento deste programa tem como intuito sanar os gargalos de digitação manual de boletins e pautas físicas, otimizando o trabalho extraclasse.", styles['ABNTP']))
    story.append(Paragraph("A metodologia une a teoria conceitual com a experimentação laboratorial prática e interativa em um simulador integrado de Microsoft Excel 365.", styles['ABNTP']))
    
    story.append(Paragraph("O projeto apoia-se no resgate de tempo produtivo do professor para focar na atenção individualizada aos alunos em sala, servindo como uma fonte de consulta eterna para o desenvolvimento profissional contínuo dos docentes municipais.", styles['ABNTP']))
    
    # Citação Longa ABNT
    story.append(Paragraph("A literacia de dados no contexto escolar não é um mero aprendizado instrumental. Trata-se da emancipação técnica necessária para que o professor transforme planilhas estáticas em ferramentas vivas de diagnóstico pedagógico, resgatando educandos sob risco de exclusão escolar. (PRIANTI, 2026, p. 14)", styles['ABNTCitacaoLonga']))
    story.append(Spacer(1, 10))
    
    # ------------------ CAPÍTULO 2: PODER DO EXCEL ------------------
    story.append(Paragraph("CAPÍTULO 2 — O PODER DAS PLANILHAS NA PRÁTICA DOCENTE", styles['ABNTH1']))
    story.append(Paragraph("O domínio técnico do Microsoft Excel confere ao educador uma autonomia sem precedentes na gestão de dados escolares, pautada em três pilares fundamentais:", styles['ABNTP']))
    
    story.append(Paragraph("1. <b>Otimização de Tempo:</b> A realização automática de somas, médias e contagens de frequências remove a necessidade de calculadoras externas e planilhas de rascunhos, evitando retrabalho e prevenindo o esgotamento mental do professor.", styles['ABNTP']))
    story.append(Paragraph("2. <b>Pedagogia Baseada em Dados:</b> O acompanhamento sistemático de avaliações permite mapear descritores de aprendizagem com baixos desempenhos de acertos de forma coletiva ou individual.", styles['ABNTP']))
    story.append(Paragraph("3. <b>Automação e Desburocratização:</b> Geração instantânea de boletins, atas de conselho de classe e planilhas de chamada de forma padronizada, agilizando repasses legais às secretarias municipais.", styles['ABNTP']))
    story.append(PageBreak())
    
    # ------------------ CONTEÚDO DOS 10 TÓPICOS TÉCNICOS COM 3 EXEMPLOS CADA ------------------
    
    topics = [
        {
            "id": 1,
            "title": "CAPÍTULO 3 — TÓPICO 1: ANATOMIA DO EXCEL E CONCEITOS INICIAIS",
            "concept": "A interface do Excel é composta por colunas (identificadas por letras de A a XFD), linhas (de 1 a 1.048.576) e células (interseções representadas por coordenadas exatas como A1). O ambiente integra a Fita de Opções (menus de recursos agrupados por abas de comandos) e a Barra de Fórmulas para manipulação direta de dados.",
            "syntax": "Coordenada de Célula: <code>[Coluna Letra][Linha Número]</code> (Ex: B5 representa a interseção da Coluna B com a Linha 5).",
            "ex1_title": "Exemplo 1: Mapeamento de Layout de Sala de Aula",
            "ex1_desc": "O docente organiza uma grade na planilha para representar a disposição física das carteiras dos alunos (de A1 a F6), permitindo planejar e alterar rapidamente assentos de inclusão de alunos com TDAH ou baixa acuidade visual.",
            "ex2_title": "Exemplo 2: Registro de Chromebooks Escolares",
            "ex2_desc": "A equipe diretiva monta uma planilha mapeando colunas para Código do Dispositivo, Data de Empréstimo e Sala de Destino, identificando por linha os chromebooks em uso no laboratório.",
            "ex3_title": "Exemplo 3: Planejador Semanal de Disciplinas",
            "ex3_desc": "Estruturar o horário semanal de aulas, cruzando as linhas de horários com colunas contendo as turmas atendidas, gerando um mapa claro de atuação pedagógica docente."
        },
        {
            "id": 2,
            "title": "CAPÍTULO 4 — TÓPICO 2: FORMATAÇÃO PEDAGÓGICA DE DIÁRIOS",
            "concept": "A formatação estética de planilhas garante legibilidade visual imediata. O uso coordenado de cores institucionais (como o Verde Excel), aplicação de bordas estruturais de grade e formatação adequada das fontes previnem cansaço visual e diminuem drasticamente erros de lançamento.",
            "syntax": "Guia Página Inicial -> Preenchimento de Célula (Balde de Tinta) -> Cores Temáticas. Ativar Bordas -> Todas as Bordas.",
            "ex1_title": "Exemplo 1: Diário de Presença Legível",
            "ex1_desc": "Aplicar preenchimento verde escuro com texto em branco nas células de cabeçalho (A1:E1) de uma planilha de chamada para guiar os olhos do professor, impedindo o registro de presenças em linhas trocadas de estudantes.",
            "ex2_title": "Exemplo 2: Destaque de Prazos de Entregas",
            "ex2_desc": "Colorir a coluna de datas finais de entrega de trabalhos em amarelo suave, separando-as visivelmente de dados cadastrais gerais da turma para visualização rápida da gestão escolar.",
            "ex3_title": "Exemplo 3: Quadro de Níveis de Alfabetização",
            "ex3_desc": "Estilizar a grelha de fluência de leitura no Ensino Fundamental I com fontes limpas e sem excesso de decorações, facilitando a rápida leitura visual para diagnósticos periódicos."
        },
        {
            "id": 3,
            "title": "CAPÍTULO 5 — TÓPICO 3: CÁLCULO DE MÉDIAS SEM ERROS",
            "concept": "A função MÉDIA substitui cálculos manuais repetitivos com calculadoras. O Excel soma dinamicamente os valores numéricos em uma faixa contígua ou dispersa de células e realiza a divisão pela quantidade exata de entradas preenchidas, descartando de forma inteligente as células vazias referentes a provas não realizadas por ausência letiva.",
            "syntax": "<code>=MÉDIA(célula_inicial:célula_final)</code>. Ex: `=MÉDIA(B2:E2)`",
            "ex1_title": "Exemplo 1: Média Final de Arthur Silva",
            "ex1_desc": "O professor insere <code>=MÉDIA(B2:E2)</code> na coluna de notas finais, obtendo instantaneamente a média aritmética das notas dos 4 bimestres contidas nas células B2, C2, D2 e E2 sem margem de erro aritmético.",
            "ex2_title": "Exemplo 2: Média Coletiva em Prova de Matemática",
            "ex2_desc": "Computar a média total de desempenho de uma avaliação bimestral de toda a turma para avaliar se o plano de ensino atingiu o objetivo pedagógico mínimo fixado.",
            "ex3_title": "Exemplo 3: Mapeamento de Notas Ponderadas",
            "ex3_desc": "Calcular as médias finais em projetos complexos ou Feiras de Ciências Escolares atribuindo pesos variados para o desenvolvimento escrito e para a apresentação em grupo."
        },
        {
            "id": 4,
            "title": "CAPÍTULO 6 — TÓPICO 4: LÓGICA CONDICIONAL DE STATUS",
            "concept": "A automação de decisões pedagógicas assenta-se na função SE. A fórmula efetua um teste lógico e devolve de forma automática uma resposta textual ou computacional caso o resultado seja verdadeiro, e outra resposta distinta caso seja falso, permitindo rotular condições escolares dinamicamente.",
            "syntax": "<code>=SE(teste_lógico; valor_se_verdadeiro; valor_se_falso)</code>. Ex: `=SE(F2>=6;\"APROVADO\";\"RECUPERAÇÃO\")`",
            "ex1_title": "Exemplo 1: Aprovação e Recuperação Automatizada",
            "ex1_desc": "O Excel avalia a média final anual calculada. Caso o valor contido em F2 seja igual ou superior a 6, escreve 'APROVADO'; caso contrário, estampa de forma instantânea a frase 'RECUPERAÇÃO'.",
            "ex2_title": "Exemplo 2: Alertas de Risco Legal de Faltas",
            "ex2_desc": "Lógica para identificar excesso de faltas baseada no limite da LDB: <code>=SE(H2<75%;\"Alertar Conselho\";\"Frequência Regular\")</code>.",
            "ex3_title": "Exemplo 3: Gestão de Insumos e Estoque da Merenda",
            "ex3_desc": "Uma fórmula na planilha de estoque escolar avisa o gestor emitindo a palavra 'COMPRAR' quando a quantidade em quilos do alimento estiver abaixo do estoque mínimo pré-definido."
        },
        {
            "id": 5,
            "title": "CAPÍTULO 7 — TÓPICO 5: MAPA DE CALOR E SINALIZAÇÕES",
            "concept": "A Formatação Condicional converte números frios em representações visuais rápidas na planilha. Ao associar regras de cores a valores específicos (como fundos avermelhados para notas críticas), o professor detecta instantaneamente os alunos com graves defasagens letivas no conselho de classe.",
            "syntax": "Guia Página Inicial -> Formatação Condicional -> Regras de Destaque das Células -> Menor que [Valor] -> Escolha de Cor.",
            "ex1_title": "Exemplo 1: Destaque de Médias Vermelhas no Diário",
            "ex1_desc": "Configurar a coluna de médias para pintar em tom vermelho claro as notas menores que 5.0, criando um alerta visual automático para montagem imediata de turmas de recuperação.",
            "ex2_title": "Exemplo 2: Mapeamento de Risco Crítico de Infrequência",
            "ex2_desc": "Colorir células de taxas de faltas acima de 25% com laranja vibrante, sinalizando educandos com risco letivo iminente de infrequência crônica.",
            "ex3_title": "Exemplo 3: Controle e Acompanhamento de Apoios do AEE",
            "ex3_desc": "Uso de coloração tag verde para 'Realizado' e amarelo para 'Apoio Pendente' no diário do Atendimento Educacional Especializado (AEE), assegurando a entrega das adaptações curriculares."
        },
        {
            "id": 6,
            "title": "CAPÍTULO 8 — TÓPICO 6: GESTÃO DE FILTROS E BUSCA ATIVA",
            "concept": "Filtros de tabela são mecanismos de gerenciamento e triagem de grandes volumes de informações. Ao acionar o recurso, o professor isola linhas contendo dados específicos, ocultando registros regulares para concentrar atenção pedagógica ou gerar listas focadas.",
            "syntax": "Guia Dados -> Filtro. Acionar o menu suspenso (▼) no cabeçalho correspondente e selecionar os critérios desejados.",
            "ex1_title": "Exemplo 1: Isolamento de Alunos Infrequentes (Busca Ativa)",
            "ex1_desc": "O coordenador filtra a lista de chamada total da escola ocultando alunos regulares e deixando apenas aqueles com frequência inferior a 75%, fornecendo a planilha oficial de busca ativa escolar.",
            "ex2_title": "Exemplo 2: Triagem de Estudantes Alérgicos (Merenda)",
            "ex2_desc": "Filtrar a base cadastral de matrículas escolares por 'Restrições Alimentares', isolando alunos celíacos ou intolerantes à lactose para repasse seguro do cronograma alimentar à cozinha.",
            "ex3_title": "Exemplo 3: Mapeamento de Alunos Laudados (AEE)",
            "ex3_desc": "Filtrar a base geral de alunos para listar em poucos segundos todos os alunos laudados cadastrados, facilitando a elaboração do plano de compras de recursos de acessibilidade."
        },
        {
            "id": 7,
            "title": "CAPÍTULO 9 — TÓPICO 7: PESQUISA E LOCALIZAÇÃO COM PROCV",
            "concept": "O PROCV (Procura Vertical) realiza buscas rápidas em grandes repositórios de dados. A fórmula lê o valor procurado na primeira coluna de uma matriz informada e extrai a informação correspondente que se encontra na coluna indicada no índice da busca vertical.",
            "syntax": "<code>=PROCV(valor_procurado; matriz_tabela; índice_coluna; procurar_intervalo)</code>. Ex: `=PROCV(\"Carlos\";A2:B5;2;FALSO)`",
            "ex1_title": "Exemplo 1: Extração Rápida de CPF de Aluno",
            "ex1_desc": "Digitar o nome do discente e extrair em segundos seu número de CPF arquivado na base de dados geral da secretaria para lançamentos no censo escolar: <code>=PROCV(\"Carlos\";A2:B5;2;FALSO)</code>.",
            "ex2_title": "Exemplo 2: Localizador de Livros na Biblioteca",
            "ex2_desc": "Localizar de forma automatizada a prateleira e a sala de leitura de um exemplar pedagógico digitando apenas o título do livro procurado na planilha de controle.",
            "ex3_title": "Exemplo 3: Telefone de Contato de Emergência",
            "ex3_desc": "Cruzamento de dados rápidos para obter o contato dos responsáveis em caso de indisposição repentina ou acidente com o estudante em horário de aula letiva."
        },
        {
            "id": 8,
            "title": "CAPÍTULO 10 — TÓPICO 8: VALIDAÇÃO E INTEGRIDADE DE DADOS",
            "concept": "A Validação de Dados atua como uma barreira preventiva contra digitações incorretas nas células. Impede a gravação de informações fora dos padrões pedagógicos ou regulatórios estipulados (como notas absurdas digitadas acidentalmente), bloqueando a entrada e emitindo um aviso sonoro/visual.",
            "syntax": "Guia Dados -> Validação de Dados -> Configurações: Permitir: 'Decimal', Dados: 'entre', Mínimo: 0, Máximo: 10.",
            "ex1_title": "Exemplo 1: Restrição de Lançamentos de Notas Escolares",
            "ex1_desc": "Bloquear as notas bimestrais para aceitarem apenas decimais de 0.0 a 10.0, emitindo aviso sonoro se um docente tentar registrar o valor 11.0 por distração ou cansaço.",
            "ex2_title": "Exemplo 2: Datas Restritas ao Calendário Letivo",
            "ex2_desc": "Limitar a inserção de datas em planilhas de registros de aulas para aceitar exclusivamente dias úteis dentro do ano civil pedagógico oficial homologado.",
            "ex3_title": "Exemplo 3: Lista Suspensa de Categorias Pedagógicas",
            "ex3_desc": "Restringir o preenchimento de colunas como 'Status Especial' ou 'Turma' através de um menu de seleção contendo apenas os dados autorizados existentes."
        },
        {
            "id": 9,
            "title": "CAPÍTULO 11 — TÓPICO 9: GRÁFICOS DE EVOLUÇÃO E TENDÊNCIA",
            "concept": "Gráficos convertem dados numéricos tabulares em representações visuais claras de comunicação em conselhos e reuniões pedagógicas. O Gráfico de Linhas é o modelo estatístico correto para evidenciar a progressão cronológica do estudante ao longo do ano letivo.",
            "syntax": "Selecionar dados -> Guia Inserir -> Gráfico de Linhas (Tendências) ou Gráfico de Colunas (Comparações).",
            "ex1_title": "Exemplo 1: Progressão Cronológica de Notas pós-Reforço",
            "ex1_desc": "Desenhar um gráfico de linhas conectando as notas bimestrais do discente para evidenciar aos pais, de forma clara, o impacto positivo do reforço ofertado no contraturno escolar.",
            "ex2_title": "Exemplo 2: Monitoramento Anual de Taxas de Matrícula",
            "ex2_desc": "Construir um gráfico de barras empilhadas para apresentar à prefeitura o fluxo de matrículas novas por segmento escolar ao longo de cinco períodos anuais.",
            "ex3_title": "Exemplo 3: Distribuição Visual de Níveis de Fluência",
            "ex3_desc": "Utilizar gráficos de colunas para comparar a quantidade percentual de alunos considerados alfabetizados, silábicos e pré-silábicos entre turmas do mesmo ano."
        },
        {
            "id": 10,
            "concept": "A segurança da informação é um dever ético-pedagógico dos educadores, respaldado legalmente pela Lei Geral de Proteção de Dados (LGPD). O bloqueio de células contendo fórmulas sensíveis, seguido da proteção geral da pasta de trabalho por senha forte, previne alterações acidentais de notas oficiais.",
            "title": "CAPÍTULO 12 — TÓPICO 10: SEGURANÇA ESCOLAR E ÉTICA (LGPD)",
            "syntax": "Selecionar células -> Formatar Células -> Proteção -> Marcar 'Bloqueada'. Guia Revisão -> Proteger Planilha -> Ativar com Senha.",
            "ex1_title": "Exemplo 1: Blindagem de Fórmulas no Diário",
            "ex1_desc": "Marcar a coluna de médias como 'Bloqueada' e proteger a planilha com senha, de forma que substitute teachers consigam lançar notas pontuais mas nunca alterar ou apagar as fórmulas lógicas.",
            "ex2_title": "Exemplo 2: Compartilhamento Seguro com a Equipe",
            "ex2_desc": "Restringir o acesso a dados de alunos sensíveis enviando planilhas encriptadas ou sob senha, garantindo a confidencialidade legal requerida pelo censo.",
            "ex3_title": "Exemplo 3: Edição Restrita por Componente Curricular",
            "ex3_desc": "Configurar permissões específicas na planilha compartilhada na nuvem municipal para que cada docente edite exclusivamente as células de notas de sua respectiva disciplina."
        }
    ]
    
    for t in topics:
        story.append(Paragraph(t["title"], styles['ABNTH1']))
        story.append(Paragraph(t["concept"], styles['ABNTP']))
        story.append(Paragraph(f"<b>Sintaxe / Configuração Técnica:</b> {t['syntax']}", styles['ABNTP']))
        
        # Bloco de Exemplos formatado em tabela (estilo Caixa Acadêmica ABNT)
        c_exs = [
            Paragraph(f"<b>CENÁRIOS PRÁTICOS E APLICAÇÃO DIÁRIA ESCOLAR</b>", ParagraphStyle('SubEx', fontName='Times-Bold', fontSize=10, textColor=green_accent, spaceAfter=8)),
            Paragraph(f"<b>{t['ex1_title']}:</b> {t['ex1_desc']}", styles['ABNTExemploCorpo']),
            Spacer(1, 4),
            Paragraph(f"<b>{t['ex2_title']}:</b> {t['ex2_desc']}", styles['ABNTExemploCorpo']),
            Spacer(1, 4),
            Paragraph(f"<b>{t['ex3_title']}:</b> {t['ex3_desc']}", styles['ABNTExemploCorpo'])
        ]
        
        # Envelopa em Tabela
        cell_parag = Paragraph("<br/>".join([
            f"<b>CENÁRIOS PRÁTICOS E APLICAÇÃO DIÁRIA ESCOLAR</b><br/>",
            f"<b>{t['ex1_title']}:</b> {t['ex1_desc']}<br/>",
            f"<b>{t['ex2_title']}:</b> {t['ex2_desc']}<br/>",
            f"<b>{t['ex3_title']}:</b> {t['ex3_desc']}"
        ]), styles['ABNTExemploCorpo'])
        
        t_box = Table([[cell_parag]], colWidths=[445])
        t_box.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), yellow_bg),
            ('BOX', (0,0), (-1,-1), 1.5, yellow_border),
            ('PADDING', (0,0), (-1,-1), 12),
        ]))
        
        story.append(t_box)
        story.append(PageBreak())
        
    # ------------------ SEÇÃO DE SUPORTE E AUTORIA PEDAGÓGICA ------------------
    story.append(Paragraph("CAPÍTULO 13 — SUPORTE TÉCNICO & AUTORIA PEDAGÓGICA", styles['ABNTH1']))
    story.append(Paragraph("Este Itinerário Extensionista de Literacia Digital em Planilhas Escolares é o resultado de uma cooperação interdisciplinar técnica voltada ao desenvolvimento educacional permanente na rede municipal.", styles['ABNTP']))
    
    # Bloco de Contato
    th_sup = ParagraphStyle('THS', fontName='Times-Bold', fontSize=10.5, textColor=colors.white)
    data_sup = [
        [Paragraph("Função / Atuação", th_sup), Paragraph("Responsável Pedagógico", th_sup), Paragraph("Escopo de Auxílio", th_sup)],
        [Paragraph("<b>Autor e Idealizador</b>", styles['ABNTExemploCorpo']), Paragraph("<font color='#0b592e'><b>Juliano Prianti</b></font><br/>Professor e Designer Didático", styles['ABNTExemploCorpo']), Paragraph("Concepção teórica, estruturação metodológica dos 10 desafios de literacia e pedagogia.", styles['ABNTExemploCorpo'])],
        [Paragraph("<b>Suporte Técnico & TI</b>", styles['ABNTExemploCorpo']), Paragraph("<font color='#0b592e'><b>Gabriel H. Rodrigues</b></font><br/>Engenheiro de TI", styles['ABNTExemploCorpo']), Paragraph("Ambiente virtual do laboratório, scripts automatizados e arquitetura da aplicação.", styles['ABNTExemploCorpo'])],
    ]
    t_sup = Table(data_sup, colWidths=[120, 150, 175])
    t_sup.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), green_accent),
        ('GRID', (0,0), (-1,-1), 0.5, border_gray),
        ('PADDING', (0,0), (-1,-1), 8),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BACKGROUND', (0,1), (-1,1), colors.white),
        ('BACKGROUND', (0,2), (-1,2), colors.HexColor("#FAF9F8")),
    ]))
    story.append(t_sup)
    story.append(Spacer(1, 10))
    story.append(Paragraph("O presente itinerário fomenta a adoção de boas práticas na guarda e processamento de informações no ambiente escolar, alinhando-se aos ditames federais de ética e integridade corporativa pública.", styles['ABNTP']))
    
    # Construção do PDF
    doc.build(story, canvasmaker=ABNTCanvas)
    print(f"Sucesso: O PDF resumido ABNT foi gerado em '{filename}'!")

if __name__ == "__main__":
    pdf_filename = "Documentacao_Resumida_ABNT.pdf"
    build_pdf(pdf_filename)
