import numpy as np

def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def check_result(row, subjects):
    for subject in subjects:
        if row[subject] < 40:
            return "FAIL"

    if row["Attendance"] < 75:
        return "FAIL"

    return "PASS"


def process_student_data(df, subjects):
    df["Total_Marks"] = df[subjects].sum(axis=1)
    df["Average_Marks"] = df["Total_Marks"] / len(subjects)
    df["Grade"] = df["Average_Marks"].apply(assign_grade)
    df["Result"] = df.apply(
        lambda row: check_result(row, subjects), axis=1
    )
    return df


def calculate_class_statistics(df):
    highest = np.max(df["Average_Marks"])
    lowest = np.min(df["Average_Marks"])
    average = np.mean(df["Average_Marks"])
    return highest, lowest, average


def count_results(df):
    passed = (df["Result"] == "PASS").sum()
    failed = (df["Result"] == "FAIL").sum()
    return passed, failed


def subject_analysis(df, subjects):
    averages = {}
    for subject in subjects:
        averages[subject] = np.mean(df[subject])
    return averages


def find_top_performers(df, number=3):
    return df.sort_values(
        by="Average_Marks", ascending=False
    ).head(number)
