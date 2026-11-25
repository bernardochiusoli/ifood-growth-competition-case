# iFood Growth & Portfolio Allocation Case

**Bernardo Akin Chiusoli Mendes** · Business Analytics & Strategy | [GitHub](https://github.com/bernardochiusoli)

Modelagem analítica e otimização de alocação de capital de crescimento sob restrição orçamentária de até **-R$ 10,00M na Operating Margin**, cobrindo diagnóstico operacional das 20 praças (`Case_Competição_prático - Dados.csv`), segmentação por arquétipos, modelagem econômica ancorada em custos unitários reais, programação linear inteira mista (MILP) e análise de sensibilidade em 27 cenários.

> **Nota:** Repositório contendo a arquitetura analítica, notebooks auditáveis e entregáveis executivos desenvolvidos para o case prático de Growth & Estratégia.

### 1. Diagnóstico da Base Real (`Case_Competição_prático - Dados.csv`)

A auditoria das 20 praças (15 variáveis operacionais e financeiras) revela alta concentração de receita e um gargalo estrutural de capacidade logística nos horários de pico:

| Métrica Consolidada (12 Meses) | Valor Auditado | Observação Operacional |
| :--- | :---: | :--- |
| **GMV Base Total** | **R$ 1.388,68M** | `City 20` concentra **45,78%** (`R$ 635,78M`); top 7 praças somam **83,79%** |
| **Pedidos Base Totais** | **17.844,02 mil** | Ticket médio ponderado de **R$ 77,82** (`AOV Basket` médio de R$ 62,20) |
| **Margem de Contribuição** | **R$ 110,68M** | **7,97%** ponderada sobre o GMV |
| **Operating Margin** | **R$ 55,36M** | **3,99%** ponderada (variando de `-4,69%` em `City 18` a `11,21%` em `City 5`) |
| **Gargalo de Saturação** | **65,6% do GMV** | 7 praças operam com **saturação > 100%** (ex.: `City 20` em `141,21%` e `City 17` em `131,38%`) |

**Tese Estratégica (Oferta antes de Demanda):** Em praças operando acima de 100% de saturação, subsídios brutos de demanda (cupons/frete grátis) degradam margem e SLA. O modelo aplica guardrails rígidos que bloqueiam estímulos de demanda em cidades saturadas, direcionando capital para **destravamento de capacidade (incentivos a entregadores)** onde há gargalo e **captura seletiva de share** onde há folga logística e margem saudável.

### 2. Resultados do Portfólio Otimizado (MILP)

A otimização exata (`scipy.optimize.milp`) selecionou **6 praças complementares** dentro do limite orçamentário:

| Indicador de Performance (12m) | Resultado Projetado | Guardrail / Referência |
| :--- | :---: | :--- |
| **Praças Selecionadas** | **6 cidades** | `City 3`, `City 17`, `City 2`, `City 18`, `City 6` e `City 4` |
| **Investimento Bruto Alocado** | **R$ 9,98M** | Teto máximo de R$ 10,00M |
| **Pedidos Incrementais Líquidos** | **+371,11 mil** | Já descontada canibalização de `15%` |
| **GMV Incremental Projetado** | **+R$ 27,52M** | **ROI GMV de 2,76x** (`+1,98%` sobre o GMV base) |
| **Margem de Contribuição Incremental** | **+R$ 2,22M** | Retorno operacional direto antes do custo de incentivo |
| **Impacto Líquido na Operating Margin** | **-R$ 7,76M** | Folga de **R$ 2,24M** frente ao limite de `-R$ 10,00M` |
| **Robustez (27 Cenários)** | **100,0% aprovados** | GMV incremental entre **R$ 20,72M** (pessimista) e **R$ 34,97M** (otimista) |

### 3. Estrutura do Repositório

<details>
<summary><strong>Clique para expandir a arquitetura de diretórios e entregáveis</strong></summary>

```text
ifood-growth-competition-case/
├── data/
│   ├── raw/
│   │   └── Case_Competição_prático - Dados.csv      # Base original real (20 praças, 15 variáveis)
│   └── processed/
│       ├── base_validada.csv                        # Saneamento PT-BR e KPIs canônicos (Notebook 01)
│       ├── base_segmentada.csv                      # Arquétipos e elegibilidade operacional (Notebook 02)
│       ├── base_impacto.csv                         # Simulação econômica por alavanca (Notebook 03)
│       └── base_alocacao_otimizada.csv              # Portfólio ótimo MILP (Notebook 04)
├── notebooks/
│   ├── 01_EDA.ipynb                                 # Auditoria, Pareto de GMV e matriz de saturação
│   ├── 02_Arquetipos.ipynb                          # Regras de segmentação e guardrails de oferta
│   ├── 03_Impacto_Alavancas.ipynb                   # Modelagem financeira com custos reais por praça
│   ├── 04_Otimizacao.ipynb                          # Otimização restrita (scipy.optimize.milp)
│   ├── 05_Sensibilidade.ipynb                       # Teste de estresse em 27 cenários combinados
│   └── 06_Entregaveis.ipynb                         # Geração do workbook Excel e gráficos executivos
├── outputs/
│   ├── excel/
│   │   └── iFood_Business_Case_Analitico_Real.xlsx  # Workbook executivo multi-abas
│   ├── figures/                                     # Gráficos analíticos de alta resolução (PNG)
│   └── reports/                                     # Sumário JSON (EDA) e matriz de sensibilidade (CSV)
├── requirements.txt
└── README.md
