def CustomerDiscount(customers):
    filtered_customers = list(filter(lambda customer: customer["age"] <= 40, customers))
    def adjust_discount(customer):
        if 18 <= customer["age"] <= 25:
            discounted_price = round(customer["total_purchase"] * 0.90)
        elif 26 <= customer["age"] <= 40:
            discounted_price = round(customer["total_purchase"] * 0.95)
        else:
            return customer

        return {"name": customer["name"], "age": customer["age"], "total_purchase": discounted_price}

    revised_customers = list(map(adjust_discount, filtered_customers))

    print(revised_customers)

customers = [
    {"name": "Emma", "age": 22, "total_purchase": 150.0},
    {"name": "John", "age": 30, "total_purchase": 200.0},
    {"name": "Grace", "age": 45, "total_purchase": 180.0}
]

CustomerDiscount(customers)
