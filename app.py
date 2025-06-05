import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend to avoid rendering issues

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Compute 3d6 probability distribution
def get_3d6_distribution():
    """
    Calculates the probability distribution of sums from rolling 3 six-sided dice (3d6).
    Returns probabilities for sums from 3 to 18.
    """
    outcomes = 6 ** 3  # Total possible outcomes = 216
    counts = np.zeros(19)  # Index 0-18, only sums 3-18 are valid
    for d1 in range(1, 7):
        for d2 in range(1, 7):
            for d3 in range(1, 7):
                counts[d1 + d2 + d3] += 1
    probabilities = counts / outcomes
    return probabilities[3:]  # Return probabilities for sums 3 to 18

# Streamlit app title
st.title("Distribuição de soma de 3d6")

# Get probability distribution and corresponding sums
prob_dist = get_3d6_distribution()
sums = np.arange(3, 19)  # Valid sums: 3 to 18

# User input: current value threshold
current_value = st.number_input(
    "Insert current value (3-18):", min_value=3, max_value=18, value=10, step=1
)

# Calculate probability of rolling above the current value
chance_above = np.sum(prob_dist[sums > current_value])

# Display chance
st.write(f"Chance de ser **acima** da soma {current_value}: {chance_above:.4f} ({chance_above*100:.2f}%)")

# Plotting with matplotlib
fig, ax = plt.subplots(figsize=(8, 4))

# Red bars for distribution
ax.bar(sums, prob_dist, color='red', edgecolor='black')

# Light grey background
ax.set_facecolor('#f0f0f0')

# Dashed vertical line at current value
ax.axvline(
    current_value,
    color='black',
    linestyle='--',
    linewidth=2,
    label=f'Limite = {current_value}'
)

# Labels and title
ax.set_xlabel("Soma do 3d6")
ax.set_ylabel("Probabilidade")
ax.set_title("Distribuição de Probabilidade de Soma de 3d6")

# Show legend
ax.legend()

# Improve layout
plt.tight_layout()

# Render plot in Streamlit
st.pyplot(fig)

# Close figure to prevent memory issues
plt.close(fig)
