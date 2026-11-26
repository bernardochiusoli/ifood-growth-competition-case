# Case de Negócio iFood — Alocação de Investimentos (-R$ 10.000.000,00 na Operating Margin)

**Autor:** Bernardo Akin Chiusoli Mendes · Estratégia de Crescimento, Alocação de Portfólio e Engenharia de Dados

## Problema de Negócio e Resultado Principal

Diante do desafio de acelerar crescimento em 20 praças heterogêneas sem comprometer a disciplina financeira, este projeto modela a alocação ótima de capital respeitando a exigência de alocar **exatamente -R$ 10.000.000,00** de impacto líquido na *Operating Margin*. O portfólio aprovado concentra recursos em **5 cidades ativas** (`City 3`, `City 2`, `City 18`, `City 6` e `City 17`), gerando **+R$ 26,08M** em GMV incremental (`2,35x`) e **+352,7 mil** pedidos incrementais líquidos.

> **Tese Central:** O portfólio aloca **R$ 11,12M** de custo bruto para gerar **R$ 26,08M** de GMV incremental, **352,7 mil** pedidos incrementais líquidos e **R$ 2,10M** de margem de contribuição incremental. Após **R$ 0,98M** de custos operacionais e de SLA, o impacto líquido na *Operating Margin* fecha em **exatamente -R$ 10.000.000,00**. O retorno marginal é de **R$ 0,19** de MC incremental por R$ 1 investido (**2,35x** de múltiplo de GMV).

---

## KPIs Finais Consolidados (Portfólio Aprovado)

| Indicador | Valor Consolidado | Detalhamento |
| :--- | :--- | :--- |
| **Cidades Ativas** | **5 cidades** | `City 3`, `City 2`, `City 18`, `City 6` e `City 17` |
| **Investimento Bruto Total** | **R$ 11.115.969,51** | Desembolso direto nas 4 alavancas selecionadas (`R$ 11,12M`) |
| **Pedidos Incrementais Líquidos** | **352.703,38** | Volume líquido após canibalização (`8%`–`22%`) e fator de realização (`92%` em `City 17`) |
| **GMV Incremental** | **R$ 26.079.593,78** | Calculado sobre o AOV real auditado de cada praça (`+R$ 26,08M`) |
| **MC Incremental** | **R$ 2.100.205,24** | Calculado sobre a taxa real de margem de contribuição de cada praça (`+R$ 2,10M`) |
| **Custo Operacional / SLA** | **R$ 984.235,73** | Inclui custos operacionais incrementais e `R$ 25.000,00` de SLA extra em `City 6` |
| **Impacto Líquido na Operating Margin** | **-R$ 10.000.000,00** | Soma algébrica exata exigida pela restrição do case (`-R$ 10,00M`) |
| **MC Incremental por R$ 1 Bruto** | **R$ 0,1889** | Eficiência marginal de contribuição (`MC Incremental / Investimento Bruto`) |
| **Múltiplo de GMV** | **2,35x** | Eficiência comercial (`GMV Incremental / Investimento Bruto`) |
| **Operating Margin Consolidada** | **R$ 55,36M → R$ 45,36M** | De **3,99%** (sobre GMV base de `R$ 1.388,68M`) para **3,21%** (pós-investimento) |

---

## Alocação Detalhada por Praça (Validação Contábil)

| Cidade | Arquétipo | Alavanca | Custo Bruto | Ajuste de Volume | Pedidos Incr. Líq. | GMV Incremental | MC Incremental | Custo Op./SLA | Impacto Líquido OM |
| :--- | :--- | :--- | ---: | :--- | ---: | ---: | ---: | ---: | ---: |
| **City 3** | Ataque | Incentivos para clientes | R$ 2.750.000,00 | Canibalização: 18% | 99.220,00 | R$ 7.639.940,00 | R$ 628.003,07 | R$ 192.500,00 | -R$ 2.314.496,93 |
| **City 2** | Ataque | Alterações de preço | R$ 2.250.000,00 | Canibalização: 12% | 71.280,00 | R$ 5.132.160,00 | R$ 459.841,54 | R$ 135.000,00 | -R$ 1.925.158,46 |
| **City 18** | Ataque (Exceção Share) | Incentivos para clientes | R$ 1.750.000,00 | Canibalização: 18% | 63.140,00 | R$ 4.167.240,00 | R$ 321.710,93 | R$ 122.500,00 | -R$ 1.550.789,07 |
| **City 6** | Ataque | Frete grátis | R$ 1.700.000,00 | Canibalização: 22% | 50.388,00 | R$ 3.577.548,00 | R$ 280.122,01 | R$ 161.000,00 | -R$ 1.580.877,99 |
| **City 17** | Capacidade | Capacidade logística | R$ 2.665.969,51 | Fator de realização: 92% | 68.675,38 | R$ 5.562.705,78 | R$ 410.527,69 | R$ 373.235,73 | -R$ 2.628.677,55 |
| **TOTAL** | **5 Cidades Ativas** | **4 Alavancas** | **R$ 11.115.969,51** | — | **352.703,38** | **R$ 26.079.593,78** | **R$ 2.100.205,24** | **R$ 984.235,73** | **-R$ 10.000.000,00** |

