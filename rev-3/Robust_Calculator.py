def calculator(a, b, operator):

    try:
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            if b == 0:
                raise ZeroDivisionError("Error: Division by zero is not allowed.")
            return a / b
        elif operator == "%":
            if b == 0:
                raise ZeroDivisionError("Error: Modulo by zero is not allowed.")
            return a % b
        elif operator == "**":
            return a ** b
        else:
            raise ValueError("Error: Unsupported operator. Use +, -, *, /, %, **")

    except ZeroDivisionError as e:
        return str(e)
    except TypeError as e:
        return "Invalid Input"
    except ValueError as e:
        return str(e)
    except Exception as e:
        return f"Error: Unexpected error - {e}"



print(calculator(10, 0, "/"))  # Should return: "Error: Division by zero"
print(calculator(10, "five", "+"))  # Should return: "Error: Invalid input type"
print(calculator(10, 5, "$"))  # Should return: "Error: Unsupported operator"

