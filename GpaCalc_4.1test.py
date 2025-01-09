import pandas as pd


# Function to convert score to GPA points
def gpa(num):
    if num >= 70:
        return 5
    elif 60 <= num < 70:
        return 4
    elif 50 <= num < 60:
        return 3
    elif 45 <= num < 50:
        return 2
    elif 40 <= num < 45:
        return 1
    else:
        return 0


# Function to categorize the GPA
def gpa_stats(var):
    if var >= 4.5:
        return f'{var:.2f} - First Class'
    elif 3.5 <= var < 4.5:
        return f'{var:.2f} - Second Class Upper'
    elif 2.5 <= var < 3.5:
        return f'{var:.2f} - Second Class Lower'
    elif 1.5 <= var < 2.5:
        return f'{var:.2f} - Third Class'
    elif 0.5 <= var < 1.5:
        return f'{var:.2f} - Probation'
    else:
        return f'{var:.2f} - Probation 2'


# Load course units from CourseUnit.csv
course_units_filepath = 'data/CourseUnit.csv'
course_units_df = pd.read_csv(course_units_filepath)
course_units = dict(zip(course_units_df['Course'], course_units_df['Unit']))

# Load student data from StudentScore.csv
student_scores_filepath = 'data/StudentScore.csv'
student_scores_df = pd.read_csv(student_scores_filepath)

# Calculate GPA for each student
gpa_results = []
for index, row in student_scores_df.iterrows():
    total_units = 0
    total_points = 0
    for course, unit in course_units.items():
        if course in row:
            score = row[course]
            grade = gpa(score)
            total_units += unit
            total_points += grade * unit
    gpa_value = total_points / total_units if total_units != 0 else 0
    gpa_results.append(gpa_value)

# Add GPA results to the DataFrame
student_scores_df['GPA'] = gpa_results

# Save the updated DataFrame to CSV
student_scores_df.to_csv(student_scores_filepath, index=False)
print("GPA results saved to data/StudentScore.csv")

# Print results
for index, row in student_scores_df.iterrows():
    print(f"Student: {row['StudentName']}, GPA: {row['GPA']:.2f}, Category: {gpa_stats(row['GPA'])}")