---

## Fundamentos Econômicos e Guardrails Operacionais

1. **Investimento Bruto (`R$ 11,12M`) vs. Impacto Líquido na Operating Margin (`-R$ 10,00M`):** A equação contábil de cada praça segue `Impacto Líquido OM = MC Incremental - Custo Bruto - Custo Operacional/SLA`. Os `+R$ 2,10M` de margem de contribuição incremental absorvem parte do desembolso bruto (`R$ 11,12M`) e dos custos operacionais/SLA (`R$ 0,98M`), fazendo o resultado líquido consolidado fechar em **exatamente -R$ 10.000.000,00**.
2. **Interpretação de `R$ 0,1889` (MC Incremental / R$ 1):** Esse indicador mede a eficiência marginal de contribuição por real bruto investido (`R$ 2,10M / R$ 11,12M`), **não** representando ROI financeiro líquido positivo no curto prazo — trata-se de investimento deliberado em crescimento e defesa de participação dentro do orçamento autorizado.
3. **Inclusão de `City 18` como exceção estratégica de ataque de share:** Sob a regra de materialidade atualizada (`GMV >= R$ 50M OU praça com folga logística, market share baixo e retorno marginal positivo`), `City 18` (`GMV` de `R$ 41,92M`) é aprovada por deter o menor *market share* da base (`65,00%`), ampla folga operacional (`78,48%` de saturação) e retorno marginal atrativo (`R$ 0,1838` MC/R$; `2,38x` GMV).
4. **`City 17` recebe capacidade logística, e não cupom genérico:** Com saturação base de `131,38%` (`1.524.881,30` pedidos equivalentes de capacidade), estimular demanda geraria atraso e cancelamento. O aporte de `R$ 2.665.969,51` adiciona `+180.000,00` pedidos equivalentes (`+11,80%` sobre a capacidade base) e aplica **fator de realização de 92%** sobre a capacidade destravada, reduzindo a saturação projetada de `135,88%` (sem intervenção) para `121,54%` (`-14,35 p.p.`).
5. **`City 6` permanece abaixo de `98%` com folga operacional estreita (`0,46 p.p.`):** Parte de `96,50%` e atinge `97,54%` após frete grátis focalizado (sem expansão de frota), incorporando `R$ 25.000,00` de reforço extra de SLA (`R$ 161.000,00` totais). Exige monitoramento semanal e gatilho automático de pausa caso ultrapasse `98,00%`.
6. **Cenário adverso como teste de estresse (não aprovado):** O **Cenário Base (`-R$ 10,00M` líquidos)** é a única alocação aprovada. O **Cenário Adverso** (`-20%` de volume / `+15%` de custo, simulando `-R$ 12,24M` líquidos) funciona como teste de estresse para acionar gatilhos de governança: pausar incentivos de menor MC/R$, priorizar `City 2` e `City 3`, recalibrar `City 17` se o SLA não responder e revisar a carteira mensalmente.

---

## Estrutura do Repositório

```text
ifood-growth-competition-case/
├── dashboard/
│   └── app.py                                       # Aplicação interativa Streamlit
├── data/
│   ├── raw/
│   │   └── Case_Competição_prático - Dados.csv      # Base original (20 praças, 15 variáveis)
│   └── processed/
│       ├── base_validada.csv                        # Auditoria e métricas derivadas (Notebook 01)
│       ├── base_segmentada.csv                      # Arquétipos e exceção City 18 (Notebook 02)
│       ├── base_impacto.csv                         # Simulação por alavanca (Notebook 03)
│       └── base_alocacao_otimizada.csv              # Portfólio aprovado de 5 cidades (Notebook 04)
├── notebooks/
│   ├── 01_EDA.ipynb                                 # Auditoria da base real (City 9 em 165,28%, etc.)
│   ├── 02_Segmentacao.ipynb                         # Segmentação estratégica e guardrails
│   ├── 03_Impacto_Alavancas.ipynb                   # Elasticidade, canibalização e fator de realização
│   ├── 04_Otimizacao.ipynb                          # Validação contábil (-R$ 10.000.000,00)
│   ├── 05_Sensibilidade.ipynb                       # Cenários base, adverso e otimista
│   └── 06_Entregaveis.ipynb                         # Consolidação de KPIs e gráficos executivos
├── outputs/
│   ├── excel/
│   │   └── iFood_Business_Case_Analitico_Real.xlsx  # Modelo Excel multi-abas auditado
│   ├── figures/                                     # Gráficos analíticos PNG (300 DPI)
│   └── reports/                                     # kpis_finais_consolidados.csv, sensibilidade e JSON
├── iFood_Apresentacao_Growth_Competicao.pptx        # Apresentação executiva (7 slides)
├── requirements.txt                                 # Dependências Python
└── README.md                                        # Documentação executiva do projeto
