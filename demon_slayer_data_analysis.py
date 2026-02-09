import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("characters.csv")

print(df.head())

print(df.info())
print(df.describe())


average_Age = df["Age"].mean()
print("Average age:", average_Age)
plt.figure(figsize=(14,8))

#Bar graph
plt.subplot(2, 2, 1)
df["Gender"].value_counts().plot(kind="bar")
plt.title("Gender Distribution")
plt.xlabel("Count")
plt.ylabel("Gender")

#Scatter Plot
plt.subplot(2, 2, 2)
plt.scatter(df["Character No."], df["Age"])
plt.title("Character Number vs Age")
plt.xlabel("Character Number")
plt.ylabel("Age")

# Heatmap
plt.subplot(2, 1, 2)
numeric_df = df.select_dtypes(include="number")
correlation = numeric_df.corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()
 
