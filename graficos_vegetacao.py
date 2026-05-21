"""
Gráficos de Vegetação — Dataset IBGE/RADAMBRASIL
================================================
INSTRUÇÕES:
  1. Coloque este arquivo na mesma pasta que os dois .xls
  2. No terminal do VS Code, rode: python graficos_vegetacao.py
  3. Os gráficos vão abrir na tela automaticamente
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# ── Carregamento dos dados ────────────────────────────────────────────────────
print("Carregando dados...")
df = pd.read_excel("vege_tabela_area.xls", engine="openpyxl")
print(f"  {len(df)} registros carregados com sucesso!\n")

# ── Paleta de cores ───────────────────────────────────────────────────────────
CORES_GRUPOS = [
    "#1b4332", "#2d6a4f", "#40916c", "#52b788", "#74c69d",
    "#95d5b2", "#b7e4c7", "#d8f3dc", "#c77dff", "#9b5de5",
    "#f15bb5", "#fee440", "#00bbf9",
]

# ═══════════════════════════════════════════════════════════════════════════════
# GRÁFICO 1 — Área por Grande Grupo de Vegetação (barras horizontais)
# ═══════════════════════════════════════════════════════════════════════════════
print("Gerando Gráfico 1: Área por Grande Grupo de Vegetação...")

grp = (
    df.groupby("legenda_1")["ar_poli_km"]
    .sum()
    .sort_values()
)
grp_milhoes = grp / 1e6

fig1, ax1 = plt.subplots(figsize=(12, 7))
fig1.patch.set_facecolor("#f8f9fa")
ax1.set_facecolor("#f0f4f0")

cores_barra = CORES_GRUPOS[: len(grp)]
bars = ax1.barh(grp.index, grp_milhoes.values, color=cores_barra[::-1],
                edgecolor="white", linewidth=0.6, height=0.7)

for bar, val in zip(bars, grp_milhoes.values):
    ax1.text(
        val + 0.01, bar.get_y() + bar.get_height() / 2,
        f"{val:.2f} M km²",
        va="center", ha="left", fontsize=8.5, color="#333333"
    )

ax1.set_xlabel("Área (milhões de km²)", fontsize=11, labelpad=8)
ax1.set_title(
    "Área por Grande Grupo de Vegetação no Brasil",
    fontsize=14, fontweight="bold", pad=14, color="#1b4332"
)
ax1.tick_params(axis="y", labelsize=9.5)
ax1.tick_params(axis="x", labelsize=9)
ax1.spines[["top", "right"]].set_visible(False)
ax1.set_xlim(0, grp_milhoes.max() * 1.20)
ax1.grid(axis="x", linestyle="--", alpha=0.4, color="gray")
plt.tight_layout()

# ═══════════════════════════════════════════════════════════════════════════════
# GRÁFICO 2 — Proporção por Tipo de Dominância (donut)
# ═══════════════════════════════════════════════════════════════════════════════
print("Gerando Gráfico 2: Proporção por Tipo de Dominância...")

dom = df.groupby("leg_sup")["ar_poli_km"].sum().sort_values(ascending=False)

LABELS_CURTOS = {
    "Vegetação Natural Dominante": "Veg. Natural",
    "Área Antrópica Dominante": "Área Antrópica",
    "Vegetação Natural Dominante em Tensão Ecológica": "Veg. Natural\n(Tensão Ecológica)",
    "Área Antrópica Dominante em Tensão Ecológica": "Antrópica\n(Tensão Ecológica)",
    "Massa D´água": "Massa d'Água",
}
labels_curtos = [LABELS_CURTOS.get(l, l) for l in dom.index]
CORES_DONUT = ["#2d6a4f", "#d62828", "#74c69d", "#e07a5f", "#457b9d"]

fig2, ax2 = plt.subplots(figsize=(9, 7))
fig2.patch.set_facecolor("#f8f9fa")
ax2.set_facecolor("#f8f9fa")

wedges, texts, autotexts = ax2.pie(
    dom.values,
    labels=None,
    autopct="%1.1f%%",
    pctdistance=0.80,
    colors=CORES_DONUT,
    startangle=90,
    wedgeprops=dict(width=0.55, edgecolor="white", linewidth=2),
)
for at in autotexts:
    at.set_fontsize(9.5)
    at.set_color("white")
    at.set_fontweight("bold")

ax2.text(0, 0, f"Total\n{dom.sum()/1e6:.1f} M\nkm²",
         ha="center", va="center", fontsize=11, fontweight="bold", color="#1b4332")

patches = [
    mpatches.Patch(
        color=CORES_DONUT[i],
        label=f"{labels_curtos[i]}  ({dom.values[i]/1e6:.2f} M km²)"
    )
    for i in range(len(dom))
]
ax2.legend(handles=patches, loc="center left", bbox_to_anchor=(1.02, 0.5),
           fontsize=9, framealpha=0.9, edgecolor="#cccccc")
ax2.set_title(
    "Proporção da Área por Tipo de Dominância",
    fontsize=14, fontweight="bold", pad=18, color="#1b4332"
)
plt.tight_layout()

# ═══════════════════════════════════════════════════════════════════════════════
# GRÁFICO 3 — Top 12 Subformações por Área (barras verticais)
# ═══════════════════════════════════════════════════════════════════════════════
print("Gerando Gráfico 3: Top 12 Subformações por Área...")

sub = (
    df.groupby("legenda_2")["ar_poli_km"]
    .sum()
    .sort_values(ascending=False)
    .head(12)
)
sub_mil = sub / 1e3

ANTR = {"Pecuária (pastagens)", "Agropecuária", "Agricultura", "Vegetação Secundária"}
cores_sub = ["#d62828" if n in ANTR else "#40916c" for n in sub.index]

fig3, ax3 = plt.subplots(figsize=(13, 7))
fig3.patch.set_facecolor("#f8f9fa")
ax3.set_facecolor("#f0f4f0")

bars3 = ax3.bar(range(len(sub)), sub_mil.values, color=cores_sub,
                edgecolor="white", linewidth=0.6, width=0.7)

for bar, val in zip(bars3, sub_mil.values):
    ax3.text(
        bar.get_x() + bar.get_width() / 2, val + 5,
        f"{val:,.0f}", ha="center", va="bottom", fontsize=8.5, color="#333333"
    )

ax3.set_xticks(range(len(sub)))
ax3.set_xticklabels(
    [n.replace(" com ", "\ncom ").replace(" das ", "\ndas ").replace(" sem ", "\nsem ")
     for n in sub.index],
    fontsize=8, rotation=30, ha="right"
)
ax3.set_ylabel("Área (mil km²)", fontsize=11, labelpad=8)
ax3.set_title(
    "Top 12 Subformações de Vegetação por Área (mil km²)",
    fontsize=14, fontweight="bold", pad=14, color="#1b4332"
)
ax3.spines[["top", "right"]].set_visible(False)
ax3.grid(axis="y", linestyle="--", alpha=0.4, color="gray")
ax3.set_ylim(0, sub_mil.max() * 1.15)

p_nat = mpatches.Patch(color="#40916c", label="Vegetação Natural")
p_ant = mpatches.Patch(color="#d62828", label="Área Antrópica")
ax3.legend(handles=[p_nat, p_ant], loc="upper right", fontsize=10,
           framealpha=0.9, edgecolor="#cccccc")
plt.tight_layout()

# ── Exibe todos os gráficos na tela ──────────────────────────────────────────
print("\nAbrindo gráficos... (feche as janelas para encerrar o programa)")
plt.show()
