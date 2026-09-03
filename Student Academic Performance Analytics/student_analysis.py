import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# Function Name : load_data()
# Description   : Loads CSV dataset into Pandas DataFrame
# Input         : Filename
# Output        : DataFrame
# Author        : Sandeep Sanjay Ghorpade
# ---------------------------------------------------------------

def load_data(filename):
    df = pd.read_csv(filename)

    print("\n------------------------------------------------")
    print("Dataset Loaded Successfully")
    print("------------------------------------------------\n")

    return df

# ---------------------------------------------------------------
# Function Name : display_basic_info()
# Description   : Displays complete dataset information
#                 including shape, columns and null values
# Input         : DataFrame
# Output        : None
# ---------------------------------------------------------------

def display_basic_info(df):

    print("\n================================================")
    print("Complete Dataset")
    print("================================================")
    print(df)

    print("\n================================================")
    print("First 5 Records")
    print("================================================")
    print(df.head())

    print("\n================================================")
    print("Dataset Shape")
    print("================================================")
    print(df.shape)

    print("\n================================================")
    print("Column Names")
    print("================================================")
    print(df.columns)

    print("\n================================================")
    print("Dataset Information")
    print("================================================")
    print(df.info())

    print("\n================================================")
    print("Missing Values")
    print("================================================")
    print(df.isnull().sum())

    print("\n================================================")
    print("Duplicate Records")
    print("================================================")
    print(df.duplicated().sum())

    print("\n================================================")
    print("Statistical Summary")
    print("================================================")

    print(df.describe())


# ---------------------------------------------------------------
# Function Name : clean_data()
# Description   : Cleans and prepares dataset for analysis
# Input         : DataFrame
# Output        : Cleaned DataFrame
# ---------------------------------------------------------------

def clean_data(df):

    print("\n================================================")
    print("Data Cleaning")
    print("================================================")

    print("Missing Values Before Cleaning")
    print(df.isnull().sum())

    print("\nDuplicate Records Before Cleaning")
    print(df.duplicated().sum())

    df["Parent_Education_Level"] = df["Parent_Education_Level"].fillna("Unknown")

    print("\nMissing Values After Cleaning")
    print(df.isnull().sum())

    print("\n================================================")
    print("Data Validation")
    print("================================================")

    print("Age Range")
    print(df["Age"].min(), "to", df["Age"].max())

    print("\nAttendance Range")
    print(df["Attendance (%)"].min(), "to", df["Attendance (%)"].max())

    print("\nFinal Score Range")
    print(df["Final_Score"].min(), "to", df["Final_Score"].max())

    print("\nStress Level Range")
    print(df["Stress_Level (1-10)"].min(), "to", df["Stress_Level (1-10)"].max())

    print("\nSleep Hours Range")
    print(df["Sleep_Hours_per_Night"].min(), "to", df["Sleep_Hours_per_Night"].max())

    print("\nMidterm Score Range")
    print(df["Midterm_Score"].min(), "to", df["Midterm_Score"].max())

    print("\nAssignment Average Range")
    print(df["Assignments_Avg"].min(), "to", df["Assignments_Avg"].max())

    print("\nQuiz Average Range")
    print(df["Quizzes_Avg"].min(), "to", df["Quizzes_Avg"].max())

    print("\nParticipation Score Range")
    print(df["Participation_Score"].min(), "to", df["Participation_Score"].max())

    print("\nProject Score Range")
    print(df["Projects_Score"].min(), "to", df["Projects_Score"].max())

    print("\nTotal Score Range")
    print(df["Total_Score"].min(), "to", df["Total_Score"].max())

    return df

# ---------------------------------------------------------------
# Function Name : sql_like_analysis()
# Description   : Performs SQL-like analytics operations
#                 using Pandas
# Input         : DataFrame
# Output        : None
# ---------------------------------------------------------------

def sql_like_analysis(df):

    print("\n================================================")
    print("Department Wise Student Count")
    print("================================================")
    print(df.groupby("Department")["Student_ID"].count())

    print("\n================================================")
    print("Average Final Score by Department")
    print("================================================")
    print(df.groupby("Department")["Final_Score"].mean())

    print("\n================================================")
    print("Gender Distribution")
    print("================================================")
    print(df.groupby("Gender")["Student_ID"].count())

    print("\n================================================")
    print("Average Attendance by Department")
    print("================================================")
    print(df.groupby("Department")["Attendance (%)"].mean())

    print("\n================================================")
    print("Average Study Hours by Department")
    print("================================================")
    print(df.groupby("Department")["Study_Hours_per_Week"].mean())

    print("\n================================================")
    print("Average Final Score by Study Hours")
    print("================================================")
    df["Study_Hours_Group"] = pd.cut(
        df["Study_Hours_per_Week"],
        bins=[0, 10, 15, 20, 25, 30],
        labels=["Below 10", "10-15", "15-20", "20-25", "25-30"]
    )
    print(df.groupby("Study_Hours_Group", observed=True)["Final_Score"].mean())

    print("\n================================================")
    print("Attendance vs Final Score")
    print("================================================")
    print(df[["Attendance (%)", "Final_Score"]].corr())

    print("\n================================================")
    print("Top 10 Performing Students")
    print("================================================")
    top_students = df.sort_values("Final_Score", ascending=False).head(10)
    print(top_students[
        ["First_Name", "Last_Name", "Department", "Final_Score"]
    ])

    print("\n================================================")
    print("Low Attendance Students")
    print("================================================")
    low_attendance = df[df["Attendance (%)"] < 75]
    print("Total Low Attendance Students:", len(low_attendance))
    print(low_attendance.sort_values("Attendance (%)").head(10)[
        ["First_Name", "Last_Name", "Department", "Attendance (%)"]
    ])

    print("\n================================================")
    print("Highest Final Score")
    print("================================================")
    print(df["Final_Score"].max())

    print("\n================================================")
    print("Lowest Final Score")
    print("================================================")
    print(df["Final_Score"].min())

    print("\n================================================")
    print("Midterm Score vs Final Score")
    print("================================================")
    print(df[["Midterm_Score", "Final_Score"]].corr())

    print("\n================================================")
    print("Average Final Score by Stress Level")
    print("================================================")
    print(df.groupby("Stress_Level (1-10)")["Final_Score"].mean())

    print("\n================================================")
    print("Complete Department Wise Analytics Report")
    print("================================================")

    report = df.groupby("Department").agg(

        Total_Students=("Student_ID", "count"),

        Average_Final_Score=("Final_Score", "mean"),

        Average_Attendance=("Attendance (%)", "mean"),

        Highest_Score=("Final_Score", "max"),

        Lowest_Score=("Final_Score", "min")
    )

    print(report)

