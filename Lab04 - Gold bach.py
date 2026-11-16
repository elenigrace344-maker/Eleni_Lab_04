def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True


try:
    n = int(input("Enter an even number greater than 2: "))

    if n <= 2 or n % 2 != 0:
        print("Invalid input.")
    else:
        print(f"Goldbach decompositions for {n}:")

        for p in range(2, n // 2 + 1):
            q = n - p

            if is_prime(p) and is_prime(q):
                print(f"{p} + {q}")

except ValueError:
    print("Please enter a valid integer.")