# Itinerário Extensionista - Excel para Educadores 📊🍎

Repositório contendo os recursos e a infraestrutura tecnológica do **Itinerário Extensionista de Capacitação e Literacia Digital Escolar**, voltado para a formação de educadores da rede municipal de ensino na ferramenta Microsoft Excel 365.

O projeto visa mitigar a sobrecarga burocrática dos professores (frequências, diários de classe, médias e conselhos), capacitando-os a automatizar planilhas e focar o tempo de ensino na mediação pedagógica.

---

## 🛠️ Componentes do Projeto

Este repositório unifica a vertente prática (simulador web) com a documental (geradores de materiais científicos e acadêmicos em formato PDF):

### 1. 🎮 Simulador Web Interativo (`index.html`)
*   **Descrição:** O "Laboratório de Literacia Docente" é um simulador web que recria a interface de planilhas eletrônicas. O professor enfrenta desafios práticos progressivos que emulam a rotina letiva (ex: cálculo de médias, frequências, formatação condicional) com feedback em tempo real de acertos, sons de sucesso e painéis de progresso.

### 2. 📄 Gerador de Documentação Científica NBR 14724 (`generate_documentation_pdf.py`)
*   **Descrição:** Script Python baseado na biblioteca `ReportLab` que renderiza a documentação acadêmica e conceitual do projeto, estruturada com capa, sumário e formatação estrita de margens (3cm esquerda/superior, 2cm direita/inferior) e cabeçalhos de paginação no topo conforme as normas da ABNT.
*   **Saída:** `Excel para Educadores Municipais.pdf`

### 3. 🖥️ Gerador de Slides Acadêmicos em Paisagem (`generate_slides_pdf.py`)
*   **Descrição:** Script Python que gera a apresentação de slides de apoio pedagógico utilizada na capacitação. Desenha um leiaute de paisagem com cabeçalho institucional, rodapé informando a autoria e numeração dinâmica de slides.
*   **Saída:** `Apresentacao_Excel_para_Educadores.pdf`

### 4. 🔀 Script de Injeção de Conteúdo (`inject_large_chapters.py`)
*   **Descrição:** Script auxiliar utilitário para enriquecer o arquivo `index.html` do simulador com textos de capítulos longos e detalhados de literacia digital por meio de expressões regulares.

---

## 📂 Estrutura de Arquivos

*   `index.html`: Simulador e apostila digital integrada de Literacia Digital Escolar.
*   `generate_documentation_pdf.py`: Script gerador do livro/livrete acadêmico em formato A4 Retrato (ABNT).
*   `generate_slides_pdf.py`: Script gerador dos slides de aula em formato A4 Paisagem.
*   `inject_large_chapters.py`: Utilitário de processamento de texto para o HTML.
*   `excel_logo.png`: Logotipo do Microsoft Excel usado nos materiais de apoio.
*   `*.pdf`: Documentações e apresentações compiladas para distribuição direta aos professores.

---

## 🚀 Como Executar

### 1. Pré-requisitos
*   Python 3.10 ou superior instalado localmente.
*   Navegador moderno de internet.

### 2. Instalando as Dependências de Geração
Para executar os geradores de PDF locais, instale a biblioteca ReportLab:
```bash
pip install reportlab
```

### 3. Gerando os Arquivos PDF Acadêmicos
Com a dependência instalada, execute os scripts de compilação:
```bash
python generate_documentation_pdf.py
python generate_slides_pdf.py
```
Os arquivos PDF serão gerados e atualizados instantaneamente no mesmo diretório.

### 4. Abrindo o Simulador
1.  Dê dois cliques no arquivo `index.html` para executá-lo diretamente em qualquer navegador moderno.
2.  Interaja com a grade de simulação, digite as fórmulas indicadas e teste seu progresso com base nos desafios fornecidos.
