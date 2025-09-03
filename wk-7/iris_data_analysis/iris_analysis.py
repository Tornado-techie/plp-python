# iris_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set Seaborn style for prettier plots
sns.set(style="whitegrid")

# Load the dataset with error handling
try:
    file_path = "data/iris.csv"
    df = pd.read_csv(file_path)
    print("✅ Dataset loaded successfully.\n")
except FileNotFoundError:
    print(f"❌ Error: File not found at {file_path}. Make sure the dataset exists.")
    exit()
except pd.errors.EmptyDataError:
    print("❌ Error: The file is empty.")
    exit()
except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
    exit()

# Display the first few rows
print("🔍 First 5 rows of the dataset:")
print(df.head(), "\n")

# Check data types and missing values
print("📊 Data Types:")
print(df.dtypes, "\n")

print("🧼 Missing Values:")
print(df.isnull().sum(), "\n")

# Clean data (remove missing rows if any)
if df.isnull().values.any():
    df = df.dropna()
    print("✅ Missing values found and removed.\n")
else:
    print("✅ No missing values found.\n")

# Basic statistics
print("📈 Basic Statistics:")
print(df.describe(), "\n")

# Group by species and compute mean
print("🔍 Mean of numeric columns grouped by species:")
print(df.groupby("target").mean(), "\n")

# Create visualizations folder if it doesn't exist
os.makedirs("visualizations", exist_ok=True)

# 1. Line plot – trend of sepal length over index
plt.figure()
plt.plot(df.index, df["sepal length (cm)"], label="Sepal Length")
plt.title("Line Plot of Sepal Length (Index as Time)")
plt.xlabel("Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.savefig("visualizations/line_plot_sepal_length.png")
plt.close()

# 2. Bar chart – avg petal length per species
plt.figure()
sns.barplot(x="target", y="petal length (cm)", data=df, estimator='mean')
plt.title("Average Petal Length per Species")
plt.xlabel("Species (target)")
plt.ylabel("Petal Length (cm)")
plt.savefig("visualizations/bar_chart_petal_length.png")
plt.close()

# 3. Histogram – distribution of sepal width
plt.figure()
sns.histplot(df["sepal width (cm)"], bins=10, kde=True)
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.savefig("visualizations/histogram_sepal_width.png")
plt.close()

# 4. Scatter plot – sepal length vs. petal length
plt.figure()
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="target", data=df)
plt.title("Sepal Length vs. Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.savefig("visualizations/scatter_sepal_vs_petal.png")
plt.close()

print("✅ Visualizations created and saved in the 'visualizations/' folder.")
