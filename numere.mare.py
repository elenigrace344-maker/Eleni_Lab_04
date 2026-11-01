import os

def add_large_numbers(num1_str, num2_str):
    i = len(num1_str) - 1
    j = len(num2_str) - 1
    carry = 0
    result = []

    while i >= 0 or j >= 0 or carry > 0:
        digit1 = int(num1_str[i]) if i >= 0 else 0
        digit2 = int(num2_str[j]) if j >= 0 else 0

        total = digit1 + digit2 + carry
        carry = total // 10
        result.append(str(total % 10))

        i -= 1
        j -= 1

    return "".join(reversed(result))

def multiply_large_numbers(num1_str, num2_str):
    if num1_str == "0" or num2_str == "0":
        return "0"

    len1, len2 = len(num1_str), len(num2_str)
    result = [0] * (len1 + len2)

    # Multiply each digit from num1 and num2 from right to left
    for i in range(len1 - 1, -1, -1):
        for j in range(len2 - 1, -1, -1):
            digit1 = int(num1_str[i])
            digit2 = int(num2_str[j])

            product = digit1 * digit2
            sum_val = product + result[i + j + 1]

            result[i + j + 1] = sum_val % 10          # Store current digit
            result[i + j] += sum_val // 10             # Add carry to the left position

    # Convert result list to string and strip leading zeros
    result_str = "".join(map(str, result)).lstrip('0')
    return result_str if result_str else "0"

def validate_non_negative_number(s):
    return s.isdigit()

def main():
    filename = "numere.txt"
    
    # Check if file exists
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' does not exist.")
        return

    # Read lines from the file
    with open(filename, "r") as file:
        lines = [line.strip() for line in file.readlines() if line.strip()]

    if len(lines) < 2:
        print("Error: The file must contain at least two numbers, one per line.")
        return

    num1_str = lines[0]
    num2_str = lines[1]

    # Validate inputs and length constraints (at most 200 digits)
    if not validate_non_negative_number(num1_str) or not validate_non_negative_number(num2_str):
        print("Error: Numbers in 'numere.txt' must be valid non-negative integers.")
        return

    if len(num1_str) > 200 or len(num2_str) > 200:
        print("Error: Numbers exceed the maximum length limit of 200 digits.")
        return

    # Perform operations
    sum_result = add_large_numbers(num1_str, num2_str)
    product_result = multiply_large_numbers(num1_str, num2_str)

    # Display results
    print(f"Number 1: {num1_str}")
    print(f"Number 2: {num2_str}")
    print("-" * 40)
    print(f"Sum      : {sum_result}")
    print(f"Product  : {product_result}")

if __name__ == "__main__":
    main()