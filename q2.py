
result = 0


def calculate_sum(n):
    global result


    if n == 0:
        return

    calculate_sum(n - 1)
    term = (-1) ** (n - 1) * (n - 1)
    result += term
