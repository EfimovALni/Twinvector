import math

def solve_quadratic(a, b, c):
    d = b**2 - 4*a*c  # дискриминант

    if d < 0:
        return "Нет вещественных корней"
    elif d == 0:
        x = -b / (2*a)
        return f"Один корень: x = {x}"
    else:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return f"Два корня: x1 = {x1}, x2 = {x2}"

if __name__ == "__main__":
    # пример: уравнение x² - 3x + 2 = 0
    print(solve_quadratic(1, -3, 2))
