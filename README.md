iFood Business Case — Alocação de Investimentos (-R$ 10,00M na Operating Margin)
Bernardo Akin Chiusoli Mendes · Análise, Estratégia de Negócios e Engenharia de Dados | GitHub
Modelagem analítica e alocação de capital de crescimento sob restrição orçamentária de até -R$ 10,00M na Operating Margin, cobrindo auditoria e diagnóstico das 20 praças (`Case_Competição_prático - Dados.csv`), segmentação e guardrails de capacidade/saturação, simulação de impacto por alavanca, validação contábil linha por linha, análise de sensibilidade e geração dos entregáveis executivos.
---
Tese Executiva Final
> “O portfólio aloca **R$ 11,12M** de custo bruto para gerar **R$ 26,08M** de GMV incremental, **352,7 mil** pedidos incrementais líquidos e **R$ 2,10M** de margem de contribuição incremental. Após custos operacionais e de SLA, o impacto líquido na Operating Margin é exatamente **-R$ 10M**, conforme a restrição do case. O retorno é de **R$ 0,19** de MC incremental por R$ 1 de incentivo e **2,35x** de múltiplo de GMV.”
---
Reprodutibilidade e Execução (Google Colab ou Ambiente Local)
Este projeto foi desenvolvido com integração ao Google Drive para persistência de artefatos no Google Colab, mas pode ser executado localmente ou em outro ambiente sem necessidade de acesso ao Drive do autor, desde que o diretório raiz do projeto seja o diretório de trabalho (`cwd`):
Clonar o repositório e acessar a pasta raiz:
```bash
   git clone https://github.com/bernardochiusoli/ifood-growth-competition-case.git
   cd ifood-growth-competition-case
   ```
