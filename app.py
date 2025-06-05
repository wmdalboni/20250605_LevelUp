import matplotlib
matplotlib.use('Agg')  # Backend não-interativo

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Função para calcular distribuição do 3d6
def get_3d6_distribution():
    """
    Aqui eu calculo a distribuição de probabilidade para a soma de 3 dados de 6 lados.
    """
    outcomes = 6 ** 3
    counts = np.zeros(19)
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                counts[d1 + d2 + d3] += 1
    probabilities = counts / outcomes
    return probabilities[3:]

# Título
st.title("Distribuição da Soma de 3d6")

# Distribuição e somas
prob_dist = get_3d6_distribution()
sums = np.arange(3, 19)

# Input do usuário
current_value = st.number_input(
    "Insira o valor atual (3-18):", min_value=3, max_value=18, value=10, step=1
)

# Probabilidades
chance_above = np.sum(prob_dist[sums > current_value])
chance_below = np.sum(prob_dist[sums <= current_value])

# Exibição
st.write(f"Chance da soma ser **acima** de {current_value}: {chance_above:.4f} ({chance_above*100:.2f}%)")
st.write(f"Chance da soma ser **igual ou abaixo** de {current_value}: {chance_below:.4f} ({chance_below*100:.2f}%)")

# Plotagem
fig, ax = plt.subplots(figsize=(8, 4))
ax.set_facecolor('#f0f0f0')

mask_red = sums <= current_value
mask_blue = sums > current_value

# Barras vermelhas
ax.bar(
    sums[mask_red],
    prob_dist[mask_red],
    color='red',
    alpha=0.6,
    edgecolor='black',
    label='≤ Limite'
)

# Barras azuis
ax.bar(
    sums[mask_blue],
    prob_dist[mask_blue],
    color='blue',
    alpha=0.6,
    edgecolor='black',
    label='> Limite'
)

# Linha tracejada
ax.axvline(
    current_value,
    color='black',
    linestyle='--',
    linewidth=2,
    label=f'Limite = {current_value}'
)

# Bubble para a % abaixo
ax.text(
    current_value - 2,
    max(prob_dist) * 0.9,
    f"{chance_below*100:.1f}%",
    color='white',
    ha='right',
    fontsize=10,
    weight='bold',
    bbox=dict(
        boxstyle='round,pad=0.3',
        facecolor='red',
        alpha=0.6,
        edgecolor='black'
    )
)

# Bubble para a % acima
ax.text(
    current_value + 2,
    max(prob_dist) * 0.9,
    f"{chance_above*100:.1f}%",
    color='white',
    ha='left',
    fontsize=10,
    weight='bold',
    bbox=dict(
        boxstyle='round,pad=0.3',
        facecolor='blue',
        alpha=0.6,
        edgecolor='black'
    )
)

# Rótulos e título
ax.set_xlabel("Soma de 3d6")
ax.set_ylabel("Probabilidade")
ax.set_title("Distribuição de Probabilidade do 3d6")
ax.legend()

plt.tight_layout()
st.pyplot(fig)
plt.close(fig)
