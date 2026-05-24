# -*- coding: utf-8 -*-
import re
import os

html_path = r"c:\Users\Usuario\Desktop\Tarefa Excel Escola\index.html"

# Vamos definir textos extremamente longos, ricos e acadêmicos em Português para cada capítulo.
# Cada capítulo terá vários parágrafos, análise técnica aprofundada, passo a passo detalhado e
# 3 cenários práticos descritos por extenso para garantir o peso de 4 páginas de consulta por capítulo.

c0_full = """
<h1 class="abnt-h1">Capítulo 1: Introdução, Justificativa e Roteiro Metodológico</h1>
<p class="abnt-p">
    O <strong>Itinerário Extensionista de Capacitação e Literacia Digital Escolar</strong> surge como uma resposta direta às demandas contemporâneas por uma gestão educacional ágil, moderna e baseada em evidências científicas de aprendizagem. Nas redes públicas municipais, os docentes frequentemente enfrentam uma sobrecarga burocrática invisível, caracterizada pelo lançamento manual de frequências em diários de papel, cálculo de médias aritméticas em calculadoras portáteis e compilação manual de planilhas para conselhos de classe. Esse cenário drena o tempo que poderia ser dedicado ao planejamento didático e ao acolhimento dos estudantes.
</p>
<p class="abnt-p">
    Este projeto propõe uma abordagem inovadora de literacia de dados, em que a teoria pedagógica e a prática instrumental do software Microsoft Excel 365 são fundidas em um ambiente virtual de simulação em tempo real. A automação das planilhas liberta o educador da rotina burocrática repetitiva, garantindo que o cérebro humano seja empregado no afeto, no cuidado individualizado e nas metodologias ativas de ensino.
</p>
<div class="abnt-quote">
    "A literacia digital nas escolas públicas municipais ultrapassa o domínio instrumental de softwares e planilhas eletrônicas. Ela representa a emancipação intelectual e técnica do educador, capacitando-o a converter dados brutos em ações efetivas de resgate pedagógico e combate à evasão letiva crônica." (PRIANTI, 2026, p. 45)
</div>
<p class="abnt-p">
    Esta documentação científica serve como fonte de consulta eterna para os educadores da rede municipal de ensino. Ela foi estruturada sob a coordenação do docente e pesquisador idealizador <strong>Juliano Prianti</strong> (Autor do Itinerário) e contou com o suporte técnico e desenvolvimento de engenharia de software de <strong>Gabriel H. Rodrigues</strong> (Infraestrutura Virtual e TI).
</p>
<h2 class="abnt-h2">Roteiro Metodológico do Laboratório</h2>
<p class="abnt-p">
    O professor iniciará a capacitação realizando a leitura dirigida do sumário didático e passará em seguida para o <strong>Ambiente Virtual Simulador</strong>. O simulador recria a interface real do Microsoft Excel 365, apresentando desafios progressivos e fornecendo feedback de som de sucesso harmonioso e atualizações de progresso em tempo real, garantindo uma aprendizagem imersiva e autônoma.
</p>
"""

c0_sum = """
<h1 class="abnt-h1">Introdução e Roteiro Metodológico (Resumo)</h1>
<p class="abnt-p">
    Este documento apresenta o Itinerário de Literacia Digital em planilhas para educadores municipais, idealizado por <strong>Juliano Prianti</strong> com infraestrutura técnica de <strong>Gabriel H. Rodrigues</strong>. O projeto automatiza tarefas burocráticas escolares para liberar o tempo do docente para a mediação pedagógica, unindo a leitura de conceitos ao uso prático de um simulador online.
</p>
"""

c1_full = """
<h1 class="abnt-h1">Capítulo 2: O Poder das Planilhas Eletrônicas na Gestão Docente</h1>
<p class="abnt-p">
    O domínio das planilhas eletrônicas representa uma das competências fundamentais do docente do século XXI. No cenário educacional atual, a coleta e análise sistemática de dados de desempenho dos estudantes não é mais um diferencial, mas sim um requisito para planejar intervenções pedagógicas de sucesso. O Microsoft Excel 365 surge como um aliado indispensável, fundamentado em três pilares metodológicos:
</p>
<h2 class="abnt-h2">1. Otimização Radical do Tempo de Trabalho Extraclasse</h2>
<p class="abnt-p">
    Ao automatizar tarefas aritméticas rotineiras como a soma de faltas bimestrais e o cálculo de notas finais, o professor economiza dezenas de horas por semestre letivo. Esse tempo poupado atua diretamente na saúde mental do professor, prevenindo a síndrome de burnout e permitindo um melhor equilíbrio entre a vida pessoal e profissional do educador.
</p>
<h2 class="abnt-h2">2. Tomada de Decisões Baseada em Evidências Pedagógicas</h2>
<p class="abnt-p">
    Em vez de apoiar-se em intuições vagas sobre o progresso da sala de aula, o docente que domina planilhas consegue cruzar os resultados das avaliações formativas e somativas com descritores de aprendizagem específicos (como os do SAEB ou Prova Brasil). Isso permite diagnosticar e isolar com precisão quais as habilidades (ex: leitura de gráficos ou frações) que exigem reforço escolar imediato.
</p>
<h2 class="abnt-h2">3. Desburocratização e Integridade de Dados Fiscais e Escolares</h2>
<p class="abnt-p">
    Planilhas estruturadas reduzem a zero o índice de erro humano no preenchimento de atas de conselho de classe e boletins. Isso protege legalmente a escola e garante a integridade de dados que são repassados ao Censo Escolar e aos sistemas centrais da prefeitura, agilizando processos administrativos em tempo recorde.
</p>
"""

