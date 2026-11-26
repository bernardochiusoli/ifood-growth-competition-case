# iFome Business Case — Alocação de Investimentos (-R$ 10,00M na Operating Margin)

**Bernardo Akin Chiusoli Mendes**  
Análise, Estratégia de Negócios e Engenharia de Dados

Este projeto resolve um case de alocação de capital para crescimento do iFome: dado um portfólio real de 20 praças, como alocar investimentos em growth, market share, experiência do cliente e ROI, respeitando a exigência de gerar **exatamente -R$ 10.000.000,00 de impacto líquido na Operating Margin**.

A solução combina auditoria da base real, segmentação operacional, modelagem de impacto por alavanca, otimização restrita, análise de sensibilidade, guardrails operacionais e geração de entregáveis executivos.

## Tese executiva

> O portfólio aloca **R$ 11,12M de custo bruto** para gerar **R$ 26,08M de GMV incremental**, **352,7 mil pedidos incrementais líquidos** e **R$ 2,10M de margem de contribuição incremental**.  
>
> Após custos operacionais e de SLA, o impacto líquido na Operating Margin é exatamente **-R$ 10,00M**, conforme a restrição do case.  
>
> O retorno é de **R$ 0,19 de MC incremental por R$ 1 de custo bruto** e **2,35x de múltiplo de GMV**.

O investimento bruto não é igual ao impacto líquido na Operating Margin. A margem de contribuição incremental gerada compensa parte do desembolso bruto e dos custos operacionais, fazendo com que o resultado líquido feche exatamente em -R$ 10M.

## Resultados principais

| Indicador | Valor |
|---|---:|
| Cidades ativas | 5 |
| Investimento bruto total | R$ 11.115.969,51 |
| Pedidos incrementais líquidos | 352.703,38 |
| GMV incremental | R$ 26.079.593,78 |
| Margem de contribuição incremental | R$ 2.100.205,24 |
| Custo operacional/SLA | R$ 984.235,73 |
| Impacto líquido na Operating Margin | -R$ 10.000.000,00 |
| MC incremental por R$ 1 de custo bruto | R$ 0,1889 |
| Múltiplo de GMV | 2,35x |
| Operating Margin consolidada | 3,99% → 3,21% |

**Nota conceitual:** o valor de R$ 0,1889 representa a margem de contribuição incremental gerada por cada R$ 1,00 de custo bruto. Não é um ROI financeiro líquido positivo.

## Base real analisada

A análise utiliza exclusivamente a base real `Case_Competição_prático - Dados.csv`, com 20 praças e 15 variáveis.

| Indicador | Valor |
|---|---:|
| GMV base total | R$ 1.388.681.883,00 |
| Pedidos base totais | 17.844.024,78 |
| Margem de contribuição base | R$ 110.679.061,46 |
| Operating Margin base | R$ 55.355.277,41 |
| Operating Margin ponderada | 3,99% |
| Concentração de City 20 no GMV | 45,78% |

Praças com saturação acima de 100% não recebem estímulo genérico de demanda (cupons, frete grátis ou descontos) para não degradar o SLA. Quando há gargalo estrutural com unit economics e prioridade de turnaround — como na City 17 (131,38% de saturação base) — a atuação ocorre via capacidade logística de entregadores, enquanto praças de alta saturação sem alocação ativa (como City 20, a 141,21%) permanecem bloqueadas.

## Abordagem analítica

```text
Base real
   ↓
Validação e EDA
   ↓
Segmentação e arquétipos
   ↓
Modelagem de impacto por alavanca
   ↓
Otimização e alocação restrita
   ↓
Sensibilidade, guardrails e entregáveis
```

A alocação considera quatro alavancas:

- Incentivos para clientes
- Alterações de preço
- Frete grátis
- Capacidade logística por meio de incentivos a entregadores

A decisão prioriza praças com folga logística, margem saudável, espaço de market share e retorno marginal positivo. Cidades com saturação acima de 100% não recebem estímulo genérico de demanda (exceto City 17, que recebe capacidade logística dedicada para destravar oferta sem estímulo de demanda).

## Alocação final

| Cidade | Classificação | Alavanca | Custo bruto | Pedidos incrementais líquidos | GMV incremental | MC incremental | Custo op./SLA | Impacto líquido na OM |
|---|---|---|---:|---:|---:|---:|---:|---:|
| City 3 | Ataque | Incentivos para clientes | R$ 2.750.000,00 | 99.220,00 | R$ 7.639.940,00 | R$ 628.003,07 | R$ 192.500,00 | -R$ 2.314.496,93 |
| City 2 | Ataque | Alterações de preço | R$ 2.250.000,00 | 71.280,00 | R$ 5.132.160,00 | R$ 459.841,54 | R$ 135.000,00 | -R$ 1.925.158,46 |
| City 18 | Ataque — exceção de share | Incentivos para clientes | R$ 1.750.000,00 | 63.140,00 | R$ 4.167.240,00 | R$ 321.710,93 | R$ 122.500,00 | -R$ 1.550.789,07 |
| City 6 | Ataque | Frete grátis | R$ 1.700.000,00 | 50.388,00 | R$ 3.577.548,00 | R$ 280.122,01 | R$ 161.000,00 | -R$ 1.580.877,99 |
| City 17 | Capacidade / turnaround | Capacidade logística | R$ 2.665.969,51 | 68.675,38 | R$ 5.562.705,78 | R$ 410.527,69 | R$ 373.235,73 | -R$ 2.628.677,55 |
| **Total** | **5 praças ativas** | **4 alavancas** | **R$ 11.115.969,51** | **352.703,38** | **R$ 26.079.593,78** | **R$ 2.100.205,24** | **R$ 984.235,73** | **-R$ 10.000.000,00** |

