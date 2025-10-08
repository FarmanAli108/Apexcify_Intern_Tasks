
import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(r"D:\vs code\AP_intern_task\student_grades.csv")
df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)
top_student = df.loc[df["Average"].idxmax()]

print("🏆 Student with the highest average:")
print(top_student, "\n")
df_sorted = df.sort_values(by="Average", ascending=False)

top_10 = df_sorted.head(10)
print("📊 Top 10 students by average score:")
print(top_10[["Name", "Average"]])
plt.figure(figsize=(10, 6))
plt.bar(top_10["Name"], top_10["Average"], color='skyblue', edgecolor='black')
plt.title("Top 10 Students by Average Score", fontsize=16)
plt.xlabel("Students", fontsize=12)
plt.ylabel("Average Score", fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
