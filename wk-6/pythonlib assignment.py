import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

# -----------------------------------------
# 1. NumPy: Create array and calculate mean
# -----------------------------------------
arr = np.arange(1, 11)
mean_val = np.mean(arr)
print("NumPy Array:", arr)
print("Mean of array:", mean_val)

# -----------------------------------------
# 2. Pandas: Create a DataFrame and summarize
# -----------------------------------------
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 25, 22],
    'Score': [88, 92, 79]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)
print("\nSummary Statistics:\n", df.describe())

# -----------------------------------------
# 3. Requests: Fetch data from a public API
# We'll use the "Bored API" for fun activities
# -----------------------------------------
response = requests.get("https://www.boredapi.com/api/activity")
if response.status_code == 200:
    activity_data = response.json()
    print("\nFetched Activity Suggestion:")
    print("👉", activity_data.get("activity"))
else:
    print("Failed to fetch activity. Status code:", response.status_code)

# -----------------------------------------
# 4. Matplotlib: Simple line plot
# -----------------------------------------
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.figure(figsize=(6, 4))
plt.plot(x, y, marker='o', linestyle='-', color='green')
plt.title("Simple Line Graph")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.tight_layout()

# ✅ Save the figure as PNG
plt.savefig("simple_line_graph.png")
plt.close()

print("\n✅ Line graph saved as 'simple_line_graph.png'")
