def salaryadjustment(employees):
    def adjust_salary(employee):
        if employee["rating"] >= 4:
            new_salary = round(employee["salary"] * 1.10)
        elif employee["rating"] == 3:
            new_salary = round(employee["salary"] * 1.05)
        else:
            new_salary = round(employee["salary"] * 0.70)
        return (employee["name"], new_salary)

    revised_salaries = dict(map(adjust_salary, employees))

    print(revised_salaries)


employees = [
    {"name": "Alice", "salary": 50000, "rating": 5},
    {"name": "Bob", "salary": 40000, "rating": 3},
    {"name": "Charlie", "salary": 35000, "rating": 2}
]

salaryadjustment(employees)


