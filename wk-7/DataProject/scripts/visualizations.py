# scripts/visualizations.py

import pandas as pd
import matplotlib.pyplot as plt
import os

# Load the Iris dataset
df = pd.read_csv("data/iris.csv")

# Create output directory if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# 1. Line chart: Trend of sepal length over index
plt.figure(figsize=(10, 5))
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length", color="blue")
plt.title("Trend of Sepal Length")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.legend()
plt.savefig("outputs/sepal_length_trend.png")
plt.close()

# 2. Bar chart: Average petal length per species
species_avg = df.groupby("target")["petal length (cm)"].mean()
plt.figure(figsize=(8, 5))
plt.bar(species_avg.index.astype(str), species_avg.values, color="green")
plt.title("Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
plt.savefig("outputs/avg_petal_length_bar.png")
plt.close()

# 3. Histogram: Distribution of sepal width
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=10, color="orange", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.savefig("outputs/sepal_width_histogram.png")
plt.close()

# 4. Scatter plot: Sepal length vs. Petal length
plt.figure(figsize=(8, 5))
plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], c="red", alpha=0.6)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.savefig("outputs/sepal_vs_petal_scatter.png")
plt.close()

print("✅ Visualizations saved to outputs/")
