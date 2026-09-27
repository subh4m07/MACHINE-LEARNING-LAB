import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_wine

wine = load_wine()

df = pd.DataFrame(wine.data, columns=wine.feature_names)

correlation = df.corr()

print("----- Correlation Matrix -----")
print(correlation)

plt.figure(figsize=(12, 8))

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation Heatmap")
plt.show()

correlation_values = correlation.where(
    ~np.eye(correlation.shape[0], dtype=bool)
)

strongest = correlation_values.stack().idxmax()
value = correlation_values.stack().max()

print("\n----- Strongest Positive Correlation -----")
print("Features:", strongest)
print("Correlation:", value)