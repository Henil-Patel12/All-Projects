def print_pyramid(n):
    for i in range(1, n + 1):
        spaces = n - i
        stars = 2 * i - 1
        print(" " * spaces + "*" * stars)

num_rows = int(input("Enter the number of rows: "))
print_pyramid(num_rows)
