# scripts/iris_analysis.py

import pandas as pd
from sklearn.datasets import load_iris

# Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# Save to CSV
df.to_csv("data/iris.csv", index=False)
print("✅ Iris dataset saved to data/iris.csv")

