# \# iFood Growth \& Portfolio Allocation Case (`ifood-growth-competition-case`)

# 

# \*\*Autor:\*\* Bernardo Akin Chiusoli Mendes  

# \*\*GitHub:\*\* \[@bernardochiusoli](https://github.com/bernardochiusoli)  

# 

# Projeto analítico de alocação estratégica de recursos de crescimento sob restrição orçamentária de até \*\*-R$ 10,00M na Operating Margin\*\*, cobrindo diagnóstico exploratório das 20 praças (`Case\_Competição\_prático - Dados.csv`), segmentação por arquétipos operacionais, modelagem de impacto ancorada nos custos unitários reais, otimização exata via Programação Linear Inteira Mista (MILP), análise de sensibilidade em 27 cenários e consolidação de entregáveis executivos.

# 

# > \*\*Confidencialidade:\*\* Repositório contendo análises técnicas e modelagem desenvolvidas para o case prático de Growth \& Estratégia.

# 

# \---

# 

# \## Resumo Executivo e Resultados Consolidados (Base Real)

# 

# \### Diagnóstico da Base (`Case\_Competição\_prático - Dados.csv`)

# \* \*\*Total de Praças Analisadas:\*\* 20 cidades (`City 1` a `City 20`)

# \* \*\*GMV Base Total (12m):\*\* \*\*R$ 1.388,68M\*\* (`17.844,02 mil` pedidos | Ticket Médio Ponderado: \*\*R$ 77,82\*\*)

# \* \*\*Margem de Contribuição Base:\*\* \*\*R$ 110,68M\*\* (`7,97%` ponderada)

# \* \*\*Operating Margin Base:\*\* \*\*R$ 55,36M\*\* (`3,99%` ponderada)

# \* \*\*Gargalo Estrutural Identificado:\*\* \*\*65,6% do GMV base\*\* está concentrado em praças operando acima da capacidade logística (`Saturação > 100%`, como `City 20` com `141,21%` e `City 17` com `131,38%`), exigindo \*\*destravamento de capacidade (oferta de entregadores)\*\* em vez de subsídio bruto de demanda.

# 

# \### Resultados do Portfólio Otimizado (12 Meses)

# \* \*\*Praças Selecionadas:\*\* \*\*6 cidades\*\* (`City 3`, `City 17`, `City 2`, `City 18`, `City 6` e `City 4`)

# \* \*\*Investimento Bruto Alocado:\*\* \*\*R$ 9,98M\*\* (respeitando o teto máximo de R$ 10,00M)

# \* \*\*Pedidos Incrementais Líquidos:\*\* \*\*+371,11 mil pedidos\*\* (já descontada canibalização de `15%`)

# \* \*\*GMV Incremental Projetado:\*\* \*\*+R$ 27,52M\*\* (\*\*ROI GMV de 2,76x\*\*)

# \* \*\*Margem de Contribuição Incremental:\*\* \*\*+R$ 2,22M\*\*

# \* \*\*Impacto Líquido na Operating Margin:\*\* \*\*-R$ 7,76M\*\* (folga de R$ 2,24M frente ao limite máximo de -R$ 10,00M)

# \* \*\*Robustez (Análise de Sensibilidade):\*\* \*\*100,0% dos 27 cenários\*\* simulados (variações de elasticidade, custo unitário e canibalização) respeitam o guardrail de `-R$ 10,00M` na Operating Margin, com GMV incremental variando entre \*\*R$ 20,72M\*\* (pessimista extremo) e \*\*R$ 34,97M\*\* (otimista extremo).

# 

# \---

# 

# \## Arquitetura e Estrutura do Repositório

# 

# ```text

# ifood-growth-competition-case/

# ├── data/

# │   ├── raw/

# │   │   └── Case\_Competição\_prático - Dados.csv      # Base original real (20 praças, 15 variáveis)

# │   └── processed/

# │       ├── base\_validada.csv                        # Saída do Notebook 01 (saneamento PT-BR e KPIs)

# │       ├── base\_segmentada.csv                      # Saída do Notebook 02 (arquétipos operacionais)

# │       ├── base\_impacto.csv                         # Saída do Notebook 03 (simulação por alavanca)

# │       └── base\_alocacao\_otimizada.csv              # Saída do Notebook 04 (portfólio ótimo MILP)

# ├── notebooks/

# │   ├── 01\_EDA.ipynb                                 # Análise exploratória, Pareto e auditoria de dados

# │   ├── 02\_Arquetipos.ipynb                          # Segmentação estratégica e guardrails de saturação

# │   ├── 03\_Impacto\_Alavancas.ipynb                   # Modelagem econômica com custos reais por cidade

# │   ├── 04\_Otimizacao.ipynb                          # Otimização exata (scipy.optimize.milp) <= R$ 10M

# │   ├── 05\_Sensibilidade.ipynb                       # Teste de estresse em 27 cenários combinados

# │   └── 06\_Entregaveis.ipynb                         # Consolidação do Excel executivo e gráficos finais

# ├── outputs/

# │   ├── excel/

# │   │   └── iFood\_Business\_Case\_Analitico\_Real.xlsx  # Workbook executivo multi-abas

# │   ├── figures/

# │   │   ├── 01\_pareto\_gmv.png                        # Curva de Pareto de GMV por praça

# │   │   ├── 01b\_saturacao\_vs\_margem.png              # Matriz Saturação Logística vs. Operating Margin

# │   │   ├── 02\_arquetipos\_operacionais.png           # Distribuição dos arquétipos estratégicos

# │   │   ├── 03\_oportunidades\_por\_alavanca.png        # GMV incremental potencial por alavanca viável

# │   │   ├── 04\_alocacao\_final.png                    # Portfólio ótimo selecionado

# │   │   ├── 05\_sensibilidade.png                     # Dispersão dos 27 cenários de estresse

# │   │   └── 06\_gmv\_incremental.png                   # Gráfico executivo final por praça e alavanca

# │   └── reports/

# │       ├── eda\_summary.json                         # KPIs consolidados da base real

# │       └── sensibilidade\_cenarios.csv               # Tabela completa dos 27 cenários simulados

# ├── .gitignore                                       # Arquivos ignorados pelo Git

# ├── requirements.txt                                 # Dependências Python do projeto

# └── README.md                                        # Documentação principal

