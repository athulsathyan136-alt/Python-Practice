import matplotlib.pyplot as plt
import numpy as np

print('='*50)
print('LINE PLOT')
print('='*50)

plt.figure(figsize=(10,6))
days = [1,2,3,4,5,6,7]
study = [2,3,1,4,3,5,6]
marks = [65,70,60,80,75,85,90]

plt.plot(days,study,marker = 'o',label = 'study',color = 'blue')
plt.plot(days,marks,marker = 's',label = 'marks',color = 'green')

plt.title('Study Hours vs Marks Over a week')
plt.xlabel('Days')
plt.ylabel('Values')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('chart1_line.png')
plt.show()

print('='*50)
print('BAR CHART')
print('='*50)

plt.figure(figsize=(10,6))
sub = ["Python", "AI", "Cloud", "SQL", "Docker"]
scores = [95, 88, 82, 90, 78]
colors = ['#FF6F00', '#FF9900', '#FFB300', '#FFC107', '#FFD54F']

bars = plt.bar(sub,scores,color = colors)

for bar ,score in zip(bars,scores):
    plt.text(bar.get_x() + bar.get_width()/2 , bar.get_height() + 1 , str(scores), ha='center',fontweight = 'bold')

plt.title('My Skill Scores')
plt.xlabel("Subject")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.savefig("chart2_bar.png")
plt.show()  

print('='*50)
print('SCATTER PLOT')
print('='*50)

plt.figure(figsize=(10,6))
np.random.seed(42)
x = np.random.randn(50)*10
y = 2 * x + np.random.randn(50) * 2

plt.scatter(x,y , alpha=0.6,color ='red',edgecolors='black')

plt.title("Scatter Plot: X vs Y")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True, alpha=0.3)
plt.savefig("chart3_scatter.png")
plt.show()

print('='*50)
print('SUBPLOT')
print('='*50)

fig,axes = plt.subplots(2,2,figsize= (12,10))

axes[0,0].plot([1,2,3,4,5],[1,4,9,16,25], 'r-o')
axes[0,0].set_title('Squares')

axes[0,1].bar(['A','B','C'],[10,20,15], color ='orange')
axes[0,1].set_title('Bar Chart')

axes[1,0].hist(np.random.randn(1000),bins = 20, color ='teal' ,edgecolor='black')
axes[1,0].set_title('Distribution')

axes[1,1].pie([30,25,20,15,10],labels =['AI', 'ML', 'Cloud', 'Web', 'Other'], autopct= '%1.1f%%')
axes[1,1].set_title('Skills pie Chart')

plt.tight_layout()
plt.savefig('chart4_subplot.png')
plt.show()