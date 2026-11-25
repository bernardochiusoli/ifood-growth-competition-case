import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# ==============================================================================
# CONFIGURAÇÃO DA PÁGINA & IDENTIDADE VISUAL (INSPIRADA NO iFOOD)
# ==============================================================================
st.set_page_config(
    page_title="iFood Growth Case | Alocação -R$ 10M Operating Margin",
    page_icon="🛵",
    layout="wide",
    initial_sidebar_state="expanded",
)

IFOOD_RED = "#EA1D2C"
IFOOD_DARK = "#2E2E2E"
IFOOD_GREEN = "#1E6B38"
IFOOD_AMBER = "#D97706"
IFOOD_LIGHT_BG = "#F7F7F7"

st.markdown(
    f"""
    <style>
    .main-header {{
        background-color: {IFOOD_RED};
        padding: 1.1rem 1.5rem;
        border-radius: 10px;
        color: white;
        margin-bottom: 1.2rem;
    }}
    .main-header h1 {{
        margin: 0;
        font-size: 1.55rem;
        font-weight: 700;
    }}
    .main-header p {{
        margin: 0.25rem 0 0 0;
        font-size: 0.92rem;
        opacity: 0.95;
    }}
    .guardrail-ok {{
        background-color: #E8F5E9;
        border-left: 5px solid {IFOOD_GREEN};
        padding: 0.65rem 0.9rem;
        border-radius: 6px;
        color: #1B4332;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }}
    .guardrail-warn {{
        background-color: #FFF3E0;
        border-left: 5px solid {IFOOD_AMBER};
        padding: 0.65rem 0.9rem;
        border-radius: 6px;
        color: #7C2D12;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }}
    .guardrail-alert {{
        background-color: #FFEBEE;
        border-left: 5px solid {IFOOD_RED};
        padding: 0.65rem 0.9rem;
        border-radius: 6px;
        color: #7F1D1D;
        font-size: 0.9rem;
        margin-bottom: 0.5rem;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# DADOS AUDITADOS DO MODELO CONSOLIDADO (20 CIDADES + 5 PRIORIZADAS)
# ==============================================================================
@st.cache_data
def load_baseline_data():
    # Dados exatos das 5 cidades priorizadas (Slides 2 a 7)
    active_cities = pd.DataFrame([
        {
            "cidade": "City 3",
            "grupo": "Frente de Ataque",
            "alavanca": "Frete Grátis Focalizado + Incentivo",
            "gmv_base": 100_000_000.0,
            "share_base_pct": 76.00,
            "om_base_pct": 6.06,
            "frete_gratis_base_pct": 27.0,
            "price_index": 101.27,
            "sat_base_pct": 79.81,
            "sat_sem_interv_pct": 96.75,
            "sat_pos_base_pct": 96.75,
            "custo_bruto_base": 2_800_000.0,
            "custo_op_base": 0.0,
            "ped_brutos_base": 400_000,
            "canib_pct": 30.0,
            "ped_inc_liq_base": 280_000,
            "gmv_inc_base": 21_560_000.0,
            "mc_inc_base": 1_772_232.0,
            "cap_adicional_eq": 0,
            "criterio": "Folga logística (<97%), OM positiva (6,06%) e espaço de frete grátis (27%)."
        },
        {
            "cidade": "City 2",
            "grupo": "Frente de Ataque",
            "alavanca": "Ajuste Seletivo de Preço + Incentivo",
            "gmv_base": 88_000_000.0,
            "share_base_pct": 67.00,
            "om_base_pct": 8.41,
            "frete_gratis_base_pct": 55.0,
            "price_index": 116.84,
            "sat_base_pct": 83.90,
            "sat_sem_interv_pct": 96.29,
            "sat_pos_base_pct": 96.29,
            "custo_bruto_base": 1_200_000.0,
            "custo_op_base": 0.0,
            "ped_brutos_base": 240_000,
            "canib_pct": 25.0,
            "ped_inc_liq_base": 180_000,
            "gmv_inc_base": 12_960_000.0,
            "mc_inc_base": 1_161_216.0,
            "cap_adicional_eq": 0,
            "criterio": "Maior OM entre grandes praças (8,41%), Price Index alto (116,84%) e share de 67%."
        },
        {
            "cidade": "City 6",
            "grupo": "Frente de Ataque",
            "alavanca": "Incentivo a Clientes + Reforço Pontual Frota",
            "gmv_base": 64_290_000.0,
            "share_base_pct": 68.00,
            "om_base_pct": 7.09,
            "frete_gratis_base_pct": 27.0,
            "price_index": 102.50,
            "sat_base_pct": 96.50,
            "sat_sem_interv_pct": 107.29,
            "sat_pos_base_pct": 94.12,
            "custo_bruto_base": 1_600_000.0,
            "custo_op_base": 0.0,
            "ped_brutos_base": 160_000,
            "canib_pct": 37.5,
            "ped_inc_liq_base": 100_000,
            "gmv_inc_base": 7_100_000.0,
            "mc_inc_base": 555_930.0,
            "cap_adicional_eq": 129_700,
            "criterio": "OM saudável (7,09%); reforço de frota (+129,7k eq.) evita saturação de 107,29%."
        },
        {
            "cidade": "City 17",
            "grupo": "Turnaround Capacidade",
            "alavanca": "Reforço Frota + Racionalização Frete Grátis",
            "gmv_base": 162_620_000.0,
            "share_base_pct": 67.00,
            "om_base_pct": -1.34,
            "frete_gratis_base_pct": 54.0,
            "price_index": 104.10,
            "sat_base_pct": 131.38,
            "sat_sem_interv_pct": 138.92,
            "sat_pos_base_pct": 114.50,
            "custo_bruto_base": 3_152_395.0,
            "custo_op_base": 200_000.0,
            "ped_brutos_base": 115_000,
            "canib_pct": 0.0,
            "ped_inc_liq_base": 115_000,
            "gmv_inc_base": 9_300_000.0,
            "mc_inc_base": 687_447.0,
            "cap_adicional_eq": 325_240,
            "criterio": "2ª maior praça (R$ 162,62M GMV) com OM base -1,34% e saturação de 131,38%."
        },
        {
            "cidade": "City 20",
            "grupo": "Turnaround Capacidade",
            "alavanca": "Proteção Estrita de Capacidade (0% Cupom)",
            "gmv_base": 635_780_000.0,
            "share_base_pct": 74.00,
            "om_base_pct": 3.20,
            "frete_gratis_base_pct": 42.0,
            "price_index": 105.00,
            "sat_base_pct": 141.21,
            "sat_sem_interv_pct": 143.87,
            "sat_pos_base_pct": 127.00,
            "custo_bruto_base": 5_880_000.0,
            "custo_op_base": 300_000.0,
            "ped_brutos_base": 140_000,
            "canib_pct": 0.0,
            "ped_inc_liq_base": 140_000,
            "gmv_inc_base": 11_915_000.0,
            "mc_inc_base": 955_570.0,
            "cap_adicional_eq": 700_060,
            "criterio": "Protege 45,78% do GMV total (R$ 635,78M) e 74% de share; alavanca 100% oferta."
        },
    ])

    # Taxas marginais por R$ 1,00 de custo bruto
    active_cities["mc_por_real"] = active_cities["mc_inc_base"] / active_cities["custo_bruto_base"]
    active_cities["mult_gmv"] = active_cities["gmv_inc_base"] / active_cities["custo_bruto_base"]
    active_cities["ped_liq_por_real"] = active_cities["ped_inc_liq_base"] / active_cities["custo_bruto_base"]
    active_cities["custo_op_por_real"] = active_cities["custo_op_base"] / active_cities["custo_bruto_base"]
    active_cities["impacto_om_base"] = (
        active_cities["mc_inc_base"] - active_cities["custo_bruto_base"] - active_cities["custo_op_base"]
    )
    active_cities["delta_sat_por_real"] = (
        active_cities["sat_pos_base_pct"] - active_cities["sat_base_pct"]
    ) / active_cities["custo_bruto_base"]

    # Base das 20 cidades para Pareto e Matriz Estratégica (Slide 3)
    portfolio_20 = pd.DataFrame([
        ("City 20", 635.78, 141.21, 74.0, 3.20, "Turnaround (2)"),
        ("City 17", 162.62, 131.38, 67.0, -1.34, "Turnaround (2)"),
        ("City 3", 100.00, 79.81, 76.0, 6.06, "Ataque (3)"),
        ("City 2", 88.00, 83.90, 67.0, 8.41, "Ataque (3)"),
        ("City 6", 64.29, 96.50, 68.0, 7.09, "Ataque (3)"),
        ("City 9", 61.50, 89.00, 80.0, 5.10, "Fora de Escopo (7)"),
        ("City 4", 52.40, 129.50, 73.0, 2.40, "Bloq. Sat >100% / OM <0 (8)"),
        ("City 18", 41.80, 82.50, 86.0, 4.80, "Fora de Escopo (7)"),
        ("City 15", 39.20, 70.00, 86.0, 6.20, "Fora de Escopo (7)"),
        ("City 1", 23.10, 99.00, 65.0, 3.90, "Fora de Escopo (7)"),
        ("City 16", 22.80, 102.00, 78.0, 1.80, "Bloq. Sat >100% / OM <0 (8)"),
        ("City 13", 22.40, 120.80, 70.0, 1.10, "Bloq. Sat >100% / OM <0 (8)"),
        ("City 7", 21.90, 78.50, 65.0, 5.50, "Fora de Escopo (7)"),
        ("City 5", 19.60, 148.00, 73.0, 0.90, "Bloq. Sat >100% / OM <0 (8)"),
        ("City 11", 16.50, 95.00, 66.0, 4.10, "Fora de Escopo (7)"),
        ("City 12", 12.80, 88.00, 64.0, -2.10, "Bloq. Sat >100% / OM <0 (8)"),
        ("City 14", 4.90, 81.00, 62.0, -3.40, "Bloq. Sat >100% / OM <0 (8)"),
        ("City 10", 4.10, 76.00, 63.0, 3.50, "Fora de Escopo (7)"),
        ("City 19", 3.20, 84.00, 61.0, -1.80, "Bloq. Sat >100% / OM <0 (8)"),
        ("City 8", 1.87, 79.00, 60.0, -4.20, "Bloq. Sat >100% / OM <0 (8)"),
    ], columns=["cidade", "gmv_base_m", "sat_base_pct", "share_base_pct", "om_base_pct", "status_grupo"])

    portfolio_20 = portfolio_20.sort_values("gmv_base_m", ascending=False).reset_index(drop=True)
    portfolio_20["gmv_acum_pct"] = portfolio_20["gmv_base_m"].cumsum() / portfolio_20["gmv_base_m"].sum() * 100

    # Tabela exata de sensibilidade de realocação R$ 500k de City 6 (Slide 7)
    realoc_df = pd.DataFrame([
        {
            "Cenario": "City 6 (-R$ 0,50M) -> City 20 (+R$ 0,50M)",
            "Delta_Ped_Inc": -27158,
            "Delta_GMV_Inc_M": -1.76,
            "Delta_Impacto_OM_M": -0.14,
            "Sat_Destino_Pos_Pct": 126.83,
            "Diagnostico": "Rejeitado: reduz pedidos, GMV e margem; praça segue sobrecarregada (>100%)."
        },
        {
            "Cenario": "City 6 (-R$ 0,50M) -> City 17 (+R$ 0,50M)",
            "Delta_Ped_Inc": -20822,
            "Delta_GMV_Inc_M": -1.29,
            "Delta_Impacto_OM_M": -0.11,
            "Sat_Destino_Pos_Pct": 113.69,
            "Diagnostico": "Rejeitado: reduz pedidos, GMV e margem; OM base negativa (-1,34%)."
        },
        {
            "Cenario": "City 6 (-R$ 0,50M) -> City 3 (+R$ 0,50M)",
            "Delta_Ped_Inc": 10938,
            "Delta_GMV_Inc_M": 1.08,
            "Delta_Impacto_OM_M": 0.10,
            "Sat_Destino_Pos_Pct": 99.87,
            "Diagnostico": "Bloqueado pelo Guardrail: ultrapassa o teto de 98,0% de saturação."
        },
        {
            "Cenario": "City 6 (-R$ 0,50M) -> City 2 (+R$ 0,50M)",
            "Delta_Ped_Inc": 35938,
            "Delta_GMV_Inc_M": 2.63,
            "Delta_Impacto_OM_M": 0.27,
            "Sat_Destino_Pos_Pct": 101.47,
            "Diagnostico": "Bloqueado pelo Guardrail: ultrapassa o teto de 98,0% de saturação."
        },
    ])

    return active_cities, portfolio_20, realoc_df


def fmt_brl(val: float, decimals: int = 2) -> str:
    s = f"{val:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    return f"R$ {s}"


def fmt_int(val: float) -> str:
    return f"{int(round(val)):,}".replace(",", ".")


df_active, df_20, df_realoc = load_baseline_data()

# ==============================================================================
# CABEÇALHO PRINCIPAL
# ==============================================================================
st.markdown(
    """
    <div class="main-header">
        <h1>🛵 Business Case de Growth & Estratégia de Portfólio — Simulador Executivo</h1>
        <p>Alocação de -R$ 10,00M na Operating Margin | Priorização de 5 Praças, Sensibilidade Marginal e Governança por Guardrails</p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ==============================================================================
# SIDEBAR — CONTROLES DE SIMULAÇÃO DE ORÇAMENTO E GUARDRAILS
# ==============================================================================
with st.sidebar:
    st.header("⚙️ Simulador de Alocação")
    st.caption("Ajuste o Custo Bruto (R$ M) por praça ou restaure o cenário auditado.")

    if st.button("🔄 Restaurar Cenário Auditado (-R$ 10,00M)", use_container_width=True):
        for _, row in df_active.iterrows():
            st.session_state[f"slider_{row['cidade']}"] = round(row["custo_bruto_base"] / 1e6, 3)

    budgets_m = {}
    for _, row in df_active.iterrows():
        c = row["cidade"]
        default_m = round(row["custo_bruto_base"] / 1e6, 3)
        budgets_m[c] = st.slider(
            f"{c} ({row['grupo']})",
            min_value=0.0,
            max_value=8.0,
            value=st.session_state.get(f"slider_{c}", default_m),
            step=0.05,
            key=f"slider_{c}",
            format="R$ %.2f M",
        )

    st.divider()
    st.subheader("🛡️ Parâmetros de Guardrail")
    teto_sat_ataque = st.number_input("Teto Saturação Ataque (%)", value=98.0, step=0.5)
    teto_om_neg = st.number_input("Limite Impacto OM (R$ M)", value=-10.00, step=0.25)

# ==============================================================================
# CÁLCULO DINÂMICO DO CENÁRIO SIMULADO
# ==============================================================================
sim_df = df_active.copy()
sim_df["custo_bruto_sim"] = sim_df["cidade"].map(lambda c: budgets_m[c] * 1e6)
sim_df["custo_op_sim"] = sim_df["custo_bruto_sim"] * sim_df["custo_op_por_real"]
sim_df["mc_inc_sim"] = sim_df["custo_bruto_sim"] * sim_df["mc_por_real"]
sim_df["gmv_inc_sim"] = sim_df["custo_bruto_sim"] * sim_df["mult_gmv"]
sim_df["ped_inc_liq_sim"] = sim_df["custo_bruto_sim"] * sim_df["ped_liq_por_real"]
sim_df["impacto_om_sim"] = sim_df["mc_inc_sim"] - sim_df["custo_bruto_sim"] - sim_df["custo_op_sim"]

# Saturação simulada (mantém exatidão no ponto base e escala linearmente na vizinhança)
sim_df["sat_pos_sim_pct"] = (
    sim_df["sat_base_pct"] + sim_df["delta_sat_por_real"] * sim_df["custo_bruto_sim"]
)

tot_custo_bruto = sim_df["custo_bruto_sim"].sum()
tot_custo_op = sim_df["custo_op_sim"].sum()
tot_mc_inc = sim_df["mc_inc_sim"].sum()
tot_gmv_inc = sim_df["gmv_inc_sim"].sum()
tot_ped_liq = sim_df["ped_inc_liq_sim"].sum()
tot_impacto_om = sim_df["impacto_om_sim"].sum()
mult_gmv_port = tot_gmv_inc / tot_custo_bruto if tot_custo_bruto > 0 else 0.0
mc_por_real_port = tot_mc_inc / tot_custo_bruto if tot_custo_bruto > 0 else 0.0

# ==============================================================================
# KPI CARDS SUPERIORES (SLIDE 1 & 2)
# ==============================================================================
k1, k2, k3, k4, k5, k6 = st.columns(6)
k1.metric("GMV Incremental", f"R$ {tot_gmv_inc/1e6:,.2f}M", f"+{tot_gmv_inc/1_388_760_000*100:.2f}% base")
k2.metric("Pedidos Inc. Líquidos", fmt_int(tot_ped_liq), "Canib. média 22,75%")
k3.metric("Múltiplo de GMV", f"{mult_gmv_port:.2f}x", "GMV / Custo Bruto")
k4.metric("MC Inc. / R$ 1", f"R$ {mc_por_real_port:.2f}", f"MC Total R$ {tot_mc_inc/1e6:.2f}M")
k5.metric("Custo Bruto Total", f"R$ {tot_custo_bruto/1e6:,.2f}M", f"+ R$ {tot_custo_op/1e3:.0f}k Op/SLA")
k6.metric(
    "Impacto Líq. Op. Margin",
    f"R$ {tot_impacto_om/1e6:,.2f}M",
    f"Desvio meta: R$ {(tot_impacto_om - teto_om_neg*1e6)/1e3:+,.0f}k",
    delta_color="normal" if abs(tot_impacto_om - teto_om_neg * 1e6) < 5000 else "inverse",
)

# Painel rápido de status dos Guardrails
st.markdown("### 🚦 Monitoramento de Guardrails em Tempo Real")
g_col1, g_col2, g_col3 = st.columns(3)

ataque_viol = sim_df[(sim_df["grupo"] == "Frente de Ataque") & (sim_df["sat_pos_sim_pct"] > teto_sat_ataque)]
with g_col1:
    if len(ataque_viol) == 0:
        st.markdown(
            f'<div class="guardrail-ok"><b>Guardrail 1 — Saturação Ataque (≤ {teto_sat_ataque:.1f}%):</b> OK. Todas as praças de ataque operam dentro da folga logística.</div>',
            unsafe_allow_html=True,
        )
    else:
        c_names = ", ".join(
            [f"{r['cidade']} ({r['sat_pos_sim_pct']:.2f}%)" for _, r in ataque_viol.iterrows()]
        )
        st.markdown(
            f'<div class="guardrail-alert"><b>Guardrail 1 VIOLADO:</b> {c_names} ultrapassou o teto de {teto_sat_ataque:.1f}%.</div>',
            unsafe_allow_html=True,
        )

with g_col2:
    diff_om = tot_impacto_om - (teto_om_neg * 1e6)
    if abs(diff_om) <= 10_000:
        st.markdown(
            f'<div class="guardrail-ok"><b>Restrição Orçamentária (-R$ 10,00M):</b> Fechamento exato em {fmt_brl(tot_impacto_om)}.</div>',
            unsafe_allow_html=True,
        )
    elif tot_impacto_om < (teto_om_neg * 1e6):
        st.markdown(
            f'<div class="guardrail-alert"><b>Orçamento Excedido:</b> Impacto líquido em {fmt_brl(tot_impacto_om)} (estouro de {fmt_brl(abs(diff_om))}).</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="guardrail-warn"><b>Subalocação Orçamentária:</b> Impacto atual em {fmt_brl(tot_impacto_om)} (folga de {fmt_brl(diff_om)}).</div>',
            unsafe_allow_html=True,
        )

with g_col3:
    st.markdown(
        '<div class="guardrail-ok"><b>Guardrails 2, 3 & 4:</b> Turnaround sem cupom genérico; pausa automática se SLA subir >8,0% vs. baseline 4 sem.</div>',
        unsafe_allow_html=True,
    )

# ==============================================================================
# ABAS NAVEGÁVEIS (ESPELHANDO OS SLIDES 2 A 9)
# ==============================================================================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 1. Consolidado & 5 Praças",
    "🗺️ 2. Diagnóstico 20 Cidades (Pareto & Matriz)",
    "🚛 3. Turnaround City 20 & City 17",
    "⚖️ 4. Sensibilidade & Teste R$ 500k",
    "🧪 5. Metodologia, Experimentos & Guardrails",
])