Execução local (Jupyter / VS Code / Python):
Abra e execute os notebooks na ordem (`01_EDA.ipynb` a `06_Entregaveis.ipynb`) a partir da raiz do repositório (`cwd`).
Os arquivos gerados e consolidados ficam em `data/processed/` e `outputs/` (`outputs/reports/`, `outputs/figures/`, `outputs/excel/`).
Execução no Google Colab (sem montar um Drive pessoal):
Caso execute sem montar um Google Drive pessoal, ajuste `PROJECT_DIR` para o diretório atual (`os.getcwd()`) após carregar os arquivos/repositório na sessão do Colab.
---
Diagnóstico da Base Real (20 Cidades, 12m)
A auditoria da base real (`Case_Competição_prático - Dados.csv`) nas 20 praças evidencia forte concentração de volume e gargalos logísticos de saturação em cidades relevantes:
Total Base do GMV: `R$ 1.388.681.883,00` (`R$ 1.388,68M`) em 12 meses (`City 20` concentra `45,78%` / `R$ 635,78M`).
Pedidos Base Totais: `17.844.024,78` pedidos (`AOV` ponderado de `R$ 77,82`).
Margem de Contribuição Base: `R$ 110.679.061,46` (`R$ 110,68M`, `7,97%` ponderada sobre o GMV).
Operating Margin Base: `R$ 55.355.277,41` (`R$ 55,36M`, `3,99%` ponderada sobre o GMV base, variando de `-4,69%` em `City 18` a `11,21%` em `City 5`).
Dinâmica de capacidade e saturação: Praças com saturação acima de `100%` (como `City 20` em `141,21%` e `City 17` em `131,38%`) exigem reforço de capacidade logística em vez de estímulo genérico de demanda.
---
KPIs Finais Consolidados (Portfólio Aprovado: 5 Cidades Ativas)
Indicador	Valor Consolidado	Observação
Cidades Ativas	5 cidades	`City 3`, `City 2`, `City 18`, `City 6` e `City 17`
Investimento Bruto Total	R$ 11.115.969,51 (`R$ 11,12M`)	Desembolso direto nas 5 alavancas selecionadas
Pedidos Incrementais Líquidos	352.703,38 (`+352,70 mil`)	Descontada canibalização específica por alavanca (`8%` a `22%`)
GMV Incremental	R$ 26.079.593,78 (`+R$ 26,08M`)	Calculado sobre AOV real auditado de cada praça
MC Incremental	R$ 2.100.205,24 (`+R$ 2,10M`)	Calculado sobre taxa de MC real de cada praça
Custo Operacional / SLA	R$ 984.235,73 (`R$ 0,98M`)	Inclui custo incremental de operação/SLA e `R$ 25.000,00` de SLA extra em `City 6`
Impacto Líquido na Operating Margin	-R$ 10.000.000,00 (`-R$ 10,00M`)	Soma algébrica exata exigida pela restrição do case
MC Incremental por R$ 1 de Custo Bruto	R$ 0,1889	Eficiência marginal de contribuição (não é ROI financeiro líquido positivo)
Múltiplo de GMV	2,35x	`GMV Incremental / Investimento Bruto`
Operating Margin Consolidada	R$ 55,36M → R$ 45,36M	De 3,99% (sobre GMV base) para 3,21% (sobre GMV pós-investimento)
---
Tabela Final de Alocação e Soma Algébrica
Cidade	Classificação	Alavanca	Custo Bruto	Pedidos Incr. Líq.	GMV Incremental	MC Incremental	Custo Op./SLA	Impacto Líquido OM
City 3	Ataque	Incentivos para clientes	R$ 2.750.000,00	99.220,00	R$ 7.639.940,00	R$ 628.003,07	R$ 192.500,00	-R$ 2.314.496,93
City 2	Ataque	Alterações de preço	R$ 2.250.000,00	71.280,00	R$ 5.132.160,00	R$ 459.841,54	R$ 135.000,00	-R$ 1.925.158,46
City 18	Ataque (Exceção Share)	Incentivos para clientes	R$ 1.750.000,00	63.140,00	R$ 4.167.240,00	R$ 321.710,93	R$ 122.500,00	-R$ 1.550.789,07
City 6	Ataque	Frete grátis	R$ 1.700.000,00	50.388,00	R$ 3.577.548,00	R$ 280.122,01	R$ 161.000,00	-R$ 1.580.877,99
City 17	Capacidade / Turnaround	Capacidade logística (entregadores)	R$ 2.665.969,51	68.675,38	R$ 5.562.705,78	R$ 410.527,69	R$ 373.235,73	-R$ 2.628.677,55
TOTAL	5 Praças Ativas	4 Alavancas	R$ 11.115.969,51	352.703,38	R$ 26.079.593,78	R$ 2.100.205,24	R$ 984.235,73	-R$ 10.000.000,00
---
Decisões Estratégicas e Guardrails
Investimento Bruto (`R$ 11,12M`) vs. Impacto Líquido na Operating Margin (`-R$ 10,00M`): A margem de contribuição incremental (`+R$ 2,10M`) compensa parte do desembolso bruto (`R$ 11,12M`) e dos custos operacionais/SLA (`R$ 0,98M`), fazendo com que o impacto líquido feche exatamente em `-R$ 10.000.000,00`.
Inclusão de `City 18` como exceção estratégica de ataque de share: Critério de materialidade atualizado para `"GMV >= R$ 50M OU cidade com folga logística, share baixo e retorno marginal positivo"`. `City 18` tem GMV real de `R$ 41,92M`, menor market share da base (`65,00%`), folga logística (`78,48%` de saturação) e retorno marginal positivo (`R$ 0,1838` MC/R$; `2,38x` GMV).
`City 17` recebe capacidade logística, e não cupom genérico: Com saturação base de `131,38%` (`1.524.881,30` pedidos equivalentes de capacidade base), o aporte de `R$ 2.665.969,51` cria `+180.000,00` pedidos equivalentes (`+11,80%` da capacidade base), reduzindo a saturação projetada de `135,88%` (sem intervenção) para `121,54%` (`-14,35 p.p.`).
`City 6` permanece abaixo de 98% com folga estreita (`0,46 p.p.`): Parte de `96,50%` e chega a `97,54%` com frete grátis focalizado (sem aumento de capacidade), incluindo `R$ 25.000,00` de custo extra de SLA (`R$ 161.000,00` no total). Exige monitoramento semanal e gatilho de pausa se exceder `98%`.
Sensibilidade e teste de estresse: O cenário base (`-R$ 10,00M`) é a alocação aprovada. No cenário adverso (`-20%` volume / `+15%` custo, `-R$ 12,24M` líquidos), acionam-se gatilhos de pausa nos incentivos de menor MC/R$, priorização de `City 2` e `City 3`, ajuste de capacidade em `City 17` se o SLA não melhorar e revisão mensal. No cenário otimista (`+20%` volume / `-10%` custo), o impacto líquido fica em `-R$ 8,37M`.
---
Estrutura do Repositório
```text
ifood-growth-competition-case/
├── data/
│   ├── raw/
│   │   └── Case_Competição_prático - Dados.csv      # Base original real (20 praças, 15 variáveis)
│   └── processed/
│       ├── base_validada.csv                        # Saneamento e totais validados (Notebook 01)
│       ├── base_segmentada.csv                      # Segmentação e exceção City 18 (Notebook 02)
│       ├── base_impacto.csv                         # Simulação econômica por alavanca (Notebook 03)
│       └── base_alocacao_otimizada.csv              # Alocação final em 5 cidades (Notebook 04)
├── notebooks/
│   ├── 01_EDA.ipynb                                 # Auditoria, totais e matriz de praças
│   ├── 02_Segmentacao.ipynb                         # Segmentação, guardrails e exceção estratégica
│   ├── 03_Impacto_Alavancas.ipynb                   # Modelagem financeira e validação cruzada
│   ├── 04_Otimizacao.ipynb                          # Validação contábil (-R$ 10M) e City 17 / City 6
│   ├── 05_Sensibilidade.ipynb                       # Cenários base, adverso e otimista
│   └── 06_Entregaveis.ipynb                         # Consolidação de KPIs e painel executivo
├── outputs/
│   ├── excel/
│   │   └── iFood_Business_Case_Analitico_Real.xlsx  # Workbook executivo multi-abas
│   ├── figures/                                     # Gráficos analíticos de alta resolução (PNG)
│   └── reports/                                     # Relatórios e CSVs consolidados
├── requirements.txt
└── README.md
```