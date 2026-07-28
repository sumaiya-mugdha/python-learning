# print pattern

def print_pattern(n):
    for i in range(n // 2, n, 2):
        print(" " * (n - 1 - i), "*" * (2 * i + 1), " " * (2 * (n - i) - 1), "*" * (2 * i + 1), sep="")
    for i in range(n // 2, n, 2):
        print("*" * (4 * n - 1))
    for i in range(0, 2 * n, 2):
        print(" " * (i + 1), "*" * (4 * n - 2 * i - 3), sep="")

    return None

#
# def print_pattern(n):
#     for i in range(n):
#         print("*" * i )
#     return None


print_pattern(29)