# ------------------------------------------------------------------------------
# TAB 1: CONSOLIDADO E FRENTE DE ATAQUE
# ------------------------------------------------------------------------------
with tab1:
    c_left, c_right = st.columns([1.15, 1])

    with c_left:
        st.subheader("Alocação Financeira e Retorno por Praça (Simulado)")
        chart_df = sim_df.copy()
        chart_df["Custo Bruto (R$ M)"] = chart_df["custo_bruto_sim"] / 1e6
        chart_df["GMV Incremental (R$ M)"] = chart_df["gmv_inc_sim"] / 1e6
        chart_df["MC Incremental (R$ M)"] = chart_df["mc_inc_sim"] / 1e6

        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(
            name="Custo Bruto (R$ M)",
            x=chart_df["cidade"],
            y=chart_df["Custo Bruto (R$ M)"],
            marker_color=IFOOD_DARK,
            text=chart_df["Custo Bruto (R$ M)"].map(lambda v: f"R${v:.2f}M"),
            textposition="outside",
        ))
        fig_bar.add_trace(go.Bar(
            name="GMV Incremental (R$ M)",
            x=chart_df["cidade"],
            y=chart_df["GMV Incremental (R$ M)"],
            marker_color=IFOOD_RED,
            text=chart_df["GMV Incremental (R$ M)"].map(lambda v: f"R${v:.2f}M"),
            textposition="outside",
        ))
        fig_bar.add_trace(go.Bar(
            name="MC Incremental (R$ M)",
            x=chart_df["cidade"],
            y=chart_df["MC Incremental (R$ M)"],
            marker_color=IFOOD_GREEN,
            text=chart_df["MC Incremental (R$ M)"].map(lambda v: f"R${v:.2f}M"),
            textposition="outside",
        ))
        fig_bar.update_layout(
            barmode="group",
            height=390,
            margin=dict(t=30, b=20, l=20, r=20),
            yaxis_title="R$ Milhões",
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with c_right:
        st.subheader("Saturação Logística: Base vs. Pós-Investimento")
        fig_sat = go.Figure()
        fig_sat.add_trace(go.Bar(
            name="Saturação Base (%)",
            x=sim_df["cidade"],
            y=sim_df["sat_base_pct"],
            marker_color="#9CA3AF",
            text=sim_df["sat_base_pct"].map(lambda v: f"{v:.1f}%"),
            textposition="outside",
        ))
        fig_sat.add_trace(go.Bar(
            name="Saturação Pós-Investimento (%)",
            x=sim_df["cidade"],
            y=sim_df["sat_pos_sim_pct"],
            marker_color=[
                IFOOD_RED if (g == "Frente de Ataque" and s > teto_sat_ataque) else IFOOD_GREEN
                for g, s in zip(sim_df["grupo"], sim_df["sat_pos_sim_pct"])
            ],
            text=sim_df["sat_pos_sim_pct"].map(lambda v: f"{v:.1f}%"),
            textposition="outside",
        ))
        fig_sat.add_hline(
            y=teto_sat_ataque,
            line_dash="dash",
            line_color=IFOOD_AMBER,
            annotation_text=f"Teto Ataque ({teto_sat_ataque:.0f}%)",
        )
        fig_sat.add_hline(
            y=100.0,
            line_dash="dot",
            line_color=IFOOD_RED,
            annotation_text="Capacidade Nominal (100%)",
        )
        fig_sat.update_layout(
            barmode="group",
            height=390,
            margin=dict(t=30, b=20, l=20, r=20),
            yaxis_title="Saturação (%)",
            yaxis_range=[0, 165],
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        )
        st.plotly_chart(fig_sat, use_container_width=True)

    st.subheader("Tabela Financeira Consolidada Auditada / Simulada")
    display_df = pd.DataFrame({
        "Cidade": sim_df["cidade"],
        "Grupo": sim_df["grupo"],
        "Alavanca": sim_df["alavanca"],
        "Custo Bruto": sim_df["custo_bruto_sim"].map(fmt_brl),
        "Custo Op./SLA": sim_df["custo_op_sim"].map(fmt_brl),
        "Ped. Inc. Líq.": sim_df["ped_inc_liq_sim"].map(fmt_int),
        "GMV Incremental": sim_df["gmv_inc_sim"].map(fmt_brl),
        "MC Incremental": sim_df["mc_inc_sim"].map(fmt_brl),
        "Impacto Líq. OM": sim_df["impacto_om_sim"].map(fmt_brl),
        "MC / R$ 1": sim_df["mc_por_real"].map(lambda v: f"R$ {v:.2f}"),
        "Mult. GMV": sim_df["mult_gmv"].map(lambda v: f"{v:.2f}x"),
        "Sat. Base -> Pós": [
            f"{b:.1f}% -> {p:.1f}%" for b, p in zip(sim_df["sat_base_pct"], sim_df["sat_pos_sim_pct"])
        ],
    })
    st.dataframe(display_df, use_container_width=True, hide_index=True)

# ------------------------------------------------------------------------------
# TAB 2: DIAGNÓSTICO DAS 20 CIDADES (SLIDE 3)
# ------------------------------------------------------------------------------
with tab2:
    st.markdown(
        "**Síntese Executiva:** As 5 cidades priorizadas concentram **75,7%** do GMV total "
        "(**R$ 1,05 Bi** de **R$ 1,39 Bi**). As outras 15 cidades são bloqueadas por saturação >100% / OM <0 (8 praças) "
        "ou ficam fora de escopo por baixa materialidade (~0,8% do GMV por praça em 7 cidades)."
    )
    p_col1, p_col2 = st.columns(2)

    with p_col1:
        st.subheader("Curva de Pareto do GMV Base (20 Cidades)")
        colors_pareto = [
            IFOOD_RED if c in ["City 20", "City 17", "City 3", "City 2", "City 6"] else "#9CA3AF"
            for c in df_20["cidade"]
        ]
        fig_pareto = go.Figure()
        fig_pareto.add_trace(go.Bar(
            x=df_20["cidade"],
            y=df_20["gmv_base_m"],
            name="GMV Base (R$ M)",
            marker_color=colors_pareto,
        ))
        fig_pareto.add_trace(go.Scatter(
            x=df_20["cidade"],
            y=df_20["gmv_acum_pct"],
            name="Participação Acumulada (%)",
            yaxis="y2",
            mode="lines+markers",
            line=dict(color=IFOOD_DARK, width=2.5),
        ))
        fig_pareto.add_hline(y=80, yref="y2", line_dash="dot", line_color=IFOOD_AMBER)
        fig_pareto.update_layout(
            height=420,
            yaxis=dict(title="GMV Base (R$ Milhões)"),
            yaxis2=dict(title="Acumulado (%)", overlaying="y", side="right", range=[0, 105]),
            margin=dict(t=25, b=20, l=20, r=20),
            legend=dict(orientation="h", y=1.08),
        )
        st.plotly_chart(fig_pareto, use_container_width=True)

    with p_col2:
        st.subheader("Matriz Saturação vs. Market Share (Tamanho = GMV)")
        color_map_20 = {
            "Ataque (3)": IFOOD_GREEN,
            "Turnaround (2)": IFOOD_RED,
            "Bloq. Sat >100% / OM <0 (8)": "#B91C1C",
            "Fora de Escopo (7)": "#9CA3AF",
        }
        fig_mat = px.scatter(
            df_20,
            x="share_base_pct",
            y="sat_base_pct",
            size="gmv_base_m",
            color="status_grupo",
            hover_name="cidade",
            text="cidade",
            color_discrete_map=color_map_20,
            size_max=48,
        )
        fig_mat.update_traces(textposition="top center", textfont_size=10)
        fig_mat.add_hline(y=98.0, line_dash="dash", line_color=IFOOD_AMBER, annotation_text="Teto 98% Ataque")
        fig_mat.add_hline(y=100.0, line_dash="dot", line_color=IFOOD_RED, annotation_text="100%")
        fig_mat.update_layout(
            height=420,
            xaxis_title="Market Share Base (%)",
            yaxis_title="Saturação Logística Base (%)",
            margin=dict(t=25, b=20, l=20, r=20),
            legend=dict(orientation="h", y=1.12, title=""),
        )
        st.plotly_chart(fig_mat, use_container_width=True)

# ------------------------------------------------------------------------------
# TAB 3: TURNAROUND DE CAPACIDADE (SLIDES 5 E 6)
# ------------------------------------------------------------------------------
with tab3:
    t20, t17 = st.columns(2)

    with t20:
        st.subheader("City 20 — Proteção Estratégica de Capacidade")
        st.info(
            "**GMV Base:** R$ 635,78M (45,78% do portfólio) | **Share:** 74,0% | **Alavanca:** 100% Oferta (0% cupom genérico)

"
            "- **Capacidade criada:** +700,06 mil eq. (atende 140.000 pedidos sem degradar SLA)
"
            "- **Alívio logístico:** Saturação cai de 143,87% (sem interv.) para **127,00%** (-16,87 p.p.)
"
            "- **Hipótese operacional a auditar:** Ocupação média de 47,54% vs. saturação de 141,21% sugere desbalanceamento intra-horário."
        )
        fig_20 = go.Figure(go.Bar(
            x=["Saturação Base", "Sem Intervenção (+140k ped.)", "Pós-Reforço Frota (+700,06k eq.)"],
            y=[141.21, 143.87, 127.00],
            marker_color=["#6B7280", IFOOD_RED, IFOOD_GREEN],
            text=["141,21%", "143,87%", "127,00% (-16,87 p.p.)"],
            textposition="outside",
        ))
        fig_20.add_hline(y=100.0, line_dash="dash", line_color=IFOOD_DARK)
        fig_20.update_layout(height=340, yaxis_range=[0, 165], yaxis_title="Saturação (%)")
        st.plotly_chart(fig_20, use_container_width=True)

    with t17:
        st.subheader("City 17 — Turnaround Estrutural & Unit Economics")
        st.info(
            "**GMV Base:** R$ 162,62M (11,71% do portfólio) | **OM Base:** -1,34% (-R$ 2,18M) | **Frete Grátis Base:** 54,0%

"
            "- **Capacidade criada:** +325,24 mil eq. (destrava 115.000 pedidos sem cupom genérico)
"
            "- **Alívio logístico:** Saturação cai de 138,92% (sem interv.) para **114,50%** (-24,42 p.p.)
"
            "- **Estratégia dual:** Reforço de entregadores + racionalização de frete grátis ineficiente (54%)."
        )
        fig_17 = go.Figure(go.Bar(
            x=["Saturação Base", "Sem Intervenção (+115k ped.)", "Pós-Reforço Frota (+325,24k eq.)"],
            y=[131.38, 138.92, 114.50],
            marker_color=["#6B7280", IFOOD_RED, IFOOD_GREEN],
            text=["131,38%", "138,92%", "114,50% (-24,42 p.p.)"],
            textposition="outside",
        ))
        fig_17.add_hline(y=100.0, line_dash="dash", line_color=IFOOD_DARK)
        fig_17.update_layout(height=340, yaxis_range=[0, 165], yaxis_title="Saturação (%)")
        st.plotly_chart(fig_17, use_container_width=True)

# ------------------------------------------------------------------------------
# TAB 4: SENSIBILIDADE MARGINAL & TESTE DE REALOCAÇÃO (SLIDE 7)
# ------------------------------------------------------------------------------
with tab4:
    st.subheader("Eficiência Marginal por Cidade Priorizada (MC/R$ 1 vs. Múltiplo GMV)")
    eff_df = df_active.sort_values("mc_por_real", ascending=False)

    fig_eff = go.Figure()
    fig_eff.add_trace(go.Bar(
        x=eff_df["cidade"],
        y=eff_df["mc_por_real"],
        name="MC Inc. por R$ 1,00 (R$)",
        marker_color=IFOOD_RED,
        text=eff_df["mc_por_real"].map(lambda v: f"R$ {v:.2f}"),
        textposition="outside",
    ))
    fig_eff.add_trace(go.Scatter(
        x=eff_df["cidade"],
        y=eff_df["mult_gmv"],
        name="Múltiplo de GMV (x)",
        yaxis="y2",
        mode="lines+markers+text",
        text=eff_df["mult_gmv"].map(lambda v: f"{v:.2f}x"),
        textposition="top center",
        line=dict(color=IFOOD_DARK, width=3),
    ))
    fig_eff.update_layout(
        height=370,
        yaxis=dict(title="MC Inc. / R$ 1,00 (R$)", range=[0, 1.25]),
        yaxis2=dict(title="Múltiplo GMV (x)", overlaying="y", side="right", range=[0, 13]),
        legend=dict(orientation="h", y=1.08),
    )
    st.plotly_chart(fig_eff, use_container_width=True)

    st.subheader("Teste de Realocação Marginal: Mover R$ 500 mil de City 6")
    st.dataframe(df_realoc, use_container_width=True, hide_index=True)

# ------------------------------------------------------------------------------
# TAB 5: GOVERNANÇA METODOLÓGICA & ROADMAP (SLIDES 8 E 9)
# ------------------------------------------------------------------------------
with tab5:
    st.subheader("Matriz de Governança Metodológica: Fatos Observados vs. Premissas & Experimentos")
    gov_df = pd.DataFrame([
        ("Elasticidade-Preço", "Price Index observado (City 2 = 116,84%; City 3 = 101,27%)", "Faixa conservadora -0,6 a -1,4 (base -1,0)", "Geo-split (bairros trat. vs. controle) por 4 semanas"),
        ("Elasticidade a Incentivo", "Custo/Pedido inc. observado (R$ 5,00 a R$ 8,00)", "Modelada separadamente (sem proxy de preço)", "Mensuração de pedidos inc. líquidos sobre controle"),
        ("Elasticidade Frete Grátis", "Cobertura base (City 2 = 55%, City 17 = 54%, City 3 = 27%)", "Retorno marginal decrescente acima de 50%", "Teste A/B de pedido mínimo em City 3"),
        ("Canibalização por Alavanca", "Não observada na base agregada (limitação estrutural)", "Incentivos 30-50% (C6: 37,5%); Frete 20-40% (C3: 30%); Preço 10-30% (C2: 25%)", "Análise de cohort semanal (orgânico vs. incentivado)"),
        ("Custo de Capacidade", "Saturação >100% em 6 cidades; Custo/hora R$ 9-13/h", "Alavanca de oferta (0% canibalização)", "Teste switchback por turno/zona (aceite e SLA)"),
        ("Hipótese City 20", "Saturação 141,21% vs. Ocupação média 47,54%", "Desbalanceamento temporal picos/vales", "Auditoria granular de dados intra-horários"),
    ], columns=["Componente Analítico", "Fato Observado na Base", "Premissa Analítica & Limitação", "Protocolo de Validação"])
    st.dataframe(gov_df, use_container_width=True, hide_index=True)

    st.subheader("Roadmap de Implantação Controlada (Semanas 1 a 8)")
    r1, r2, r3 = st.columns(3)
    r1.success("**Semanas 1–2 | Setup & Auditoria**

Desenho *geo-split* (ataque) e *switchback* (capacidade) + auditoria intra-horária na City 20.")
    r2.warning("**Semanas 3–6 | Piloto Controlado**

Execução nas 5 praças sob gatilhos automáticos de pausa (Sat >98% ou SLA +8%).")
    r3.info("**Semanas 7–8 | Leitura D30 & Escala**

Calibração de elasticidade real, canibalização e retenção D30 para revisão mensal.")