c1_sum = """
<h1 class="abnt-h1">O Poder do Excel para Educadores (Resumo)</h1>
<p class="abnt-p">
    O uso do Excel foca em três eixos centrais de empoderamento docente: otimização drástica de horas extras dedicadas a rotinas manuais burocráticas; fundamentação de diagnósticos pedagógicos baseados em dados científicos de avaliações formativas; e segurança administrativa no preenchimento de documentos oficiais da secretaria escolar.
</p>
"""

# Vamos gerar os 10 capítulos práticos dinamicamente com os mesmos detalhes massivos.
# Cada capítulo de 1 a 10 terá:
# - Uma explicação pedagógica longa (2-3 parágrafos)
# - Sintaxe detalhada por extenso
# - Roteiro passo a passo pedagógico (5 passos)
# - 3 Exemplos Escolares detalhadíssimos por extenso (cada exemplo em uma div .abnt-example-box)

chapters_data = [
    {
        "id": 1,
        "title": "1. Anatomia do Excel",
        "concept": """
            A interface operacional do Microsoft Excel 365 é estruturada sob um sistema de grade cartesiana, permitindo o armazenamento sistemático e cruzado de informações. A Fita de Opções (Ribbon) superior organiza os comandos em abas lógicas (como Página Inicial, Inserir, Dados e Revisão) para acesso rápido. As Colunas são representadas por letras maiúsculas e as Linhas por números inteiros. A célula é a menor unidade funcional da planilha, identificada pela interseção dessas coordenadas (ex: A1). A Barra de Fórmulas atua como o visor analítico de edição, revelando se a célula contém um dado estático ou o resultado de um cálculo dinâmico.
        """,
        "syntax": """
            Coordenada de Célula: <code>[Letra da Coluna][Número da Linha]</code>. Exemplo: a célula <code>B2</code> localiza-se na segunda coluna (B) e na segunda linha (2) da planilha de trabalho.
        """,
        "steps": """
            1. Identifique a Fita de Opções no topo para navegar nas guias de comando da planilha.<br/>
            2. Localize a Barra de Fórmulas branca e comprida logo abaixo do menu de opções.<br/>
            3. Visualize os Cabeçalhos de Coluna representados pelas letras (A, B, C...) no topo da grade.<br/>
            4. Localize os Cabeçalhos de Linha representados pelos números verticais (1, 2, 3...) à esquerda.<br/>
            5. Observe a Barra de Status no rodapé verde escuro para conferir o status do sistema.
        """,
        "ex1_title": "Exemplo 1: Mapeamento de Layout de Sala de Aula",
        "ex1_desc": "O docente organiza as coordenadas físicas das carteiras dos alunos na planilha usando o intervalo A1 a F6. Cada célula representa uma mesa específica na sala. O professor mapeia e altera rapidamente os assentos de alunos laudados ou com necessidades visuais e de atenção (AEE), integrando-os de forma estratégica e visual no espaço físico letivo de aprendizagem.",
        "ex2_title": "Exemplo 2: Registro de Carrinhos de Chromebooks e Equipamentos",
        "ex2_desc": "A equipe de coordenação cria uma planilha cadastral contendo colunas identificadoras (A: Código do Chromebook, B: Estado, C: Sala de Destino, D: Responsável). Cada linha representa um dispositivo do laboratório móvel, permitindo à secretaria escolar monitorar o histórico de empréstimo e conservação diária.",
        "ex3_title": "Exemplo 3: Planejador Semanal de Disciplinas e Horários",
        "ex3_desc": "Organizar o cronograma de conteúdos e turmas semanais da escola. As linhas representam os horários de aulas diários (1º horário, 2º horário...) e as colunas representam os dias da semana (Segunda a Sexta), gerando um mapa matricial limpo de atuação docente de cada professor.",
        "summary": "Mapeamento e reconhecimento dos componentes físicos e virtuais do Microsoft Excel 365, cobrindo fita de opções, barra de fórmulas, colunas, linhas e a barra de status verde escura. <strong>Exemplos:</strong> (1) Layout físico de sala (carteiras A1 a F6); (2) Controle de empréstimo de Chromebooks; (3) Grade horária semanal docente."
    },
    {
        "id": 2,
        "title": "2. Formatação Pedagógica",
        "concept": """
            A formatação pedagógica é a arte de organizar visualmente as informações de forma a facilitar a leitura rápida de boletins e chamadas, mitigando o cansaço dos professores. Um diário confuso, com fontes inadequadas e sem separações estruturais claras, induz o professor a registrar presenças ou notas nas linhas de alunos errados. O uso coerente da cor verde institucional, o ajuste correto de fontes, o alinhamento de texto e a aplicação sistemática de bordas de grade finas garantem total contraste e clareza, tornando a planilha utilizável off-line.
        """,
        "syntax": """
            Guia Página Inicial -> Preenchimento de Célula (Balde de Tinta) -> Cor Verde Escuro para cabeçalhos e Grade -> Todas as Bordas para linhas de dados.
        """,
        "steps": """
            1. Clique e arraste o mouse para selecionar o intervalo de células de cabeçalho A1:E1.<br/>
            2. Na aba Página Inicial, clique no ícone do Balde de Tinta e selecione a cor Verde Temática.<br/>
            3. Na mesma aba, mude a cor do texto para branco para garantir contraste ideal de leitura.<br/>
            4. Selecione a tabela de dados completa que deseja formatar com bordas.<br/>
            5. Clique no ícone de Bordas na Página Inicial e ative a opção 'Todas as Bordas'.
        """,
        "ex1_title": "Exemplo 1: Diário de Presença Escolar Legível",
        "ex1_desc": "Estilizar uma planilha de controle de chamada diária de 35 alunos aplicados ao cabeçalho (A1:E1) em verde escuro oficial e texto branco. A aplicação de bordas estruturais em todas as células de dados evita que o professor erre a linha de lançamento durante a chamada corrida na sala.",
        "ex2_title": "Exemplo 2: Destaque de Prazos de Entregas e Atividades",
        "ex2_desc": "O coordenador de projetos escolares cria uma planilha de cronograma e destaca as colunas de data limite de entrega com um preenchimento amarelo suave e texto em negrito escuro, separando prazos críticos de dados demográficos de forma rápida para visualização da direção.",
        "ex3_title": "Exemplo 3: Quadro de Níveis de Alfabetização Infantil",
        "ex3_desc": "Estruturar tabelas de leitura infantil utilizando fontes limpas de alta legibilidade (sans-serif) com margens internas largas nas células. Isso ajuda docentes da educação infantil a diagnosticar de forma visual e confortável o progresso em níveis de alfabetização periódica.",
        "summary": "Aplicação de cores institucionais (Verde Excel), contraste tipográfico de texto e bordas de grade estruturais para melhorar o fluxo visual de leitura das planilhas. <strong>Exemplos:</strong> (1) Cabeçalhos coloridos em chamada diária; (2) Destaque visual de prazos em amarelo; (3) Grades limpas de leitura na alfabetização."
    },
    {
        "id": 3,
        "title": "3. Cálculo de Média",
        "concept": """
            O cálculo automático de médias aritméticas representa o fim do uso de calculadoras externas e do retrabalho de digitação na secretaria escolar. A função matemática padrão soma dinamicamente os valores contidos em um intervalo vertical ou horizontal de células de notas e realiza a divisão pela quantidade exata de avaliações lançadas. O grande trunfo pedagógico da função reside no fato de que o Excel ignora automaticamente as células vazias, permitindo que alunos que perderam avaliações por ausência justificada não tenham sua média derrubada antes da prova substitutiva.
        """,
        "syntax": """
            <code>=MÉDIA(célula_inicial:célula_final)</code>. Exemplo: a fórmula <code>=MÉDIA(B2:E2)</code> realiza a soma das notas contidas nas células B2, C2, D2 e E2 e as divide por quatro.
        """,
        "steps": """
            1. Clique e selecione a célula onde o resultado final da média deve ser apresentado (F2).<br/>
            2. Localize a Barra de Fórmulas superior ou dê dois cliques rápidos na célula selecionada.<br/>
            3. Digite o sinal de igual (=) para abrir o editor e escreva a palavra 'MÉDIA' em maiúsculas e com acento.<br/>
            4. Abra parênteses, selecione o intervalo arrastando de B2 até E2, ou digite manualmente 'B2:E2'.<br/>
            5. Feche parênteses e pressione a tecla Enter para computar o resultado.
        """,
        "ex1_title": "Exemplo 1: Média Final de Arthur Silva",
        "ex1_desc": "O docente digita a fórmula exata <code>=MÉDIA(B2:E2)</code> na coluna de resultados, gerando de forma instantânea a média anual das notas dos 4 bimestres contidas nas células de Arthur Silva, obtendo a nota oficial letiva para o conselho de classe municipal sem risco de erro aritmético.",
        "ex2_title": "Exemplo 2: Média Geral da Classe em Matemática",
        "ex2_desc": "Computar a média final total de desempenho alcançada por uma turma inteira de 30 alunos em uma avaliação bimestral de Álgebra. O resultado permite à equipe docente avaliar se a didática aplicada atingiu o nível satisfatório ou exige readequações.",
        "ex3_title": "Exemplo 3: Consolidação de Notas de Projetos Multidisciplinares",
        "ex3_desc": "Mapear e tabular médias finais em projetos complexos ou Feiras de Ciências Escolares atribuindo pesos aritméticos ou somando as notas individuais da redação teórica, confecção de cartazes e apresentação oral em grupo de forma centralizada.",
        "summary": "Automatização aritmética de notas escolares com a função <code>=MÉDIA()</code>, calculando resultados sem risco de falha manual e ignorando lacunas temporárias. <strong>Exemplos:</strong> (1) Média final anual do discente Arthur Silva; (2) Desempenho médio de turma em prova letiva; (3) Notas de feira de ciências."
    },
    {
        "id": 4,
        "title": "4. Lógica Condicional",
        "concept": """
            A automação de tomadas de decisão pedagógicas assenta-se sobre a lógica condicional da função SE. Esta função atua como um juiz automatizado da planilha, realizando um teste lógico pré-estabelecido (como conferir se a nota é maior ou igual à nota de corte municipal). Se a condição for atendida (verdadeiro), o Excel exibe instantaneamente um texto ou executa um cálculo específico; se a condição for rejeitada (falso), exibe outra resposta diferente. Isso remove o trabalho manual e o erro emocional do professor.
        """,
        "syntax": """
            <code>=SE(teste_lógico; valor_se_verdadeiro; valor_se_falso)</code>. Exemplo: <code>=SE(F2>=6;"APROVADO";"RECUPERAÇÃO")</code> avalia a nota em F2 frente à média escolar.
        """,
        "steps": """
            1. Posicione seu cursor e selecione a célula de resultado da situação escolar (G2).<br/>
            2. Digite '=' e abra a função digitando 'SE' seguido de parênteses: '=SE('.<br/>
            3. Defina a condição lógica (ex: F2>=6) representando o teste de média do estudante.<br/>
            4. Digite ponto e vírgula (;) e escreva o resultado se verdadeiro entre aspas: '"APROVADO"'.<br/>
            5. Digite ponto e vírgula (;) e escreva o resultado se falso entre aspas: '"RECUPERAÇÃO"'. Feche parênteses.
        """,
        "ex1_title": "Exemplo 1: Situação Final de Aprovados ou em Recuperação",
        "ex1_desc": "O Excel avalia a média anual calculada em F2. Se a nota for maior ou igual a 6, o status exibe 'APROVADO' de forma imediata. Se a nota for menor que 6, estampa 'RECUPERAÇÃO', poupando o lançamento manual de 200 alunos um por um pelo professor.",
        "ex2_title": "Exemplo 2: Alertas de Infrequência e Notificação ao Conselho",
        "ex2_desc": "Mapear o risco de evasão legal nas turmas por meio da lógica: <code>=SE(H2<75%;\"Alertar Conselho\";\"Frequência Regular\")</code>. O Excel identifica de forma visual quais alunos ultrapassaram os limites legais de faltas permitidos pela LDB.",
        "ex3_title": "Exemplo 3: Controle e Reposição da Merenda Escolar",
        "ex3_desc": "O diretor de estoque de merenda insere na planilha a fórmula <code>=SE(Estoque<EstoqueMinimo;\"COMPRAR\";\"Regular\")</code> na coluna de insumos. A planilha gera avisos rápidos e automáticos de compras para garantir o almoço dos educandos.",
        "summary": "Configuração técnica da lógica condicional <code>=SE()</code> para classificar automaticamente a situação pedagógica e administrativa de estudantes e insumos. <strong>Exemplos:</strong> (1) Status de aprovado/recuperação; (2) Alertas de risco letivo de faltas LDB; (3) Estoque de merenda escolar."
    },
    {
        "id": 5,
        "title": "5. O Mapa de Calor",
        "concept": """
            A formatação condicional atua como um sistema de radar visual instantâneo para o professor. Em planilhas repletas de dezenas de números, o cérebro humano demora a identificar padrões críticos. Ao configurar regras que pintam automaticamente a cor de fundo das células com base em critérios pedagógicos definidos (como tons vermelhos para notas de perigo), as situações mais graves saltam aos olhos do professor em frações de segundos no conselho de classe, otimizando reuniões pedagógicas.
        """,
        "syntax": """
            Guia Página Inicial -> Formatação Condicional -> Regras de Realce das Células -> Menor do que... -> Inserir Nota de Alerta (5.0) -> Selecionar Estilo Vermelho Claro.
        """,
        "steps": """
            1. Selecione a coluna inteira contendo as notas que deseja mapear visualmente (coluna Média).<br/>
            2. Na fita superior Página Inicial, clique no botão destacado 'Formatação Condicional'.<br/>
            3. Navegue no menu flutuante até 'Regras de Realce das Células' e selecione 'Menor do que...'.<br/>
            4. No diálogo de preenchimento, digite o limite de nota escolar baixa (5.0).<br/>
            5. Selecione a formatação padrão 'Preenchimento Vermelho Claro e Texto Vermelho Escuro' e clique em OK.
        """,
        "ex1_title": "Exemplo 1: Alertas Visuais Vermelhos para Notas Baixas",
        "ex1_desc": "O professor aplica a regra na coluna de médias da turma. Imediatamente, as células contendo notas menores que 5.0 são coloridas em vermelho claro, revelando de forma visual instantânea quais estudantes estão em defasagem pedagógica e necessitam de triagem rápida.",
        "ex2_title": "Exemplo 2: Alertas Críticos de Faltas Escolares",
        "ex2_desc": "Destacar taxas de faltas acima de 25% com uma coloração alaranjada suave. Isso alerta o coordenador de forma imediata sobre a infrequência de alunos sob risco letivo que exige a busca ativa escolar municipal.",
        "ex3_title": "Exemplo 3: Mapeamento de Fila de Atendimento do AEE",
        "ex3_desc": "Utilizar cores personalizadas (Verde para 'Realizado', Vermelho para 'Pendente') no mapeamento do cronograma de apoios psicopedagógicos e adaptações curriculares do Atendimento Educacional Especializado (AEE) de alunos laudados.",
        "summary": "Uso estratégico de regras de Formatação Condicional para criar sinalizadores cromáticos que otimizam a triagem pedagógica no conselho de classe. <strong>Exemplos:</strong> (1) Destacar médias menores que 5.0 em vermelho; (2) Destacar faltas de risco em laranja; (3) Mapear cronogramas do AEE."
    },
    {
        "id": 6,
        "title": "6. Filtros de Evasão",
        "concept": """
            Os filtros são ferramentas robustas para gerenciar bancos de dados e isolar informações críticas no ambiente escolar. Em planilhas com centenas de linhas de matrículas de toda a escola municipal, a busca manual é ineficiente. A ativação de filtros de tabela permite ao gestor ou professor ocultar momentaneamente todas as linhas regulares de dados e concentrar a atenção unicamente em casos que exigem intervenção emergencial imediata, como a busca ativa.
        """,
        "syntax": """
            Guia Dados -> Ativar Filtro. Clicar no ícone de seta do filtro (▼) do cabeçalho da coluna Frequência -> Filtros de Número -> Menor do que -> Digitar o limite (75%).
        """,
        "steps": """
            1. Selecione o cabeçalho completo da sua tabela de chamada (A1:E1).<br/>
            2. Vá até a aba superior Dados da fita de opções e clique no botão com ícone de funil chamado 'Filtro'.<br/>
            3. Clique no pequeno triângulo com seta para baixo (▼) que surgiu na coluna da Frequência.<br/>
            4. No menu suspenso de filtragem, selecione 'Filtros de Número' e clique em 'Menor do que...'.<br/>
            5. Digite a porcentagem de risco letivo de faltas (75%) ou '0,75' e clique em OK para ocultar os frequentes.
        """,
        "ex1_title": "Exemplo 1: Isolamento de Alunos Infrequentes para Busca Ativa",
        "ex1_desc": "O assistente social da escola aciona o filtro de frequência menor que 75% na base geral. Instantaneamente, todos os alunos frequentes são ocultados e a planilha revela a lista exata e focada de estudantes com alto absenteísmo para visitas domiciliares.",
        "ex2_title": "Exemplo 2: Triagem de Alunos com Restrições Alimentares",
        "ex2_desc": "A coordenação de cozinha filtra a lista cadastral de matrículas escolares por termos de 'Restrições Alimentares' (ex: glúten, lactose), isolando os alunos alérgicos em segundos para repassar o cardápio e plano de preparo de almoço adaptado.",
        "ex3_title": "Exemplo 3: Listagem de Alunos do AEE Laudados",
        "ex3_desc": "Filtrar a base geral de matrículas municipais pelo campo 'Necessidades Especiais' ou 'Laudo', gerando em poucos cliques o censo interno direcionado para planejamento de verbas federais de acessibilidade.",
        "summary": "Uso de Filtros para gerenciar e isolar dados pedagógicos e demográficos prioritários, otimizando o envio de relatórios e busca ativa. <strong>Exemplos:</strong> (1) Filtrar frequências < 75% para busca ativa; (2) Isolar restrições alimentares de merenda; (3) Mapear estudantes laudados do AEE."
    },
    {
        "id": 7,
        "title": "7. O Localizador PROCV",
        "concept": """
            A função PROCV (Procura Vertical) atua como um sistema de busca analítico de alta eficiência dentro do Excel. Imagine procurar o CPF ou o contato do responsável de um aluno específico em uma lista geral contendo mais de mil cadastros. Em vez de percorrer a base manualmente, a fórmula localiza a informação desejada pesquisando verticalmente o nome do estudante na primeira coluna da esquerda e retornando o respectivo valor na mesma linha da coluna de resposta indicada.
        """,
        "syntax": """
            <code>=PROCV(valor_procurado; matriz_tabela; índice_coluna; procurar_intervalo)</code>. Exemplo: <code>=PROCV("Carlos";A2:B5;2;FALSO)</code> localiza a nota ou o CPF de Carlos no intervalo selecionado.
        """,
        "steps": """
            1. Selecione a célula de destino da consulta onde a resposta final deve surgir (B9).<br/>
            2. Digite '=' e inicie a fórmula digitando 'PROCV' seguido de parênteses: '=PROCV('.<br/>
            3. Insira o valor que deseja pesquisar de referência (ex: o nome do aluno entre aspas: '"Carlos"').<br/>
            4. Digite ';' e indique o intervalo completo da tabela de busca geral (ex: de A2 até B5: 'A2:B5').<br/>
            5. Digite ';' e informe o número do índice da coluna que contém a resposta (2). Digite ';FALSO' e feche parênteses.
        """,
        "ex1_title": "Exemplo 1: Extração Rápida de CPF de Alunos",
        "ex1_desc": "O docente digita <code>=PROCV(\"Carlos\";A2:B5;2;FALSO)</code> na aba de consultas da secretaria. O Excel varre a tabela cadastral de dados em segundos, extraindo com total integridade o número de CPF do aluno correspondente para emissão de histórico escolar.",
        "ex2_title": "Exemplo 2: Localizador de Livros Didáticos na Biblioteca",
        "ex2_desc": "Consultar de forma automatizada em qual estante, prateleira ou sala de leitura um exemplar de material pedagógico está armazenado, bastando que o professor ou aluno digite o título da obra na planilha do acervo.",
        "ex3_title": "Exemplo 3: Contato Telefônico Urgente de Pais ou Responsáveis",
        "ex3_desc": "Buscar o telefone de emergência do responsável pelo educando. Em situações de mal-estar súbito na sala, o professor digita o nome do aluno e obtém o número de contato telefônico do responsável de forma instantânea na secretaria.",
        "summary": "Implementação da busca vertical analítica com `=PROCV` para cruzar e resgatar dados demográficos com rapidez e sem margem de erro. <strong>Exemplos:</strong> (1) Buscar CPF de discentes por nome; (2) Localizar materiais pedagógicos na biblioteca; (3) Pesquisar telefones urgentes de pais."
    },
    {
        "id": 8,
        "title": "8. Integridade de Dados",
        "concept": """
            A integridade de dados é garantida pelo bloqueio preventivo de inconsistências operacionais na planilha. Erros acidentais de digitação (como digitar uma nota escolar como '11' por pressa ou cansaço) geram inconsistências graves nos boletins finais e dão margem a retrabalhos administrativos imensos na escola. A ferramenta Validação de Dados cria uma cerca de segurança digital na célula selecionada, permitindo apenas dados parametrizados e exibindo avisos sonoros e visuais personalizados de erro.
        """,
        "syntax": """
            Guia Dados -> Validação de Dados -> Configurar Critério para Decimal -> Mínimo: 0 -> Máximo: 10. Configurar Mensagem de Alerta de Erro personalizada.
        """,
        "steps": """
            1. Selecione a coluna completa de notas dos alunos que deseja proteger contra erros de digitação.<br/>
            2. Navegue até a aba superior Dados da fita e selecione o ícone de 'Validação de Dados'.<br/>
            3. Na janela de opções, vá em Permitir e selecione a modalidade 'Decimal'.<br/>
            4. Em Mínimo, digite a menor nota possível (0). Em Máximo, digite o limite superior oficial (10).<br/>
            5. Vá na aba Alerta de Erro, digite o título 'Erro de Secretaria', personalize a mensagem explicativa e clique em OK.
        """,
        "ex1_title": "Exemplo 1: Restrição Absoluta de Digitação de Notas Escolares",
        "ex1_desc": "Ao limitar as células para aceitarem apenas decimais de 0 a 10, a secretaria fica blindada de erros. Se um professor tentar registrar a nota 11 por desatenção, o Excel bloqueia o lançamento, soa um alerta e impede que a média fictícia seja impressa.",
        "ex2_title": "Exemplo 2: Inserção de Datas Restrita ao Calendário Letivo",
        "ex2_desc": "Configurar células de diário de bordo letivo para aceitarem datas compreendidas estritamente em dias úteis escolares homologados, rejeitando lançamentos em fins de semana ou recessos oficiais da rede pública.",
        "ex3_title": "Exemplo 3: Lista Suspensa de Segmentos e Anos Escolares",
        "ex3_desc": "Restringir o preenchimento de cadastros de novas matrículas escolares exigindo a seleção a partir de um menu de seleção contendo apenas as turmas pré-existentes (ex: 6º Ano A, 6º Ano B), padronizando a base geral.",
        "summary": "Blindagem de células com a ferramenta de Validação de Dados para impedir digitações incoerentes e garantir a integridade dos boletins. <strong>Exemplos:</strong> (1) Limitar notas exclusivamente de 0 a 10; (2) Restringir datas a dias de calendário letivo; (3) Listas suspensas de turmas."
    },
    {
        "id": 9,
        "title": "9. Gráficos de Tendência",
        "concept": """
            A comunicação estatística eficaz é a base para deliberações em conselhos de classe e devolutivas para as famílias. Apresentar tabelas volumosas e cheias de números para os pais dificulta a visualização de avanços escolares. Os gráficos convertem dados matemáticos complexos em representações visuais ágeis de impacto. Para dados cronológicos (evolução temporal), o Gráfico de Linhas é o modelo correto, pois desenha de forma instantânea a inclinação da aprendizagem ao longo do ano letivo.
        """,
        "syntax": """
            Selecionar Notas Cronológicas (Bimestres) -> Guia Inserir -> Inserir Gráfico de Linhas (Área de Tendências e Avanço).
        """,
        "steps": """
            1. Selecione na planilha o intervalo de células contendo as notas dos quatro bimestres do aluno.<br/>
            2. Vá na aba superior Inserir da fita de opções do simulador.<br/>
            3. No painel central de Gráficos, identifique o ícone contendo representações de linhas cruzadas.<br/>
            4. Clique em 'Gráfico de Linhas' e selecione o modelo de linha simples com marcadores em cada bimestre.<br/>
            5. Redimensione o gráfico gerado na tela ao lado da tabela de dados para visualização clara.
        """,
        "ex1_title": "Exemplo 1: Progressão de Notas Pós-Reforço Escolar",
        "ex1_desc": "Desenhar um gráfico de linhas temporais unindo o 1º ao 4º bimestre de um estudante. A linha ascendente ilustra visualmente para os pais a efetividade das aulas de recuperação ofertadas no contraturno escolar, gerando engajamento e apoio familiar.",
        "ex2_title": "Exemplo 2: Mapeamento de Fluxo e Evolução de Matrículas Escolares",
        "ex2_desc": "Construir um gráfico de colunas agrupadas para demonstrar à prefeitura municipal as taxas anuais de matrículas novas por segmento escolar nos últimos cinco anos letivos, embasando compras futuras de mobiliário.",
        "ex3_title": "Exemplo 3: Distribuição de Alunos por Níveis de Alfabetização",
        "ex3_desc": "Utilizar gráficos de barras para comparar o percentual de discentes considerados alfabetizados, silábicos e pré-silábicos entre turmas do mesmo ano no Fundamental I, norteando as metas da coordenação.",
        "summary": "Visualização dinâmica de dados com Gráficos temporais (Linhas) para evidenciar padrões e embasar decisões em reuniões escolares. <strong>Exemplos:</strong> (1) Curva linear de notas pós-recuperação; (2) Gráfico anual de fluxo de matrículas; (3) Gráfico de níveis de leitura infantil."
    },
    {
        "id": 10,
        "title": "10. Segurança Escolar",
        "concept": """
            A segurança da informação é um dever ético, técnico e legal inegociável de todo educador, amparado pela Lei Geral de Proteção de Dados (LGPD). Células contendo fórmulas lógicas e cálculos automáticos de boletins oficiais devem ser bloqueadas preventivamente para evitar a exclusão acidental por professores que utilizam o diário de forma compartilhada. A proteção por senha da pasta de trabalho garante sigilo legal aos cadastros sensíveis e impede violações.
        """,
        "syntax": """
            Formatar Células -> Proteção -> Marcar 'Bloqueada'. Guia Revisão -> Proteger Planilha -> Digitar Senha de Segurança Forte e Confirmar.
        """,
        "steps": """
            1. Selecione a coluna completa de células contendo as médias e status lógicos automáticos.<br/>
            2. Clique com botão direito (ou vá em Formatar), acesse a aba Proteção e marque a caixa 'Bloqueada'.<br/>
            3. Navegue na fita superior até a aba de controle de conteúdo chamada 'Revisão'.<br/>
            4. Clique no botão de destaque 'Proteger Planilha' localizado no menu superior.<br/>
            5. Digite uma senha segura de secretaria, confirme no diálogo e clique em OK para ativar o bloqueio letivo.
        """,
        "ex1_title": "Exemplo 1: Blindagem de Fórmulas Contra Exclusões Acidentais",
        "ex1_desc": "O diretor pedagógico marca as fórmulas automáticas como bloqueadas e ativa a proteção geral. Os docentes conseguem digitar livremente as notas do bimestre letivo, mas o sistema impede que as fórmulas sejam excluídas ou alteradas acidentalmente.",
        "ex2_title": "Exemplo 2: Criptografia e Envio Seguro de Boletins Oficiais",
        "ex2_desc": "Criptografar planilhas cadastrais contendo dados sensíveis de menores (como CPFs de responsáveis ou relatórios de apoio do AEE) com senha forte antes do repasse por e-mail, garantindo a confidencialidade legal sob a LGPD.",
        "ex3_title": "Exemplo 3: Direitos de Edição Segmentados por Disciplina",
        "ex3_desc": "Configurar intervalos de permissão de edição na nuvem municipal de forma que o professor de Matemática edite exclusivamente as células de sua coluna de notas, deixando as colunas de Geografia e História protegidas contra erros de escrita.",
        "summary": "Implementação do bloqueio preventivo de fórmulas e encriptação com senha de planilhas para garantir a integridade dos dados e conformidade ética com a LGPD. <strong>Exemplos:</strong> (1) Blindagem de colunas matemáticas; (2) Criptografia de dados sensíveis; (3) Permissões na nuvem."
    }
]
"""

# Vamos escrever a lógica de injeção desses dados de forma robusta e limpa em Python
# O script buscará as linhas onde `state.docChapters` é declarado e substituirá pela nova estrutura Docs-Style / Landing page com atalhos funcionais e textos longos de alta fidelidade pedagógica.

import json

# Vamos formatar os capítulos em strings Javascript seguras e sem colisão de crases nos códigos
# As crases internas no texto das sintaxes já foram substituídas por <code> nas strings python acima!

# Vamos construir o código Javascript contendo todo o state.docChapters
js_doc_chapters = "        state.docChapters = [\n"
for i, ch in enumerate(chapters_data):
    # Tratar e escapar as quebras de linhas nas strings python
    fullText_formatted = ch["concept"] + f"""
                    <h2 class="abnt-h2">Sintaxe / Diretrizes Técnicas</h2>
                    <p class="abnt-p">{ch["syntax"]}</p>
                    <h2 class="abnt-h2">Roteiro Passo a Passo Pedagógico</h2>
                    <p class="abnt-p">{ch["steps"]}</p>
                    <h2 class="abnt-h2">Cenários Práticos de Aplicação Diária Escolar</h2>
                    <div class="abnt-example-box">
                        <h5>{ch["ex1_title"]}</h5>
                        {ch["ex1_desc"]}
                    </div>
                    <div class="abnt-example-box">
                        <h5>{ch["ex2_title"]}</h5>
                        {ch["ex2_desc"]}
                    </div>
                    <div class="abnt-example-box">
                        <h5>{ch["ex3_title"]}</h5>
                        {ch["ex3_desc"]}
                    </div>
    """
    
    # Criar a string literal js
    js_doc_chapters += "            {\n"
    js_doc_chapters += f"                title: {json.dumps(ch['title'])},\n"
    js_doc_chapters += f"                fullText: `\n                    <h1 class=\"abnt-h1\">Capítulo {ch['id']+2}: {ch['title']}</h1>\n                    {fullText_formatted}\n                `,\n"
    js_doc_chapters += f"                summary: `\n                    <h1 class=\"abnt-h1\">{ch['title']} (Resumo)</h1>\n                    <p class=\"abnt-p\">\n                        {ch['summary']}\n                    </p>\n                `\n"
    js_doc_chapters += "            }"
    if i < len(chapters_data) - 1:
        js_doc_chapters += ",\n"
    else:
        js_doc_chapters += "\n"
js_doc_chapters += "        ];\n"

# Ler o arquivo index.html completo
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Encontrar e substituir state.docChapters e as funções de documentação
# Queremos substituir a declaração completa das funções e dados que inserimos
# O bloco começa em `// ================= SISTEMA DE DOCUMENTAÇÃO ABNT E DATASET =================`
# E vai até o início de `// Ativar/Desativar Tela Cheia para o Projetor`

# Vamos fazer uma busca regex robusta para encontrar esse bloco
pattern = r"// ================= SISTEMA DE DOCUMENTAÇÃO ABNT E DATASET =================.*?// Ativar/Desativar Tela Cheia para o Projetor"
match = re.search(pattern, html, re.DOTALL)
if not match:
    print("Bloco de documentação não encontrado com regex padrão. Vamos buscar por trecho.")
    exit(1)

# Vamos definir o novo bloco de substituição que conterá os novos dados gigantescos e a
# lógica Docs-style / Landing page de rolagem com atalhos!

novo_bloco = f"""// ================= SISTEMA DE DOCUMENTAÇÃO ABNT E DATASET =================
        state.selectedDocChapter = 0;
        state.isResumed = false;
        
        state.docChapters = [
            // Chapter 0 (Introdução)
            {{
                title: "Introdução e Roteiro Metodológico",
                fullText: `{c0_full}`,
                summary: `{c0_sum}`
            }},
            // Chapter 1 (Poder das Planilhas)
            {{
                title: "O Poder do Excel para Educadores",
                fullText: `{c1_full}`,
                summary: `{c1_sum}`
            }},
            // Os 10 Capítulos Técnicos
"""
# Remover o cabeçalho e rodapé de state.docChapters nas strings js geradas
js_doc_chapters_cleaned = js_doc_chapters.replace("        state.docChapters = [\n", "").replace("        ];\n", "")
novo_bloco += js_doc_chapters_cleaned
novo_bloco += """        ];

        // Transição: Qualquer -> Documentação ABNT
        function goToDocumentation() {
            initAudio();
            playSuccessSound();
            
            const presContainer = document.getElementById("presentation-container");
            const appContainer = document.getElementById("app-container");
            const docContainer = document.getElementById("documentation-container");
            
            presContainer.style.opacity = "0";
            appContainer.style.opacity = "0";
            
            setTimeout(() => {
                presContainer.classList.add("hidden");
                appContainer.classList.add("hidden");
                
                docContainer.classList.remove("hidden");
                docContainer.style.opacity = "0";
                
                // Forçar redesenho (reflow)
                docContainer.offsetHeight;
                
                docContainer.style.opacity = "1";
                docContainer.style.transition = "opacity 0.3s ease";
                
                // Renderizar o conteúdo total Docs-style
                renderDocumentation();
            }, 300);
        }

        // Transição: Documentação -> Slides
        function goBackFromDoc() {
            initAudio();
            
            const presContainer = document.getElementById("presentation-container");
            const docContainer = document.getElementById("documentation-container");
            
            docContainer.style.opacity = "0";
            setTimeout(() => {
                docContainer.classList.add("hidden");
                presContainer.classList.remove("hidden");
                presContainer.style.opacity = "0";
                
                // Forçar redesenho (reflow)
                presContainer.offsetHeight;
                
                presContainer.style.opacity = "1";
                presContainer.style.transition = "opacity 0.3s ease";
                
                renderActiveSlide();
            }, 300);
        }

        // Renderização Docs-Style / Landing Page (Todos os tópicos em uma página longa de rolagem com atalhos)
        function renderDocumentation() {
            const menuContainer = document.getElementById("doc-menu-items");
            const paperContainer = document.getElementById("doc-paper-content");
            if (!menuContainer || !paperContainer) return;
            
            // 1. Renderizar Menu lateral (Outline de atalhos)
            menuContainer.innerHTML = "";
            state.docChapters.forEach((chapter, idx) => {
                const menuItem = document.createElement("div");
                menuItem.className = `doc-menu-item ${idx === state.selectedDocChapter ? 'active' : ''}`;
                menuItem.innerHTML = `<span>📄</span> ${chapter.title}`;
                menuItem.addEventListener("click", () => {
                    initAudio();
                    state.selectedDocChapter = idx;
                    
                    // Destacar ativo no menu
                    document.querySelectorAll(".doc-menu-item").forEach((item, i) => {
                        if (i === idx) item.classList.add("active");
                        else item.classList.remove("active");
                    });
                    
                    // Rolar suavemente até a seção correspondente no documento Docs-style
                    const targetEl = document.getElementById(`doc-sec-${idx}`);
                    if (targetEl) {
                        targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
                    }
                });
                menuContainer.appendChild(menuItem);
            });
            
            // 2. Renderizar TODOS os capítulos no mesmo papel (Docs-style / Landing page de rolagem)
            let fullHTML = "";
            state.docChapters.forEach((chapter, idx) => {
                const htmlContent = state.isResumed ? chapter.summary : chapter.fullText;
                fullHTML += `
                    <section id="doc-sec-${idx}" class="doc-section-page" style="margin-bottom: 50px;">
                        ${htmlContent}
                        
                        <div class="no-print" style="margin: 40px 0; border-top: 1px dashed var(--excel-border); height: 1px;"></div>
                        <div class="page-break" style="page-break-after: always;"></div>
                    </section>
                `;
            });
            
            paperContainer.innerHTML = `
                <div class="abnt-text">
                    ${fullHTML}
                    
                    <!-- Rodapé Acadêmico no rodapé do documento longo -->
                    <div style="font-size: 9pt; text-align: center; color: #777777; margin-top: 50px; line-height: 1.4; border-top: 1px solid #CCCCCC; padding-top: 15px;" class="academic-footer">
                        <strong>Rede Municipal de Educação — Capacitação Permanente em Literacia Digital</strong><br>
                        Autor do Itinerário: Juliano Prianti | Suporte e TI: Gabriel H. Rodrigues<br>
                        <em>Padrão Científico de Formatação NBR/ABNT — Documento de Consulta Permanente</em>
                    </div>
                </div>
            `;
            
            // 3. Atualizar botão de visualização/versão
            const toggleIcon = document.getElementById("doc-version-icon");
            const toggleText = document.getElementById("doc-version-text");
            if (toggleIcon && toggleText) {
                if (state.isResumed) {
                    toggleIcon.innerText = "📄";
                    toggleText.innerText = "Versão Completa";
                } else {
                    toggleIcon.innerText = "📝";
                    toggleText.innerText = "Versão Resumida";
                }
            }
        }

        function toggleDocVersion() {
            initAudio();
            state.isResumed = !state.isResumed;
            renderDocumentation();
        }

        function printDocSummary() {
            initAudio();
            const wasResumed = state.isResumed;
            
            // Forçar modo resumido para a impressão
            state.isResumed = true;
            renderDocumentation();
            
            // Executar window.print()
            setTimeout(() => {
                window.print();
                
                // Restaurar o modo anterior de tela após fechar a tela de impressão
                state.isResumed = wasResumed;
                renderDocumentation();
            }, 100);
        }

        // Ativar/Desativar Tela Cheia para o Projetor"""

# Substituir no HTML
html_novo = html.replace(match.group(0), novo_bloco)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_novo)

print("Injeção realizada com sucesso! HTML atualizado com textos longos e rolagem Docs-style!")
