import pandas as pd

data = {
    'Student': ['John', 'Sara', 'Mike', 'Anna', 'David', 'Emily', 'Chris', 'Sophia'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Marks': [85, 72, 90, 65, 78, 88, 92, 55],
    'Attendance': [92, 80, 95, 70, 85, 90, 97, 60]
}

df = pd.DataFrame(data)

avg_marks = df.groupby('Subject')['Marks'].mean()
high_marks_low_attendance = df[(df['Marks'] > 85) & (df['Attendance'] < 90)]
df['Grade'] = df['Marks'].apply(lambda x: 'A' if x >= 90 else 'B' if x >= 80 else 'C' if x >= 70 else 'D')
grade_counts = df['Grade'].value_counts()
correlation = df[['Marks', 'Attendance']].corr().iloc[0, 1]

print(avg_marks)
print(high_marks_low_attendance)
print(df)
print(grade_counts)
print(correlation)
