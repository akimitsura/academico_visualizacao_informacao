# 🌿 Vegetação Brasileira — Visualização de Dados

Análise e visualização da cobertura vegetal do Brasil com base nos dados oficiais do **IBGE/RADAMBRASIL**, utilizando Python, pandas e matplotlib.

---

## 📊 Gráficos Gerados

### 1. Área por Grande Grupo de Vegetação
Comparação das grandes regiões fitoecológicas do Brasil em milhões de km².

![Gráfico 1](grafico1_grupos_vegetacao.png)

---

### 2. Proporção por Tipo de Dominância
Visão geral da composição territorial: vegetação natural, áreas antrópicas e massas d'água.

![Gráfico 2](grafico2_dominancia.png)

---

### 3. Top 12 Subformações por Área
Ranking das subformações vegetais com maior extensão territorial, com destaque visual para áreas antrópicas (vermelho) e naturais (verde).

![Gráfico 3](grafico3_subformacoes.png)

---

## 📁 Estrutura do Repositório

```
📦 vegetacao-brasil
 ┣ 📄 graficos_vegetacao.py       # Script principal
 ┣ 📊 vege_tabela_area.xls              # Dados de área por polígono
 ┣ 📖 vege_tabela_dicionario_conceitos.xls  # Dicionário de conceitos
 ┣ 🖼️ grafico1_grupos_vegetacao.png    # Gráfico 1
 ┣ 🖼️ grafico2_dominancia.png          # Gráfico 2
 ┣ 🖼️ grafico3_subformacoes.png        # Gráfico 3
 ┗ 📄 README.md
```

---

## 🚀 Como Rodar Localmente

### Pré-requisitos

- Python 3.8 ou superior
- pip

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/vegetacao-brasil.git
cd vegetacao-brasil
```

### 2. Instale as dependências

```bash
pip install pandas matplotlib openpyxl
```

### 3. Execute o script

```bash
python graficos_vegetacao.py
```

Os três gráficos vão abrir automaticamente na tela.

---

## 🗂️ Sobre os Dados

| Arquivo | Descrição |
|---|---|
| `vege_tabela_area.xls` | 145.458 registros com área (km²) por polígono de vegetação |
| `vege_tabela_dicionario_conceitos.xls` | Dicionário com descrição de cada tipologia vegetal |

Os dados são provenientes do projeto **RADAMBRASIL** e organizados pelo **IBGE**, cobrindo todas as fitofisionomias do território nacional.

### Principais colunas utilizadas

| Coluna | Descrição |
|---|---|
| `legenda_1` | Grande grupo de vegetação (ex: Floresta Ombrófila Densa) |
| `legenda_2` | Subformação vegetal |
| `leg_sup` | Tipo de dominância (natural, antrópica, água) |
| `ar_poli_km` | Área do polígono em km² |

---

## 🧠 O que cada gráfico mostra

**Gráfico 1 — Barras Horizontais**
> Ideal para comparar categorias com nomes longos. Mostra que a **Floresta Ombrófila Densa** é o maior grupo com ~2,2 milhões de km², seguida de Contatos/Ecotonos e Savana.

**Gráfico 2 — Donut**
> Evidencia a composição territorial: a vegetação natural ainda domina, mas a **área antrópica já ocupa quase 30% do território** analisado — um dado preocupante.

**Gráfico 3 — Barras Verticais com cores condicionais**
> Revela que **Pecuária e Agropecuária** estão entre as maiores "subformações" do país, disputando espaço com formações naturais como a Floresta Ombrófila Densa Submontana.

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=flat)

---

## 📜 Fonte dos Dados

> Instituto Brasileiro de Geografia e Estatística — IBGE  
> Projeto RADAMBRASIL  
> [www.ibge.gov.br]([https://www.ibge.gov.br](https://bdiaweb.ibge.gov.br/#/consulta/vegetacao))

---

*Desenvolvido como projeto de finalidade acadêmica para o curso de sistemas de informação.*
