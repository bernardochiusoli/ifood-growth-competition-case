import pytest

# Fechamento auditado das 5 praças priorizadas (Slide 2)
PORTFOLIO = {
    "City 3": {"mc_inc": 1_772_232.0, "custo_bruto": 2_800_000.0, "custo_op": 0.0, "sat_pos": 96.75, "grupo": "ataque"},
    "City 2": {"mc_inc": 1_161_216.0, "custo_bruto": 1_200_000.0, "custo_op": 0.0, "sat_pos": 96.29, "grupo": "ataque"},
    "City 6": {"mc_inc": 555_930.0, "custo_bruto": 1_600_000.0, "custo_op": 0.0, "sat_pos": 94.12, "grupo": "ataque"},
    "City 17": {"mc_inc": 687_447.0, "custo_bruto": 3_152_395.0, "custo_op": 200_000.0, "sat_pos": 114.50, "grupo": "turnaround"},
    "City 20": {"mc_inc": 955_570.0, "custo_bruto": 5_880_000.0, "custo_op": 300_000.0, "sat_pos": 127.00, "grupo": "turnaround"},
}


def test_fechamento_exato_operating_margin():
    tot_mc = sum(v["mc_inc"] for v in PORTFOLIO.values())
    tot_bruto = sum(v["custo_bruto"] for v in PORTFOLIO.values())
    tot_op = sum(v["custo_op"] for v in PORTFOLIO.values())
    impacto_om = tot_mc - tot_bruto - tot_op

    assert tot_mc == pytest.approx(5_132_395.0)
    assert tot_bruto == pytest.approx(14_632_395.0)
    assert tot_op == pytest.approx(500_000.0)
    assert impacto_om == pytest.approx(-10_000_000.0)


def test_guardrail_saturacao_frente_ataque():
    for cidade, dados in PORTFOLIO.items():
        if dados["grupo"] == "ataque":
            assert dados["sat_pos"] <= 98.0, f"{cidade} violou guardrail de 98%: {dados['sat_pos']}%"
