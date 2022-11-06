import random


def monteCarlo(n):
    straik = 0
    for _ in range(n):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            straik += 1
    return 4.0 * straik / n


num = int(input('Введіть кількість спроб: '))

print(monteCarlo(num))
