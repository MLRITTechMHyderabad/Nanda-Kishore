import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank', 'Grace', 'Hannah'],
    'Department': ['HR', 'IT', 'IT', 'HR', 'Finance', 'Finance', 'IT', 'HR'],
    'Age': [25, 32, 29, 41, 37, 45, 26, 38],
    'Salary': [50000, 70000, 65000, 80000, 75000, 90000, 62000, 85000],
    'Experience': [2, 7, 5, 15, 10, 20, 3, 12]
}

df = pd.DataFrame(data)
avg_salary = df.groupby('Department')['Salary'].mean()
print("Average salary by department:")
print(avg_salary)
highest_paid = df.loc[df.groupby('Department')['Salary'].idxmax()]
print("\nHighest-paid employee by department:")
print(highest_paid[['Department', 'Employee', 'Salary']])
filtered_employees = df[(df['Experience'] > 5) & (df['Salary'] > 65000)]
print("\nNumber of employees with >5 years experience and salary >65,000:", len(filtered_employees))

def determine_seniority(exp):
    if exp < 5:
        return "Junior"
    elif 5 <= exp <= 10:
        return "Mid-Level"
    else:
        return "Senior"

df['Seniority'] = df['Experience'].apply(determine_seniority)
print("\nDataFrame with 'Seniority' column added:")
print(df)
sorted_it = df[df['Department'] == 'IT'].sort_values(by='Salary', ascending=False)
print("\nIT department employees sorted by salary in descending order:")
print(sorted_it)