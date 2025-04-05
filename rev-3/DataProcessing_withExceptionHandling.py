def process_data(data, index):

    try:
        int_data = [int(num) for num in data]

        result = int_data[index] / int_data[index - 1]
        return result

    except ZeroDivisionError:
        return "Error: Division by zero occurred."
    except ValueError:
        return "Error: Invalid value encountered during conversion."
    except IndexError:
        return "Error: Index out of bounds."
    except Exception as e:
        return f"Unexpected error: {e}"


# Example Usage:
data_list = ["10", "20", "0", "40"]
print(process_data(data_list, 2))  # Should handle division by zero
print(process_data(["10", "abc", "30"], 1))  # Should handle ValueError
print(process_data([10, 20], 5))  # Should handle IndexError