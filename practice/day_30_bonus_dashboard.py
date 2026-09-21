# Day 30 - Bonus: Sales Data Dashboard
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

print("Building Sales Dashboard...")

# ==========================================
# 1. GENERATE FAKE SALES DATA
# ==========================================
np.random.seed(42)

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Simulate sales with an upward trend
sales_data = {
    'Month': months,
    'Laptop': np.random.randint(30, 100, 12),
    'Phone': np.random.randint(50, 150, 12),
    'Tablet': np.random.randint(20, 80, 12),
    'Headphones': np.random.randint(40, 120, 12)
}

df = pd.DataFrame(sales_data)
df['Total'] = df[['Laptop', 'Phone', 'Tablet', 'Headphones']].sum(axis=1)

print("\n📊 Sales Data:")
print(df)

# ==========================================
# 2. CREATE A 4-PANEL DASHBOARD
# ==========================================
fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("📊 YEARLY SALES DASHBOARD", fontsize=18, fontweight='bold')

# --- Panel 1: Total Sales Over Time (Line) ---
axes[0, 0].plot(df['Month'], df['Total'], 'b-o', linewidth=2, markersize=8)
axes[0, 0].fill_between(df['Month'], df['Total'], alpha=0.2, color='blue')
axes[0, 0].set_title("Total Monthly Sales", fontsize=14, fontweight='bold')
axes[0, 0].set_ylabel("Units Sold")
axes[0, 0].grid(True, alpha=0.3)
axes[0, 0].tick_params(axis='x', rotation=45)

# --- Panel 2: Product Comparison (Bar) ---
products = ['Laptop', 'Phone', 'Tablet', 'Headphones']
totals = [df[p].sum() for p in products]
colors = ['#FF6F00', '#FF9900', '#FFB300', '#FFC107']

bars = axes[0, 1].bar(products, totals, color=colors, edgecolor='black')
for bar, total in zip(bars, totals):
    axes[0, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 20,
                    f'{total}', ha='center', fontweight='bold')
axes[0, 1].set_title("Yearly Product Sales", fontsize=14, fontweight='bold')
axes[0, 1].set_ylabel("Total Units")
axes[0, 1].grid(True, alpha=0.3, axis='y')

# --- Panel 3: Market Share (Pie) ---
axes[1, 0].pie(totals, labels=products, autopct='%1.1f%%',
               colors=colors, startangle=90, explode=[0.05, 0.05, 0.05, 0.05])
axes[1, 0].set_title("Market Share by Product", fontsize=14, fontweight='bold')

# --- Panel 4: Growth Rate (Bar with Colors) ---
growth = df['Total'].pct_change() * 100
growth = growth.fillna(0)
bar_colors = ['green' if g > 0 else 'red' for g in growth]

axes[1, 1].bar(df['Month'], growth, color=bar_colors, edgecolor='black')
axes[1, 1].axhline(y=0, color='black', linewidth=1)
axes[1, 1].set_title("Month-over-Month Growth (%)", fontsize=14, fontweight='bold')
axes[1, 1].set_ylabel("Growth %")
axes[1, 1].grid(True, alpha=0.3, axis='y')
axes[1, 1].tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig("sales_dashboard.png", dpi=150)
plt.show()

# ==========================================
# 3. KEY METRICS SUMMARY
# ==========================================
print("\n" + "=" * 50)
print("📈 KEY METRICS")
print("=" * 50)
print(f"Total Sales: {df['Total'].sum():,} units")
print(f"Average Monthly Sales: {df['Total'].mean():.0f} units")
print(f"Best Month: {df.loc[df['Total'].idxmax(), 'Month']} ({df['Total'].max()} units)")
print(f"Worst Month: {df.loc[df['Total'].idxmin(), 'Month']} ({df['Total'].min()} units)")
print(f"Best-Selling Product: {products[totals.index(max(totals))]} ({max(totals)} units)")

# ==========================================
# 4. SAVE DATA TO CSV
# ==========================================
df.to_csv("sales_report.csv", index=False)
print("\n✅ Data saved to sales_report.csv")
print("✅ Chart saved to sales_dashboard.png")