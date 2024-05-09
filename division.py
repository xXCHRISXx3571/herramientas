def divide(num_1, num_2):
    if num_2 != 0:
        result = num_1 / num_2
        print(f'{num_1} / {num_2} is equal to {result}')
        return result
    else:
        print("Error: Division by zero is not allowed.")
        return None