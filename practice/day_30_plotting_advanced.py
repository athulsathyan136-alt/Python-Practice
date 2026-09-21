# Day 30: Advanced Plotting
import matplotlib.pyplot as plt
import numpy as np

print("Generating advanced charts... (Close each window to see the next)")

# ==========================================
# 1. STYLED LINE CHART
# ==========================================
plt.figure(figsize=(10, 6))

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, 'b-', linewidth=2, label='sin(x)')
plt.plot(x, y2, 'r--', linewidth=2, label='cos(x)')

plt.title("Sine and Cosine Waves", fontsize=16, fontweight='bold')
plt.xlabel("X axis", fontsize=12)
plt.ylabel("Y axis", fontsize=12)
plt.legend(fontsize=12)
plt.grid(True, alpha=0.3)
plt.savefig("advanced1_waves.png", dpi=150)
plt.show()

# ==========================================
# 2. MULTIPLE LINES (Model Comparison)
# ==========================================
plt.figure(figsize=(10, 6))

epochs = np.arange(1, 21)
model_a = 1 - np.exp(-epochs / 3)
model_b = 1 - np.exp(-epochs / 5)
model_c = 1 - np.exp(-epochs / 7)

plt.plot(epochs, model_a, 'o-', label='Model A (Fast)', color='green')
plt.plot(epochs, model_b, 's-', label='Model B (Medium)', color='orange')
plt.plot(epochs, model_c, '^-', label='Model C (Slow)', color='red')

plt.title("Model Training Comparison", fontsize=16, fontweight='bold')
plt.xlabel("Epoch", fontsize=12)
plt.ylabel("Accuracy", fontsize=12)
plt.legend(fontsize=11, loc='lower right')
plt.grid(True, alpha=0.3)
plt.ylim(0, 1.05)
plt.savefig("advanced2_models.png", dpi=150)
plt.show()

# ==========================================
# 3. HEATMAP (Feature Correlation)
# ==========================================
plt.figure(figsize=(8, 6))

# Simulate a correlation matrix
np.random.seed(42)
data = np.random.rand(6, 6)
correlation = (data + data.T) / 2  # Make it symmetric
np.fill_diagonal(correlation, 1)   # Diagonal is 1

labels = ['Python', 'AI', 'Cloud', 'SQL', 'Docker', 'K8s']
plt.imshow(correlation, cmap='coolwarm', vmin=0, vmax=1)

plt.colorbar(label='Correlation')
plt.xticks(range(6), labels, rotation=45)
plt.yticks(range(6), labels)
plt.title("Skill Correlation Heatmap", fontsize=14, fontweight='bold')

# Add text values in each cell
for i in range(6):
    for j in range(6):
        plt.text(j, i, f'{correlation[i, j]:.2f}',
                ha='center', va='center', color='black', fontsize=9)

plt.tight_layout()
plt.savefig("advanced3_heatmap.png", dpi=150)
plt.show()

# ==========================================
# 4. GAUGE / DONUT (Progress)
# ==========================================
fig, ax = plt.subplots(figsize=(6, 6))

# Outer donut
sizes = [75, 25]
colors = ['#4CAF50', '#E0E0E0']
wedges, texts = ax.pie(sizes, colors=colors, startangle=90,
                        wedgeprops=dict(width=0.3, edgecolor='white'))

# Inner donut
sizes2 = [60, 40]
colors2 = ['#2196F3', '#E0E0E0']
ax.pie(sizes2, colors=colors2, radius=0.6, startangle=90,
       wedgeprops=dict(width=0.3, edgecolor='white'))

ax.text(0, 0, "75%\nComplete", ha='center', va='center',
        fontsize=16, fontweight='bold')

plt.title("Portfolio Progress", fontsize=14, fontweight='bold')
plt.savefig("advanced4_donut.png", dpi=150)
plt.show()

# ==========================================
# 5. ADVANCED SUBPLOTS (2x3 Grid)
# ==========================================
fig, axes = plt.subplots(2, 3, figsize=(15, 10))
fig.suptitle("AI Engineering Dashboard", fontsize=16, fontweight='bold')

# Top-left: Loss curve
axes[0, 0].plot(range(1, 11), [10, 7, 5, 3.5, 2.5, 1.8, 1.4, 1.1, 0.9, 0.8], 'r-')
axes[0, 0].set_title("Training Loss")
axes[0, 0].set_xlabel("Epoch")
axes[0, 0].grid(True, alpha=0.3)

# Top-middle: Accuracy
axes[0, 1].plot(range(1, 11), [0.5, 0.65, 0.75, 0.82, 0.87, 0.90, 0.92, 0.94, 0.955, 0.97], 'g-')
axes[0, 1].set_title("Accuracy")
axes[0, 1].set_xlabel("Epoch")
axes[0, 1].grid(True, alpha=0.3)

# Top-right: Bar
axes[0, 2].bar(['Train', 'Val', 'Test'], [97, 94, 93], color=['#4CAF50', '#FF9800', '#2196F3'])
axes[0, 2].set_title("Final Performance")

# Bottom-left: Confusion matrix heatmap
cm = np.array([[85, 5, 10], [3, 90, 7], [8, 4, 88]])
axes[1, 0].imshow(cm, cmap='Blues')
axes[1, 0].set_title("Confusion Matrix")
axes[1, 0].set_xticks([0, 1, 2]); axes[1, 0].set_xticklabels(['A', 'B', 'C'])
axes[1, 0].set_yticks([0, 1, 2]); axes[1, 0].set_yticklabels(['A', 'B', 'C'])

# Bottom-middle: Histogram
axes[1, 1].hist(np.random.randn(500), bins=25, color='purple', edgecolor='black')
axes[1, 1].set_title("Data Distribution")

# Bottom-right: Pie
axes[1, 2].pie([40, 30, 20, 10], labels=['AI', 'Cloud', 'DevOps', 'Other'],
               autopct='%1.0f%%', startangle=90)
axes[1, 2].set_title("Skill Breakdown")

plt.tight_layout()
plt.savefig("advanced5_dashboard.png", dpi=150)
plt.show()

print("\n✅ 5 advanced charts created!")
print("Files saved:")
print("  - advanced1_waves.png")
print("  - advanced2_models.png")
print("  - advanced3_heatmap.png")
print("  - advanced4_donut.png")
print("  - advanced5_dashboard.png")