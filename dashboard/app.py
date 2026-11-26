import os
import streamlit as st
import pandas as pd
import plotly.express as px

# ==============================================================================
# 1. CONFIGURAÇÃO DA PÁGINA E IDENTIDADE VISUAL (IFOOD)
# ==============================================================================
st.set_page_config(
    page_title="iFood Business Case — Alocação de R$ 10M na Operating Margin",
    page_icon="🔴",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F7F7F7;
        color: #1A1A1A;
    }
    .author-banner {
        background-color: #FFFFFF;
        border: 1px solid #E6E6E6;
        border-left: 5px solid #EA1D2C;
        border-radius: 8px;
        padding: 12px 18px;
        margin-bottom: 18px;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-between;
        align-items: center;
        gap: 8px;
    }
    .author-name {
        color: #1A1A1A;
        font-weight: 700;
        font-size: 0.98rem;
    }
    .secondary-gray {
        color: #666666;
        font-size: 0.88rem;
    }
    .ifood-accent {
        color: #EA1D2C;
        font-weight: 700;
        font-size: 0.88rem;
    }
    /* Evita truncamento excessivo nos cartões de métrica */
    div[data-testid="stMetric"] {
        background-color: #FFFFFF;
        border: 1px solid #E6E6E6;
        border-top: 4px solid #EA1D2C;
        padding: 12px 14px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }
    div[data-testid="stMetricLabel"] > div {
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: clip !important;
        color: #666666;
        font-weight: 600;
        font-size: 0.80rem;
        line-height: 1.25;
    }
    div[data-testid="stMetricValue"] > div {
        white-space: normal !important;
        overflow: visible !important;
        text-overflow: clip !important;
        color: #1A1A1A;
        font-weight: 700;
        font-size: 1.15rem;
        line-height: 1.25;
    }
    .footer-bar {
        text-align: center;
        color: #666666;
        font-size: 0.85rem;
        padding: 16px 0;
        margin-top: 28px;
        border-top: 1px solid #DFDFDF;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# 2. CAMINHOS RELATIVOS, CACHE E FORMATAÇÃO
# ==============================================================================
DATA_PATH = os.path.join("data", "processed", "base_alocacao_otimizada.csv")

CANDIDATOS_LOGO = [
    os.path.join("assets", "ifood_logo.png"),
    os.path.join("dashboard", "ifood_logo.png"),
    "ifood_logo.png",
]
LOGO_PATH = next((p for p in CANDIDATOS_LOGO if os.path.exists(p)), None)


@st.cache_data
def carregar_base(caminho: str) -> pd.DataFrame:
    """Carrega a base processada usando caminho relativo."""
    return pd.read_csv(caminho)


def fmt_brl(valor: float) -> str:
    """Formata valores em Reais no padrão brasileiro."""
    sinal = "-" if float(valor) < 0 else ""
    abs_val = abs(float(valor))
    txt = f"{abs_val:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"{sinal}R$ {txt}"


def fmt_num(valor: float, decimais: int = 2) -> str:
    """Formata valores numéricos no padrão brasileiro."""
    txt = f"{float(valor):,.{decimais}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return txt


# ==============================================================================
# 3. TRATAMENTO DE ERRO CASO O CSV NÃO EXISTIR
# ==============================================================================
if not os.path.exists(DATA_PATH):
    st.title("iFood Business Case — Alocação de R$ 10M na Operating Margin")
    st.markdown(
        '<div class="author-banner">'
        '<span class="author-name">Bernardo Akin Chiusoli Mendes</span>'
        '<span class="secondary-gray">Análise, Estratégia de Negócios e Engenharia de Dados</span>'
        "</div>",
        unsafe_allow_html=True,
    )
    st.error(
        f"**Arquivo não encontrado:** `{DATA_PATH}`.\n\n"
        "Para gerar o arquivo necessário, execute os notebooks na ordem:\n"
        "1. `notebooks/01_EDA.ipynb`\n"
        "2. `notebooks/02_Segmentacao.ipynb`\n"
        "3. `notebooks/03_Impacto_Alavancas.ipynb`\n"
        "4. `notebooks/04_Otimizacao.ipynb`\n"
        "5. `notebooks/05_Sensibilidade.ipynb`\n"
        "6. `notebooks/06_Entregaveis.ipynb`"
    )
    st.stop()

try:
    df = carregar_base(DATA_PATH)
except Exception as erro:
    st.error(f"Erro ao ler `{DATA_PATH}`: {erro}")
    st.stop()

# ==============================================================================
# 4. CABEÇALHO, LOGO, ASSINATURA E FILTROS
# ==============================================================================
col_logo, col_titulo = st.columns([1.2, 8.8], vertical_alignment="center")
with col_logo:
    if LOGO_PATH:
        st.image(LOGO_PATH, width=90)
    else:
        st.markdown('<div class="ifood-accent">iFood</div>', unsafe_allow_html=True)

with col_titulo:
    st.title("iFood Business Case — Alocação de R$ 10M na Operating Margin")

st.markdown(
    '<div class="author-banner">'
    '<div><span class="author-name">Bernardo Akin Chiusoli Mendes</span> '
    '<span class="secondary-gray">· Visão Executiva do Portfólio</span></div>'
    '<span class="ifood-accent">Fonte: data/processed/base_alocacao_otimizada.csv</span>'
    "</div>",
    unsafe_allow_html=True,
)

if LOGO_PATH:
    st.sidebar.image(LOGO_PATH, width=95)
st.sidebar.markdown("**Elaborado por:** Bernardo Akin Chiusoli Mendes")
st.sidebar.markdown("---")
st.sidebar.markdown("### Filtros")

df_view = df.copy()

cidades_opts = sorted(df_view["cidade"].dropna().astype(str).unique().tolist())
cidades_sel = st.sidebar.multiselect("Cidade", options=cidades_opts, default=cidades_opts)
if cidades_sel:
    df_view = df_view[df_view["cidade"].astype(str).isin(cidades_sel)]

alavancas_opts = sorted(df_view["alavanca"].dropna().astype(str).unique().tolist())
alavancas_sel = st.sidebar.multiselect("Alavanca", options=alavancas_opts, default=alavancas_opts)
if alavancas_sel:
    df_view = df_view[df_view["alavanca"].astype(str).isin(alavancas_sel)]

class_opts = sorted(df_view["classificacao"].dropna().astype(str).unique().tolist())
class_sel = st.sidebar.multiselect("Classificação", options=class_opts, default=class_opts)
if class_sel:
    df_view = df_view[df_view["classificacao"].astype(str).isin(class_sel)]

if df_view.empty:
    st.warning("Nenhum registro corresponde aos filtros selecionados.")
    st.stop()

# ==============================================================================
# 5. KPIS EXECUTIVOS (SOMENTE DADOS DA BASE FILTRADA)
# ==============================================================================
cidades_ativas = int(df_view["cidade"].nunique())
custo_bruto_tot = float(df_view["custo_bruto_rs"].sum())
pedidos_liq_tot = float(df_view["pedidos_incrementais_liquidos"].sum())
gmv_inc_tot = float(df_view["gmv_incremental_rs"].sum())
mc_inc_tot = float(df_view["mc_incremental_rs"].sum())
om_liq_tot = float(df_view["impacto_liquido_om_rs"].sum())

mc_por_real = (mc_inc_tot / custo_bruto_tot) if custo_bruto_tot != 0 else 0.0
multiplo_gmv = (gmv_inc_tot / custo_bruto_tot) if custo_bruto_tot != 0 else 0.0

k1, k2, k3, k4 = st.columns(4)
k1.metric("Cidades ativas", f"{cidades_ativas}")
k2.metric("Investimento bruto total", fmt_brl(custo_bruto_tot))
k3.metric("Pedidos incrementais líquidos", fmt_num(pedidos_liq_tot, 2))
k4.metric("GMV incremental", fmt_brl(gmv_inc_tot))

k5, k6, k7, k8 = st.columns(4)
k5.metric("MC incremental", fmt_brl(mc_inc_tot))
k6.metric("Impacto líquido na OM", fmt_brl(om_liq_tot))
k7.metric("MC / R$ 1 custo bruto", f"R$ {fmt_num(mc_por_real, 4)}")
k8.metric("Múltiplo de GMV", f"{fmt_num(multiplo_gmv, 2)}x")

st.markdown("---")

# ==============================================================================
# 6. GRÁFICOS DE BARRAS POR CIDADE
# ==============================================================================
g1, g2 = st.columns(2)

with g1:
    df_om = df_view.sort_values("impacto_liquido_om_rs", ascending=True)
    fig_om = px.bar(
        df_om,
        x="cidade",
        y="impacto_liquido_om_rs",
        text=df_om["impacto_liquido_om_rs"].apply(fmt_brl),
        title="Impacto líquido na Operating Margin por cidade",
        labels={"cidade": "Cidade", "impacto_liquido_om_rs": "Impacto líquido na OM (R$)"},
        color="cidade",
        color_discrete_sequence=["#991B1B", "#EA1D2C", "#F87171", "#334155", "#64748B"],
    )
    fig_om.update_traces(textposition="outside", cliponaxis=False)
    fig_om.update_layout(
        showlegend=False,
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        font=dict(color="#1A1A1A"),
        xaxis_title="",
        yaxis_title="Impacto líquido na OM (R$)",
    )
    st.plotly_chart(fig_om, use_container_width=True)

with g2:
    df_gmv = df_view.sort_values("gmv_incremental_rs", ascending=False)
    fig_gmv = px.bar(
        df_gmv,
        x="cidade",
        y="gmv_incremental_rs",
        text=df_gmv["gmv_incremental_rs"].apply(fmt_brl),
        title="GMV incremental por cidade",
        labels={"cidade": "Cidade", "gmv_incremental_rs": "GMV incremental (R$)"},
        color="cidade",
        color_discrete_sequence=["#EA1D2C", "#1E293B", "#475569", "#94A3B8", "#CBD5E1"],
    )
    fig_gmv.update_traces(textposition="outside", cliponaxis=False)
    fig_gmv.update_layout(
        showlegend=False,
        plot_bgcolor="#FFFFFF",
        paper_bgcolor="#FFFFFF",
        font=dict(color="#1A1A1A"),
        xaxis_title="",
        yaxis_title="GMV incremental (R$)",
    )
    st.plotly_chart(fig_gmv, use_container_width=True)

st.markdown("---")

# ==============================================================================
# 7. DESTAQUES: CITY 17 E CITY 6
# ==============================================================================
d17, d6 = st.columns(2)

with d17:
    with st.container(border=True):
        st.subheader("City 17")
        sub17 = df[df["cidade"].astype(str) == "City 17"]
        if not sub17.empty:
            r17 = sub17.iloc[0]
            c1, c2 = st.columns(2)
            c1.metric("Capacidade base", fmt_num(r17["capacidade_base_pedidos_equiv"], 2))
            c2.metric("Capacidade adicional", fmt_num(r17["capacidade_adicional_pedidos_equiv"], 2))

            c3, c4, c5 = st.columns(3)
            c3.metric("Sat. base", f"{fmt_num(r17['saturacao_base_pct'], 2)}%")
            c4.metric("Sat. sem interv.", f"{fmt_num(r17['saturacao_sem_intervencao_pct'], 2)}%")
            c5.metric("Sat. pós-inv.", f"{fmt_num(r17['saturacao_pos_investimento_pct'], 2)}%")
        else:
            st.info("City 17 não encontrada na base.")

with d6:
    with st.container(border=True):
        st.subheader("City 6")
        sub6 = df[df["cidade"].astype(str) == "City 6"]
        if not sub6.empty:
            r6 = sub6.iloc[0]
            s1, s2, s3 = st.columns(3)
            s1.metric("Sat. base", f"{fmt_num(r6['saturacao_base_pct'], 2)}%")
            s2.metric("Sat. pós-inv.", f"{fmt_num(r6['saturacao_pos_investimento_pct'], 2)}%")
            s3.metric("Folga até 98%", f"{fmt_num(r6['folga_guardrail_98_pp'], 2)} p.p.")
        else:
            st.info("City 6 não encontrada na base.")

st.markdown("---")

# ==============================================================================
# 8. TABELA DETALHADA
# ==============================================================================
st.subheader("Tabela Detalhada")

df_tab = pd.DataFrame({
    "Cidade": df_view["cidade"],
    "Classificação": df_view["classificacao"],
    "Alavanca": df_view["alavanca"],
    "Custo bruto": df_view["custo_bruto_rs"].apply(fmt_brl),
    "Pedidos incrementais líquidos": df_view["pedidos_incrementais_liquidos"].apply(lambda v: fmt_num(v, 2)),
    "GMV incremental": df_view["gmv_incremental_rs"].apply(fmt_brl),
    "MC incremental": df_view["mc_incremental_rs"].apply(fmt_brl),
    "Custo operacional/SLA": df_view["custo_operacional_sla_rs"].apply(fmt_brl),
    "Impacto líquido na Operating Margin": df_view["impacto_liquido_om_rs"].apply(fmt_brl),
})

st.dataframe(df_tab, use_container_width=True, hide_index=True)

# ==============================================================================
# 9. RODAPÉ
# ==============================================================================
st.markdown(
    '<div class="footer-bar">Dados confidenciais | Pipeline Python | Análise reprodutível</div>',
    unsafe_allow_html=True,
)