def is_prime(num):
    if num < 2:
        return False
    if num in (2, 3):
        return True
    if num % 2 == 0:
        return False

    i = 3
    while i * i <= num:
        if num % i == 0:
            return False
        i += 2
    return True


def find_goldbach_decompositions(n):
    print(f"\nDecompositions for n = {n}:")
    found = False

    for p in range(2, n // 2 + 1):
        if is_prime(p):
            q = n - p
            if is_prime(q):
                print(f"{n} = {p} + {q}")
                found = True

    if not found:
        print("No decompositions found.")


def main():
    user_input = input("Enter an even natural number greater than 2: ").strip()

    try:
        n = int(user_input)
        if n <= 2 or n % 2 != 0:
            print("Error: Please enter a valid *even* natural number strictly greater than 2.")
            return
    except ValueError:
        print("Error: Invalid input. Please enter an integer number.")
        return

    find_goldbach_decompositions(n)


if __name__ == "__main__":
    main()
