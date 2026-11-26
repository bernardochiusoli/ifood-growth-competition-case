import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="iFood Growth & Portfolio Allocation (-R$ 10M OM)", layout="wide")

st.title("iFood Business Case — Alocação Otimizada (-R$ 10,00M na Operating Margin)")
st.caption("Fonte de verdade: base real Case_Competição_prático - Dados.csv (20 praças) | Soma algébrica exata = -R$ 10.000.000,00")

df_alloc = pd.read_csv("data/processed/base_alocacao_otimizada.csv")
df_sens = pd.read_csv("outputs/reports/sensibilidade_cenarios.csv")

# KPIs Principais
c1, c2, c3, c4, c5, c6, c7 = st.columns(7)
c1.metric("Cidades Ativas", "5 praças")
c2.metric("Investimento Bruto", "R$ 11,12M", "R$ 11.115.969,51")
c3.metric("Pedidos Incr. Líquidos", "+352,70k", "352.703,38 pedidos")
c4.metric("GMV Incremental", "+R$ 26,08M", "Múltiplo 2,35x")
c5.metric("MC Incremental", "+R$ 2,10M", "R$ 0,1889 / R$ 1 custo")
c6.metric("Custo Op. / SLA", "R$ 0,98M", "R$ 984.235,73")
c7.metric("Impacto Líquido OM", "-R$ 10,00M", "OM: 3,99% -> 3,21%")

st.info("Tese Executiva: O portfólio aloca R$ 11,12M de custo bruto para gerar R$ 26,08M de GMV incremental, 352,7 mil pedidos incrementais líquidos e R$ 2,10M de margem de contribuição incremental. Após custos operacionais e de SLA, o impacto líquido na Operating Margin é exatamente -R$ 10M. Nota: R$ 0,1889 de MC incremental por R$ 1 de custo bruto não representa ROI financeiro líquido positivo.")

# Tabela Aprovada
st.subheader("1. Tabela Final de Alocação Aprovada (Soma Algébrica = -R$ 10.000.000,00)")
st.dataframe(df_alloc[[
    "cidade", "classificacao", "alavanca", "custo_bruto_rs", "pedidos_brutos",
    "canibalizacao_pct", "pedidos_incrementais_liquidos", "gmv_incremental_rs",
    "mc_incremental_rs", "custo_operacional_sla_rs", "impacto_liquido_om_rs",
    "mc_por_real_custo", "multiplo_gmv", "saturacao_base_pct", "saturacao_pos_investimento_pct", "justificativa"
]], use_container_width=True)

# Painéis Especiais City 17 e City 6
col_a, col_b = st.columns(2)
with col_a:
    st.subheader("2. Painel Especial — City 17 (Capacidade Logística)")
    st.markdown("""
    - **Papel:** Praça estrutural (GMV R$ 162,62M, OM base -1,34%) — recebe **capacidade logística de entregadores** (sem cupom genérico).
    - **Capacidade base:** `1.524.881,30` pedidos equivalentes (`2.003.389,05 / 1,3138`).
    - **Capacidade adicional criada:** `+180.000,00` pedidos equivalentes (`+11,80%` sobre a capacidade base; equivalente a `296.218,83` h a `R$ 9,00/h`).
    - **Saturação:** Base `131,38%` | Sem intervenção `135,88%` | Pós-investimento `121,54%` (**-14,35 p.p.** vs. sem intervenção; **-9,84 p.p.** vs. base).
    """)
with col_b:
    st.subheader("3. Painel Especial — City 6 (Guardrail de Saturação)")
    st.markdown("""
    - **Papel:** Ataque focalizado com **frete grátis** (sem aumento de capacidade de entregadores).
    - **Saturação base -> pós-investimento:** `96,50%` -> `97,54%` (permanece abaixo do teto de `98%`).
    - **Folga remanescente até o guardrail de 98%:** **0,46 p.p.** (`98,00% - 97,54%`).
    - **Custo operacional/SLA incremental:** `R$ 161.000,00` (`8%` do custo bruto = `R$ 136.000,00` + `R$ 25.000,00` de SLA extra). Monitoramento semanal obrigatório.
    """)

# Drill-down por cidade
st.subheader("4. Drill-Down por Cidade")
cid_sel = st.selectbox("Selecione uma cidade ativa:", df_alloc["cidade"].tolist())
r_cid = df_alloc[df_alloc["cidade"] == cid_sel].iloc[0]
d1, d2, d3, d4 = st.columns(4)
d1.metric("Custo Bruto", f"R$ {r_cid['custo_bruto_rs']:,.2f}")
d2.metric("GMV Incremental", f"R$ {r_cid['gmv_incremental_rs']:,.2f}")
d3.metric("MC Incremental", f"R$ {r_cid['mc_incremental_rs']:,.2f}")
d4.metric("Impacto Líquido OM", f"R$ {r_cid['impacto_liquido_om_rs']:,.2f}")
st.write(f"**Justificativa:** {r_cid['justificativa']}")

# Simulador de Cenários
st.subheader("5. Simulador de Cenários e Sensibilidade")
st.dataframe(df_sens, use_container_width=True)
vol_mult = st.slider("Variação de Volume Incremental (%)", -30, 30, 0, 5)
custo_mult = st.slider("Variação de Custo Bruto e Op./SLA (%)", -20, 25, 0, 5)
gmv_sim = 26079593.78 * (1 + vol_mult/100.0)
mc_sim = 2100205.24 * (1 + vol_mult/100.0)
custo_sim = 11115969.51 * (1 + custo_mult/100.0)
op_sim = 984235.73 * (1 + custo_mult/100.0)
om_sim = mc_sim - custo_sim - op_sim
s1, s2, s3 = st.columns(3)
s1.metric("GMV Incremental Simulado", f"R$ {gmv_sim/1e6:.2f}M")
s2.metric("MC Incremental Simulada", f"R$ {mc_sim/1e6:.2f}M")
s3.metric("Impacto Líquido OM Simulado", f"R$ {om_sim/1e6:.2f}M", delta=f"R$ {(om_sim + 10000000)/1e6:.2f}M vs. -R$ 10M")