## Decisões estratégicas

### City 18 — exceção estratégica de share

City 18 possui GMV de R$ 41,92M, abaixo do corte original de R$ 50M, mas foi incluída como exceção estratégica porque apresenta:

- Folga logística, com saturação de 78,48%.
- Menor market share da base, 65%.
- Retorno marginal positivo de R$ 0,1838 de MC incremental por R$ 1 de custo bruto.
- Múltiplo de GMV de 2,38x.

O critério de materialidade foi atualizado para:

> GMV ≥ R$ 50M **ou** cidade com folga logística, share baixo e retorno marginal positivo.

A tese é captura de share e escala em uma praça com capacidade disponível, com monitoramento rigoroso de margem por pedido e canibalização.

### City 17 — capacidade logística, não cupom

City 17 opera com saturação de 131,38% e Operating Margin negativa de -1,34%. Por isso, recebe capacidade logística por meio de incentivos a entregadores, e não cupom genérico.

| Métrica | Valor |
|---|---:|
| Capacidade base | 1.524.881,30 pedidos equivalentes |
| Capacidade adicional | +180.000 pedidos equivalentes |
| Aumento de capacidade | +11,80% |
| Saturação sem intervenção | 135,88% |
| Saturação pós-investimento | 121,54% |
| Redução da saturação | -14,35 p.p. |

A cidade continua acima de 100% de saturação após o investimento, mas a intervenção reduz a sobrecarga e permite atender pedidos adicionais sem estimular demanda além da capacidade criada.

### City 6 — ataque controlado

City 6 parte de 96,50% de saturação e alcança 97,54% após o frete grátis focalizado, permanecendo abaixo do guardrail de 98%.

- Folga remanescente: 0,46 p.p.
- Custo operacional/SLA: R$ 161.000,00
- Regra de governança: pausar ou reduzir o incentivo se a saturação semanal exceder 98%.

Não houve aumento de capacidade logística em City 6.

## Guardrails e sensibilidade

O cenário base é a alocação aprovada, com impacto líquido exato de -R$ 10M na Operating Margin.

| Cenário | Pressuposto | Impacto líquido na OM |
|---|---|---:|
| Base | Premissas aprovadas | -R$ 10,00M |
| Adverso | -20% de volume e +15% de custo | -R$ 12,24M |
| Otimista | +20% de volume e -10% de custo | -R$ 8,37M |

O cenário adverso é um teste de estresse, e não a alocação aprovada. Nesse cenário, os guardrails devem ser acionados:

- Pausar ou reduzir incentivos nas cidades com pior retorno marginal.
- Priorizar City 2 e City 3.
- Reduzir ou pausar capacidade em City 17 se o SLA não melhorar.
- Revisar a alocação mensalmente com dados reais de retenção, recorrência e unit economics.

## Premissas e limitações

A base real não contém elasticidades observadas, taxas de canibalização, curvas de SLA, retenção de 30 dias ou distribuição horária entre picos e vales. Portanto, estes parâmetros foram tratados como premissas explícitas de simulação.

| Premissa | Tratamento |
|---|---|
| Elasticidade-preço | Premissa conservadora, separada das demais alavancas |
| Elasticidade a incentivo ao cliente | Premissa positiva, específica por alavanca |
| Elasticidade a frete grátis | Premissa positiva, considerando cobertura já existente |
| Canibalização | Premissa específica por alavanca |
| Capacidade logística | Tratada como alavanca de capacidade, não de demanda |
| Fator de realização em City 17 | 92% da capacidade destravada |
| Retenção e LTV | Não embutidos no retorno de curto prazo |

As projeções devem ser validadas por teste controlado — geo-split ou switchback — antes da escala integral.

## Estrutura do repositório

```text
ifome-growth-case/
├── data/
│   ├── raw/
│   │   └── Case_Competição_prático - Dados.csv
│   └── processed/
│       ├── base_validada.csv
│       ├── base_segmentada.csv
│       ├── base_impacto.csv
│       └── base_alocacao_otimizada.csv
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_Segmentacao.ipynb
│   ├── 03_Impacto_Alavancas.ipynb
│   ├── 04_Otimizacao.ipynb
│   ├── 05_Sensibilidade.ipynb
│   └── 06_Entregaveis.ipynb
├── outputs/
│   ├── excel/
│   ├── figures/
│   └── reports/
├── requirements.txt
└── README.md
```

## Como executar

### Ambiente local

```bash
git clone [https://github.com/bernardochiusoli/ifome-growth-case.git](https://github.com/bernardochiusoli/iifome-growth-case.git)
cd ifome-growth-case
pip install -r requirements.txt
jupyter lab
```
## Dashboard executivo

O projeto inclui um dashboard interativo em Streamlit para visualizar a alocação final, os KPIs do portfólio e os principais guardrails operacionais.

### Execução local

```bash
streamlit run dashboard/app.py
```
Execute os notebooks na ordem:

```text
01_EDA.ipynb
02_Segmentacao.ipynb
03_Impacto_Alavancas.ipynb
04_Otimizacao.ipynb
05_Sensibilidade.ipynb
06_Entregaveis.ipynb
```

### Google Colab

Abra os notebooks no Google Colab e execute-os na mesma ordem. O projeto utiliza integração com o Google Drive para persistência dos artefatos no Colab, mas também pode ser executado localmente a partir da raiz do repositório.

## Governança e confidencialidade

Este repositório contém dados confidenciais de negócio. Não versionar credenciais, chaves de API, dados sensíveis adicionais ou outputs grandes no histórico do Git.

O pipeline foi estruturado para garantir rastreabilidade entre a base real, os notebooks, o Excel analítico e a apresentação executiva.
