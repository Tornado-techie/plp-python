import pandas as pd

# Step 1: Load the dataset
df = pd.read_csv("data/iris.csv")

# Step 2: Display the first 5 rows
print("🔍 First 5 rows of the dataset:")
print(df.head())

# Step 3: Display data types and missing values
print("\n📊 Data types:")
print(df.dtypes)

print("\n❓ Missing values per column:")
print(df.isnull().sum())

# Step 4: Basic statistics
print("\n📈 Descriptive Statistics:")
print(df.describe())

# Step 5: Grouping by species and calculating mean of each feature
print("\n🔎 Average measurements per species:")
print(df.groupby("species").mean(numeric_only=True))

