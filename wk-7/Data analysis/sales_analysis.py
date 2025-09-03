import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("sales_data.csv")

# Calculate total revenue
total_revenue = df["Revenue ($)"].sum()

# Find best-selling product (by quantity sold)
best_selling_product = df.groupby("Product")["Quantity Sold"].sum().idxmax()

# Find the day with the highest total sales (by revenue)
top_sales_day = df.groupby("Date")["Revenue ($)"].sum().idxmax()

# Save insights to a text file
with open("sales_summary.txt", "w", encoding="utf-8") as file:
    file.write("📊 Sales Summary Report\n")
    file.write("------------------------\n")
    file.write(f"✅ Total Revenue: ${total_revenue:,.2f}\n")
    file.write(f"🏆 Best-Selling Product: {best_selling_product}\n")
    file.write(f"📅 Day with Highest Sales: {top_sales_day}\n")

# Print results in user-friendly format
print("📊 Sales Summary:")
print(f"✅ Total Revenue: ${total_revenue:,.2f}")
print(f"🏆 Best-Selling Product: {best_selling_product}")
print(f"📅 Day with Highest Sales: {top_sales_day}")

# 🎯 Bonus: Visualize sales trends
# Convert Date to datetime format
df["Date"] = pd.to_datetime(df["Date"])

# Group by date to get daily revenue
daily_revenue = df.groupby("Date")["Revenue ($)"].sum()

# Plot the trend
plt.figure(figsize=(10, 6))
plt.plot(daily_revenue.index, daily_revenue.values, marker='o', color='teal')
plt.title("📈 Daily Revenue Trend")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("sales_trend.png")  # Saves the plot
print("📉 Sales trend chart saved as sales_trend.png")

