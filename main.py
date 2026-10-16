
import pandas as pd
import numpy as np

from functions import (
    process_student_data,
    calculate_class_statistics,
    count_results,
    subject_analysis,
    find_top_performers
)

print("=" * 55)
print(" STUDENT PERFORMANCE ANALYTICS SYSTEM ")
print("=" * 55)

# Step 1: Load dataset
df = pd.read_csv("students.csv")

subjects = [
    "Python",
    "Mathematics",
    "Data_Science",
    "AI",
    "Statistics"
]

# Step 2: Display dataset information
print("\n--- DATASET INFORMATION ---")
print("Total Students:", len(df))
print("Department:", df["Department"].iloc[0])
print("\nStudent Records:")
print(df.to_string(index=False))

# Step 3: Process student data
df = process_student_data(df, subjects)

# Step 4: Display student performance
print("\n--- STUDENT PERFORMANCE ---")
print(
    df[[
        "Student_ID", "Name", "Total_Marks",
        "Average_Marks", "Grade", "Result"
    ]].to_string(index=False)
)

# Step 5: Class performance
highest, lowest, average = calculate_class_statistics(df)

print("\n--- CLASS PERFORMANCE ---")
print(f"Highest Average: {highest:.2f}")
print(f"Lowest Average: {lowest:.2f}")
print(f"Class Average: {average:.2f}")

# Step 6: Pass and fail statistics
passed, failed = count_results(df)

print("\n--- PASS / FAIL STATISTICS ---")
print("Passed Students:", passed)
print("Failed Students:", failed)

# Step 7: Subject-wise analysis
averages = subject_analysis(df, subjects)

print("\n--- SUBJECT-WISE PERFORMANCE ---")
for subject, avg in averages.items():
    print(f"{subject}: {avg:.2f}")

print("\nBest Subject:", max(averages, key=averages.get))
print("Lowest Subject:", min(averages, key=averages.get))

# Step 8: Top three performers
print("\n--- TOP THREE PERFORMERS ---")
top_students = find_top_performers(df, 3)

for _, row in top_students.iterrows():
    print(
        f"{row['Name']} | Average: "
        f"{row['Average_Marks']:.2f} | Grade: {row['Grade']}"
    )

# Step 9: NumPy analysis
all_marks = df[subjects].to_numpy()

print("\n--- NUMPY ANALYSIS ---")
print("Highest Mark:", np.max(all_marks))
print("Lowest Mark:", np.min(all_marks))
print("Overall Marks Average:", round(np.mean(all_marks), 2))

# Step 10: Attendance analysis
print("\n--- ATTENDANCE ANALYSIS ---")
print(f"Average Attendance: {df['Attendance'].mean():.2f}%")

# Step 11: Save final report
df.to_csv("student_performance_report.csv", index=False)

print("\nReport saved: student_performance_report.csv")
print("\nANALYSIS COMPLETED SUCCESSFULLY!")
