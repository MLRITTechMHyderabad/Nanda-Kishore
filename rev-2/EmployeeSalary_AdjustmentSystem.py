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


def CustomerDiscount(customers):
    # Filter customers eligible for a discount
    filtered_customers = list(filter(lambda customer: customer["age"] <= 40, customers))

    # Function to apply the discount
    def adjust_discount(customer):
        if 18 <= customer["age"] <= 25:
            discounted_price = round(customer["total_purchase"] * 0.90, 2)  # 10% discount
        elif 26 <= customer["age"] <= 40:
            discounted_price = round(customer["total_purchase"] * 0.95, 2)  # 5% discount
        else:
            return customer  # Return unchanged if no discount

        return {"name": customer["name"], "age": customer["age"], "total_purchase": discounted_price}

    # Apply discounts using map
    revised_customers = list(map(adjust_discount, filtered_customers))

    print(revised_customers)


# Sample Input
customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

# Function Call
CustomerDiscount(customers)



