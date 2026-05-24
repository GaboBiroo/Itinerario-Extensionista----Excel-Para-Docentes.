# -*- coding: utf-8 -*-
import os
import sys

# Garante saída UTF-8 no console
sys.stdout.reconfigure(encoding='utf-8')

try:
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib import colors
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.pdfgen import canvas
except ImportError:
    print("Erro: A biblioteca reportlab não está instalada. Por favor, rode 'pip install reportlab' antes de executar este script.")
    sys.exit(1)

# Dimensões da Página (A4 em Paisagem)
PAGE_WIDTH, PAGE_HEIGHT = landscape(A4)

class SlideCanvas(canvas.Canvas):
    """
    Canvas personalizado para desenhar decorações em duas passagens,
    permitindo exibir dinamicamente o número total de páginas (slides).
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
            self.draw_slide_decorations(page_count)
            super().showPage()
        super().save()
        
    def draw_slide_decorations(self, total_pages):
        self.saveState()
        
        green_excel = colors.HexColor("#107C41")
        border_gray = colors.HexColor("#D2D0CE")
        text_gray = colors.HexColor("#605E5C")
        
        # Faixa verde no topo de todas as páginas
        self.setFillColor(green_excel)
        self.rect(0, PAGE_HEIGHT - 12, PAGE_WIDTH, 12, stroke=0, fill=1)
        
        if self._pageNumber == 1:
            # Capa do Slide: Borda interna dourada grossa nas laterais para visual clássico
            self.setStrokeColor(colors.HexColor("#D4AF37"))
            self.setLineWidth(6)
            self.rect(15, 15, PAGE_WIDTH - 30, PAGE_HEIGHT - 30, stroke=1, fill=0)
        else:
            # Demais slides: Cabeçalho superior
            self.setFont("Helvetica-Bold", 10)
            self.setFillColor(colors.HexColor("#0b592e"))
            self.drawString(40, PAGE_HEIGHT - 36, "EXCEL PARA EDUCADORES")
            
            self.setFont("Helvetica", 9)
            self.setFillColor(text_gray)
            self.drawRightString(PAGE_WIDTH - 40, PAGE_HEIGHT - 36, "Capacitação Pedagógica Permanente")
            
            # Linha divisória de cabeçalho
            self.setStrokeColor(border_gray)
            self.setLineWidth(1)
            self.line(40, PAGE_HEIGHT - 44, PAGE_WIDTH - 40, PAGE_HEIGHT - 44)
            
            # Rodapé
            self.setFont("Helvetica-Oblique", 8)
            self.drawString(40, 24, "Autor: Juliano Prianti | Suporte Técnico: Gabriel H. Rodrigues")
            
            self.setFont("Helvetica", 9)
            self.drawRightString(PAGE_WIDTH - 40, 24, f"Slide {self._pageNumber} de {total_pages}")
            
        self.restoreState()

def build_pdf(filename):
    # Configuração do Documento com margens largas e adequadas
    doc = SimpleDocTemplate(
        filename,
        pagesize=landscape(A4),
        leftMargin=50,
        rightMargin=50,
        topMargin=60,
        bottomMargin=50
    )
    
    styles = getSampleStyleSheet()
    
    # Cores
    green_primary = colors.HexColor("#107C41")
    green_hover = colors.HexColor("#0b592e")
    text_dark = colors.HexColor("#323130")
    text_muted = colors.HexColor("#605E5C")
    card_bg = colors.HexColor("#FAF9F8")
    border_gray = colors.HexColor("#D2D0CE")
    
    # Estilos de Parágrafos
    styles.add(ParagraphStyle(
        name='CoverTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=38,
        leading=44,
        textColor=green_primary,
        alignment=1, # Centralizado
        spaceAfter=15
    ))
    
    styles.add(ParagraphStyle(
        name='CoverSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=18,
        leading=22,
        textColor=text_dark,
        alignment=1,
        spaceAfter=30
    ))
    
    styles.add(ParagraphStyle(
        name='CoverBadge',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=green_hover,
        alignment=1,
        spaceAfter=40
    ))
    
    styles.add(ParagraphStyle(
        name='SlideTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=24,
        leading=28,
        textColor=green_hover,
        spaceAfter=6
    ))
    
    styles.add(ParagraphStyle(
        name='SlideSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=text_muted,
        spaceAfter=25
    ))
    
    styles.add(ParagraphStyle(
        name='SlideText',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=18,
        textColor=text_dark,
        spaceAfter=14
    ))
    
    styles.add(ParagraphStyle(
        name='SlideBullet',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=11.5,
        leading=17,
        textColor=text_dark,
        leftIndent=20,
        firstLineIndent=-12,
        spaceAfter=10
    ))
    
    styles.add(ParagraphStyle(
        name='CardTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=14,
        textColor=green_hover,
        spaceAfter=4
    ))
    
    styles.add(ParagraphStyle(
        name='CardBody',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13,
        textColor=text_dark
    ))

    story = []
    
    # ------------------ SLIDE 1: CAPA ------------------
    story.append(Spacer(1, 100))
    story.append(Paragraph("Excel para Educadores", styles['CoverTitle']))
    story.append(Paragraph("Literacia de Dados e Gestão Eficiente na Rede Municipal", styles['CoverSubtitle']))
    story.append(Paragraph("CAPACITAÇÃO DOCENTE PERMANENTE", styles['CoverBadge']))
    story.append(Spacer(1, 30))
    story.append(PageBreak())
    
    # ------------------ SLIDE 2: INTRODUÇÃO ------------------
    story.append(Paragraph("Os 10 Passos da Literacia", styles['SlideTitle']))
    story.append(Paragraph("A tecnologia deve libertar o professor da burocracia", styles['SlideSubtitle']))
    story.append(Paragraph("Bem-vindo(a) ao seu <b>Laboratório de Literacia Docente</b>! Este itinerário formativo foi estruturado em <b>10 desafios práticos</b> para capacitá-lo na gestão diária de dados pedagógicos.", styles['SlideText']))
    story.append(Paragraph("Vamos transformar listas de chamadas estáticas e diários físicos em sistemas automatizados e eficientes. A automação nos dá de volta o que há de mais precioso: o tempo de focar nos alunos.", styles['SlideText']))
    
    # Grid de cards
    c1 = Paragraph("<b>🎯 Estética Pedagógica</b><br/>Tabelas claras e organizadas ajudam no fluxo de leitura e evitam erros cruciais de lançamento.", styles['CardBody'])
    c2 = Paragraph("<b>⚡ Prática Imediata</b><br/>Após compreender a base teórica neste guia, você acionará o simulador prático interativo.", styles['CardBody'])
    t_intro = Table([[c1, c2]], colWidths=[360, 360])
    t_intro.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), card_bg),
        ('BOX', (0,0), (-1,-1), 1, border_gray),
        ('INNERGRID', (0,0), (-1,-1), 1, border_gray),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_intro)
    story.append(PageBreak())
    
    # ------------------ SLIDE 3: ANATOMIA DO EXCEL ------------------
    story.append(Paragraph("1. A Anatomia do Excel", styles['SlideTitle']))
    story.append(Paragraph("Dominando o Ambiente de Trabalho", styles['SlideSubtitle']))
    story.append(Paragraph("O primeiro passo do nosso Laboratório é dominar a interface visual do Excel. Você precisará reconhecer e interagir com 5 áreas essenciais:", styles['SlideText']))
    
    story.append(Paragraph("• <b>Fita de Opções:</b> Os menus superiores que agrupam comandos por abas de ação.", styles['SlideBullet']))
    story.append(Paragraph("• <b>Barra de Fórmulas:</b> O campo de texto longo para visualização e edição exata de fórmulas.", styles['SlideBullet']))
    story.append(Paragraph("• <b>Cabeçalhos:</b> Identificadores de colunas (Letras A, B, C) e linhas (Números 1, 2, 3).", styles['SlideBullet']))
    story.append(Paragraph("• <b>Barra de Status:</b> A faixa inferior que apresenta dados resumidos e status do sistema.", styles['SlideBullet']))
    story.append(PageBreak())
    
    # ------------------ SLIDE 4: DIÁRIO VISUAL ------------------
    story.append(Paragraph("2. O Diário Visual", styles['SlideTitle']))
    story.append(Paragraph("Preenchimento de Cabeçalhos e Bordas de Grade", styles['SlideSubtitle']))
    story.append(Paragraph("Um diário de classe confuso induz a erros ao transferir as notas para os sistemas municipais. O visual das planilhas pedagógicas deve ser limpo e intuitivo.", styles['SlideText']))
    
    c1 = Paragraph("<b>🎨 Preenchimento Verde</b><br/>No laboratório, você deverá selecionar o intervalo de cabeçalho <b>A1:E1</b> e usar a ferramenta Balde de Tinta na fita para aplicar um preenchimento <b>Verde Escuro</b>.", styles['CardBody'])
    c2 = Paragraph("<b>🔳 Bordas Completas</b><br/>Em seguida, acione o ícone de bordas no menu superior e ative <b>Todas as Bordas</b>, delimitando os dados e destacando a leitura e a estrutura da tabela.", styles['CardBody'])
    t_visual = Table([[c1, c2]], colWidths=[360, 360])
    t_visual.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), card_bg),
        ('BOX', (0,0), (-1,-1), 1, border_gray),
        ('INNERGRID', (0,0), (-1,-1), 1, border_gray),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_visual)
    story.append(PageBreak())
    
    # ------------------ SLIDE 5: ARITMÉTICA AUTOMATIZADA ------------------
    story.append(Paragraph("3. Aritmética Automatizada", styles['SlideTitle']))
    story.append(Paragraph("Calculando Médias sem Erro Humano", styles['SlideSubtitle']))
    story.append(Paragraph("O Excel descarta o uso de calculadoras externas. A função de cálculo automático soma os bimestres e divide ignorando células em branco.", styles['SlideText']))
    story.append(Paragraph("No terceiro desafio técnico do Laboratório, você calculará a média anual das notas do aluno Arthur Silva digitando a fórmula oficial:", styles['SlideText']))
    
    # Caixa da Fórmula
    c_f = Paragraph("<b>=MÉDIA(B2:E2)</b>", ParagraphStyle('Formula', fontName='Courier-Bold', fontSize=18, textColor=green_hover, alignment=1))
    t_formula = Table([[c_f]], colWidths=[400])
    t_formula.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.white),
        ('BOX', (0,0), (-1,-1), 1, border_gray),
        ('PADDING', (0,0), (-1,-1), 15),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
    ]))
    story.append(Spacer(1, 10))
    story.append(t_formula)
    story.append(Spacer(1, 10))
    story.append(Paragraph("<font color='#605E5C' size='9'><i>(Indica que a média cobrirá as notas registradas nas células B2, C2, D2 e E2 correspondentes)</i></font>", styles['CoverSubtitle']))
    story.append(PageBreak())
    
    # ------------------ SLIDE 6: LÓGICA CONDICIONAL ------------------
    story.append(Paragraph("4. Lógica Condicional", styles['SlideTitle']))
    story.append(Paragraph("O julgamento automático de médias com a função SE", styles['SlideSubtitle']))
    story.append(Paragraph("Vamos automatizar a tomada de decisões na escola! Em vez de digitar manualmente se o aluno foi aprovado ou está em recuperação, usaremos a função lógica <b>=SE</b>.", styles['SlideText']))
    
    c1 = Paragraph("<b>1. Teste Lógico (B2>=6)</b><br/>Analisa se a média de Arthur em B2 é maior ou igual a 6.", styles['CardBody'])
    c2 = Paragraph("<b>2. Se Verdadeiro (\"APROVADO\")</b><br/>O resultado retornado se a nota de Arthur for igual ou superior a 6.", styles['CardBody'])
    c3 = Paragraph("<b>3. Se Falso (\"RECUPERAÇÃO\")</b><br/>O resultado caso a média seja menor que 6.", styles['CardBody'])
    
    t_se = Table([[c1, c2, c3]], colWidths=[240, 240, 240])
    t_se.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), card_bg),
        ('BOX', (0,0), (-1,-1), 1, border_gray),
        ('INNERGRID', (0,0), (-1,-1), 1, border_gray),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_se)
    story.append(PageBreak())
    
    # ------------------ SLIDE 7: MAPA DE CALOR ------------------
    story.append(Paragraph("5. O Mapa de Calor", styles['SlideTitle']))
    story.append(Paragraph("Identificando Alunos em Risco com Formatação Condicional", styles['SlideSubtitle']))
    story.append(Paragraph("O olhar pedagógico deve repousar com prioridade absoluta sobre os alunos que necessitam de intervenção pedagógica e recuperação imediata.", styles['SlideText']))
    story.append(Paragraph("A <b>Formatação Condicional</b> atua de forma automatizada, pintando o fundo das células com base nos critérios pedagógicos definidos.", styles['SlideText']))
    
    # Card de Alerta
    c_alert = Paragraph("<b>📢 No Desafio do Laboratório:</b><br/>Você selecionará a coluna de Notas e ativará a <b>Regra de Células: Menor que 5</b> para pintar automaticamente em Vermelho Claro todas as notas baixas da tabela, criando um mapa de calor instantâneo.", styles['CardBody'])
    t_alert = Table([[c_alert]], colWidths=[720])
    t_alert.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFF5F5")),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor("#FF3B30")),
        ('PADDING', (0,0), (-1,-1), 14),
    ]))
    story.append(t_alert)
    story.append(PageBreak())
    
    # ------------------ SLIDE 8: FILTROS DE EVASÃO ------------------
    story.append(Paragraph("6. Filtros de Evasão", styles['SlideTitle']))
    story.append(Paragraph("Acompanhamento Ativo de Frequência Escolar", styles['SlideSubtitle']))
    story.append(Paragraph("O Bolsa Família e as portarias do conselho tutelar exigem vigilância estrita sobre a evasão escolar e o absenteísmo dos educandos.", styles['SlideText']))
    
    story.append(Paragraph("• <b>Filtro de Planilha:</b> Você ativará o Filtro (ícone de funil) no cabeçalho da coluna <b>Frequência</b>.", styles['SlideBullet']))
    story.append(Paragraph("• <b>Isolando Alunos em Risco:</b> Configurará a opção para selecionar e isolar apenas os alunos com frequência <b>menor que 75%</b>, permitindo emitir relatórios de busca ativa.", styles['SlideBullet']))
    story.append(Paragraph("• <b>Importância:</b> Com diários filtrados, as equipes de coordenação e assistência social atuam antes que a infrequência se converta em abandono definitivo.", styles['SlideBullet']))
    story.append(PageBreak())
    
    # ------------------ SLIDE 9: LOCALIZADOR PROCV ------------------
    story.append(Paragraph("7. O Localizador PROCV", styles['SlideTitle']))
    story.append(Paragraph("Pesquisando Dados de Alunos Instantaneamente", styles['SlideSubtitle']))
    story.append(Paragraph("Como extrair o CPF de um aluno específico no meio de uma planilha com mais de 800 cadastros? A função <b>PROCV</b> realiza essa pesquisa vertical cruzando os dados das tabelas:", styles['SlideText']))
    
    # Tabela do PROCV
    header_style = ParagraphStyle('TH', fontName='Helvetica-Bold', fontSize=10, textColor=colors.white)
    cell_bold_style = ParagraphStyle('TDBold', fontName='Helvetica-Bold', fontSize=9, textColor=text_dark)
    cell_normal_style = ParagraphStyle('TDNormal', fontName='Helvetica', fontSize=9, textColor=text_dark)
    
    data = [
        [Paragraph("Parâmetro", header_style), Paragraph("Significado Didático", header_style), Paragraph("Inserção no Simulador", header_style)],
        [Paragraph("1. Valor Procurado", cell_bold_style), Paragraph("O dado de referência que você já possui.", cell_normal_style), Paragraph("<b>\"Carlos\"</b> (entre aspas por ser texto)", cell_normal_style)],
        [Paragraph("2. Matriz Tabela", cell_bold_style), Paragraph("A região de busca (cobre as colunas A e B).", cell_normal_style), Paragraph("<b>A2:B5</b>", cell_normal_style)],
        [Paragraph("3. Índice de Coluna", cell_bold_style), Paragraph("A contagem da coluna que contém a resposta.", cell_normal_style), Paragraph("<b>2</b> (A coluna 2 guarda os CPFs)", cell_normal_style)],
        [Paragraph("4. Procurar Intervalo", cell_bold_style), Paragraph("Tipo de busca: exata (FALSO) ou aproximada.", cell_normal_style), Paragraph("<b>FALSO</b> (Garante correspondência exata)", cell_normal_style)],
    ]
    t_vlookup = Table(data, colWidths=[180, 320, 220])
    t_vlookup.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), green_hover),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 8),
        ('GRID', (0,0), (-1,-1), 0.5, border_gray),
        ('BACKGROUND', (0,1), (-1,1), colors.white),
        ('BACKGROUND', (0,2), (-1,2), card_bg),
        ('BACKGROUND', (0,3), (-1,3), colors.white),
        ('BACKGROUND', (0,4), (-1,4), card_bg),
    ]))
    story.append(t_vlookup)
    story.append(PageBreak())
    
    # ------------------ SLIDE 10: INTEGRIDADE DE DADOS ------------------
    story.append(Paragraph("8. Integridade de Dados", styles['SlideTitle']))
    story.append(Paragraph("Evitando digitações acidentais e erros de secretaria", styles['SlideSubtitle']))
    story.append(Paragraph("Digitar uma nota errada como '11' por pressa ou distração gera graves inconsistências legais e escolares. A <b>Validação de Dados</b> nos protege blindando as células.", styles['SlideText']))
    
    c1 = Paragraph("<b>🎯 Nossa Configuração de Segurança</b><br/>No simulador, você abrirá a Validação de Dados na aba Dados e a configurará para aceitar exclusivamente números do tipo <b>Decimal</b>, limitando os valores de notas em um intervalo entre o Mínimo de <b>0</b> e Máximo de <b>10</b>.", styles['CardBody'])
    c2 = Paragraph("<b>🚨 Alerta de Erro do Excel</b><br/>Ao testar inserindo a nota 11 na planilha validada, o sistema municipal recusará a entrada imediatamente, exibindo um alerta sonoro e visual para impedir o erro.", styles['CardBody'])
    t_valid = Table([[c1, c2]], colWidths=[360, 360])
    t_valid.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), card_bg),
        ('BOX', (0,0), (-1,-1), 1, border_gray),
        ('INNERGRID', (0,0), (-1,-1), 1, border_gray),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_valid)
    story.append(PageBreak())
    
    # ------------------ SLIDE 11: GRÁFICOS DE TENDÊNCIA ------------------
    story.append(Paragraph("9. Gráficos de Tendência", styles['SlideTitle']))
    story.append(Paragraph("Acompanhando o progresso de notas ao longo do tempo", styles['SlideSubtitle']))
    story.append(Paragraph("Para conselhos de classe e devolutivas pedagógicas para as famílias, a visualização cronológica ajuda a identificar o impacto das nossas intervenções e apoios.", styles['SlideText']))
    
    c1 = Paragraph("<b>📈 Gráfico de Linhas</b><br/><b>A Escolha Correta!</b> Demonstra visualmente as tendências temporais com clareza (subidas, quedas ou platôs) de forma fluida.", styles['CardBody'])
    c2 = Paragraph("<b>🍕 Gráfico de Pizza</b><br/>Inadequado para continuidade temporal. Serve para analisar proporções estáticas e partes isoladas de um todo.", styles['CardBody'])
    t_graph = Table([[c1, c2]], colWidths=[360, 360])
    t_graph.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), card_bg),
        ('BOX', (0,0), (-1,-1), 1, border_gray),
        ('INNERGRID', (0,0), (-1,-1), 1, border_gray),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_graph)
    story.append(PageBreak())
    
    # ------------------ SLIDE 12: SEGURANÇA ESCOLAR ------------------
    story.append(Paragraph("10. Segurança Escolar", styles['SlideTitle']))
    story.append(Paragraph("Evitando alterações acidentais em fórmulas essenciais", styles['SlideSubtitle']))
    story.append(Paragraph("Após estruturar e programar toda a inteligência e as fórmulas lógicas da sua planilha, o diário deve ser protegido antes de ser compartilhado.", styles['SlideText']))
    
    c1 = Paragraph("<b>🔒 Passo 1: Bloquear Células</b><br/>Garantir que as células contendo fórmulas automáticas de notas estejam marcadas como <b>Bloqueadas</b> nas propriedades de proteção da célula.", styles['CardBody'])
    c2 = Paragraph("<b>🛡️ Passo 2: Proteger Planilha</b><br/>Ir até a aba superior <b>Revisão</b> e acionar o botão <b>Proteger Planilha</b>, ativando o bloqueio estrutural geral por senha.", styles['CardBody'])
    t_sec = Table([[c1, c2]], colWidths=[360, 360])
    t_sec.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), card_bg),
        ('BOX', (0,0), (-1,-1), 1, border_gray),
        ('INNERGRID', (0,0), (-1,-1), 1, border_gray),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_sec)
    story.append(PageBreak())
    
    # ------------------ SLIDE 13: ÉTICA E LGPD ------------------
    story.append(Paragraph("Ética e LGPD Escolar", styles['SlideTitle']))
    story.append(Paragraph("A Segurança dos Dados Escolares é Inegociável", styles['SlideSubtitle']))
    story.append(Paragraph("Diários escolares carregam informações sensíveis que vão muito além de números: guardam CPFs de responsáveis, relatórios médicos, laudos de necessidades especiais e endereços residenciais.", styles['SlideText']))
    
    c_lgpd = Paragraph("<b>⚖️ Lei Geral de Proteção de Dados (LGPD) e Dever de Confidencialidade:</b><br/>Deixar planilhas sem senhas em computadores de uso coletivo, esquecer pen-drives em salas de professores ou enviar dados soltos por aplicativos viola a LGPD e fere a ética profissional docente. Tratar as planilhas com cuidado técnico é proteger a integridade moral da criança.", styles['CardBody'])
    t_lgpd = Table([[c_lgpd]], colWidths=[720])
    t_lgpd.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#FFF9F0")),
        ('BOX', (0,0), (-1,-1), 1.5, colors.HexColor("#FF8C00")),
        ('PADDING', (0,0), (-1,-1), 14),
    ]))
    story.append(t_lgpd)
    story.append(PageBreak())
    
    # ------------------ SLIDE 14: PROPÓSITO FINAL ------------------
    story.append(Paragraph("O Propósito Final", styles['SlideTitle']))
    story.append(Paragraph("A tecnologia a serviço do afeto e do cuidado pedagógico", styles['SlideSubtitle']))
    story.append(Spacer(1, 40))
    
    c_quote = Paragraph("<i>\"A tecnologia liberta o professor das planilhas manuais, devolvendo-lhe o tempo precioso que deve ser gasto com o afeto e a didática humana.\"</i>", ParagraphStyle('Quote', fontName='Times-Italic', fontSize=18, leading=24, textColor=green_hover, alignment=1))
    story.append(c_quote)
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>— Equipe de Coordenação Pedagógica</b>", ParagraphStyle('QuoteAuthor', fontName='Helvetica-Bold', fontSize=11, textColor=text_muted, alignment=1)))
    story.append(PageBreak())
    
    # ------------------ SLIDE 15: CERTIFICAÇÃO ------------------
    story.append(Paragraph("Certificação de Proficiência", styles['SlideTitle']))
    story.append(Paragraph("O reconhecimento formal das suas competências", styles['SlideSubtitle']))
    story.append(Paragraph("Ao finalizar com sucesso os 10 passos do Laboratório, o sistema emitirá automaticamente o seu Certificado de Literacia Docente.", styles['SlideText']))
    story.append(Paragraph("Este diploma é um atestado das suas novas habilidades de manipulação técnica, formatação de diários, integridade de dados e proteção escolar. Você poderá baixar a imagem de alta definição gerada em tempo real para compor sua pasta profissional.", styles['SlideText']))
    story.append(PageBreak())
    
    # ------------------ SLIDE 16: SUPORTE & AUTORIA ------------------
    story.append(Paragraph("Suporte Técnico & Autoria", styles['SlideTitle']))
    story.append(Paragraph("Os Responsáveis pelo Itinerário Extensionista", styles['SlideSubtitle']))
    story.append(Paragraph("Caso você precise de auxílio com a navegação do Laboratório de Literacia Docente ou possua sugestões para novas capacitações:", styles['SlideText']))
    
    c1 = Paragraph("<b>🛠️ Suporte Técnico</b><br/><font color='#107C41'><b>Gabriel H. Rodrigues</b></font><br/>Responsável técnico de TI, suporte ao ambiente virtual e correção de inconsistências do código.", styles['CardBody'])
    c2 = Paragraph("<b>✍️ Autor do Projeto</b><br/><font color='#107C41'><b>Juliano Prianti</b></font><br/>Docente Idealizador e Autor do Itinerário Extensionista de Capacitação e Literacia Digital Escolar.", styles['CardBody'])
    t_sup = Table([[c1, c2]], colWidths=[360, 360])
    t_sup.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), card_bg),
        ('BOX', (0,0), (-1,-1), 1, border_gray),
        ('INNERGRID', (0,0), (-1,-1), 1, border_gray),
        ('PADDING', (0,0), (-1,-1), 12),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
    ]))
    story.append(t_sup)
    story.append(PageBreak())
    
    # ------------------ SLIDE 17: PRÁTICA ------------------
    story.append(Paragraph("A Hora da Prática", styles['SlideTitle']))
    story.append(Paragraph("Você compreendeu a teoria. Agora, mãos na massa!", styles['SlideSubtitle']))
    story.append(Spacer(1, 40))
    story.append(Paragraph("A teoria foi absorvida com sucesso! Agora chegou a hora de aplicar suas habilidades. Acesse o nosso laboratório prático interativo do Microsoft Excel 365 e vença os 10 desafios!", styles['SlideText']))
    story.append(Spacer(1, 20))
    story.append(Paragraph("<b>🎮 ACESSE O AMBIENTE VIRTUAL DO SIMULADOR NA PÁGINA WEB!</b>", ParagraphStyle('PracticeText', fontName='Helvetica-Bold', fontSize=14, textColor=green_hover, alignment=1)))
    story.append(PageBreak())
    
    # ------------------ SLIDE 18: REFERÊNCIAS ------------------
    story.append(Paragraph("Referências e Créditos", styles['SlideTitle']))
    story.append(Paragraph("Fontes das Imagens e Elementos Visuais", styles['SlideSubtitle']))
    story.append(Paragraph("Todas as referências utilizadas para compor este itinerário são listadas abaixo:", styles['SlideText']))
    
    th_ref = ParagraphStyle('THR', fontName='Helvetica-Bold', fontSize=10, textColor=colors.white)
    
    ref_data = [
        [Paragraph("Origem / Fonte", th_ref), Paragraph("Endereço / Link da Imagem", th_ref)],
        [Paragraph("<b>Kinder Craze</b> (Sala de Computação)", cell_bold_style), Paragraph("<font color='#107C41'><u>https://kindercraze.com</u></font><br/>http://kindercraze.com/wp-content/uploads/2014/02/teachercomputer114.jpg", cell_normal_style)],
        [Paragraph("<b>Depict Data Studio</b> (Formatação Condicional)", cell_bold_style), Paragraph("<font color='#107C41'><u>https://depictdatastudio.com</u></font><br/>https://cdn.kicksdigital.com/depictdatastudio.com/2021/03/Conditional-Formatting_10.png", cell_normal_style)],
        [Paragraph("<b>Freepik</b> (Segurança & LGPD)", cell_bold_style), Paragraph("<font color='#107C41'><u>https://www.freepik.com</u></font><br/>https://img.freepik.com/premium-photo/cyber-security-data-protection-concept-with-digital-lock-circuit-background_136766-154.jpg", cell_normal_style)],
        [Paragraph("<b>Vecteezy</b> (Selo & Diploma 3D)", cell_bold_style), Paragraph("<font color='#107C41'><u>https://www.vecteezy.com</u></font><br/>https://static.vecteezy.com/system/resources/previews/045/907/692/non_2x/graduation-diploma-certificate-with-medal-and-cap-educational-achievement-3d-icon-realistic-vector.jpg", cell_normal_style)],
        [Paragraph("<b>Smith System</b> (Mobiliário Colaborativo)", cell_bold_style), Paragraph("<font color='#107C41'><u>https://smithsystem.com</u></font><br/>https://smithsystem.com/smithfiles/wp-content/uploads/sites/2/2015/09/2024-Cat-Elementary-copy-scaled.jpg", cell_normal_style)],
    ]
    
    t_refs = Table(ref_data, colWidths=[240, 480])
    t_refs.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), green_hover),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('PADDING', (0,0), (-1,-1), 6),
        ('GRID', (0,0), (-1,-1), 0.5, border_gray),
        ('BACKGROUND', (0,1), (-1,1), colors.white),
        ('BACKGROUND', (0,2), (-1,2), card_bg),
        ('BACKGROUND', (0,3), (-1,3), colors.white),
        ('BACKGROUND', (0,4), (-1,4), card_bg),
        ('BACKGROUND', (0,5), (-1,5), colors.white),
    ]))
    story.append(t_refs)
    
    # Construir PDF
    doc.build(story, canvasmaker=SlideCanvas)
    print(f"Sucesso: O PDF foi gerado em '{filename}'!")

if __name__ == "__main__":
    pdf_filename = "Apresentacao_Excel_para_Educadores.pdf"
    build_pdf(pdf_filename)