# ---------------------------------------------------------------
# Function Name : create_visualizations()
# Description   : Creates multiple visualizations for
#                 analytics and dashboard representation
# Input         : DataFrame
# Output        : Graphical Visualization
# ---------------------------------------------------------------

def create_visualizations(df):

    # -----------------------------------------------------------
    # Department Wise Student Count
    # -----------------------------------------------------------

    department_count = df.groupby("Department")["Student_ID"].count()

    plt.figure(figsize=(8, 5))

    department_count.plot(kind="bar")

    plt.title("Department Wise Student Count")
    plt.xlabel("Department")
    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.show()

    # -----------------------------------------------------------
    # Average Final Score by Department
    # -----------------------------------------------------------

    avg_score = df.groupby("Department")["Final_Score"].mean()

    plt.figure(figsize=(8, 5))

    avg_score.plot(kind="bar")

    plt.title("Average Final Score by Department")

    plt.xlabel("Department")

    plt.ylabel("Average Final Score")

    plt.tight_layout()

    plt.show()

    # -----------------------------------------------------------
    # Gender Distribution
    # -----------------------------------------------------------

    gender_count = df.groupby("Gender")["Student_ID"].count()

    plt.figure(figsize=(7, 7))

    gender_count.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Gender Distribution")
    plt.ylabel("")

    plt.tight_layout()
    plt.show()

    # -----------------------------------------------------------
    # Grade Distribution
    # -----------------------------------------------------------

    grade_count = df.groupby("Grade")["Student_ID"].count()

    plt.figure(figsize=(8, 5))

    grade_count.plot(kind="bar")

    plt.title("Grade Distribution")

    plt.xlabel("Grade")

    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.show()

    # -----------------------------------------------------------
    # Attendance Distribution
    # -----------------------------------------------------------

    attendance = df["Attendance (%)"]

    plt.figure(figsize=(9, 5))

    plt.hist(attendance, bins=10)

    plt.title("Attendance Distribution")

    plt.xlabel("Attendance (%)")

    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.show()

    # -----------------------------------------------------------
    # Average Study Hours by Department
    # -----------------------------------------------------------

    study_hours = df.groupby("Department")["Study_Hours_per_Week"].mean()

    plt.figure(figsize=(8, 5))

    study_hours.plot(kind="bar")

    plt.title("Average Study Hours by Department")

    plt.xlabel("Department")

    plt.ylabel("Average Study Hours per Week")

    plt.tight_layout()

    plt.show()

    # -----------------------------------------------------------
    # Final Score Distribution
    # -----------------------------------------------------------

    plt.figure(figsize=(8, 5))

    plt.hist(df["Final_Score"], bins=10)

    plt.title("Final Score Distribution")

    plt.xlabel("Final Score")

    plt.ylabel("Number of Students")

    plt.tight_layout()

    plt.show()

    # -----------------------------------------------------------
    # Attendance vs Final Score
    # -----------------------------------------------------------

    plt.figure(figsize=(8, 5))

    plt.scatter(df["Attendance (%)"], df["Final_Score"])

    plt.title("Attendance vs Final Score")

    plt.xlabel("Attendance (%)")

    plt.ylabel("Final Score")

    plt.tight_layout()

    plt.show()

    # -----------------------------------------------------------
    # Midterm Score vs Final Score
    # -----------------------------------------------------------

    plt.figure(figsize=(8, 5))

    plt.scatter(df["Midterm_Score"], df["Final_Score"])

    plt.title("Midterm Score vs Final Score")

    plt.xlabel("Midterm Score")

    plt.ylabel("Final Score")

    plt.tight_layout()

    plt.show()

# ---------------------------------------------------------------
# Function Name : main()
# Description   : Entry point function of application
# Input         : None
# Output        : None
# ---------------------------------------------------------------

def main():

    filename = "Students Performance Dataset.csv"

    df = load_data(filename)

    display_basic_info(df)

    df = clean_data(df)

    sql_like_analysis(df)

    create_visualizations(df)

# ---------------------------------------------------------------
# Application Starter
# ---------------------------------------------------------------

if __name__ == "__main__":
    main()