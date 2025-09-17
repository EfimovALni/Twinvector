import math

def solve_quadratic(a, b, c):
    """
    Решает квадратное уравнение ax^2 + bx + c = 0.
    Возвращает корни или сообщение, если корней нет.
    """
    if a == 0:
        return "Коэффициент 'a' не должен быть равен нулю"

    d = b**2 - 4*a*c  # дискриминант

    if d < 0:
        return "Нет вещественных корней"
    elif d == 0:
        x = -b / (2*a)
        return f"Один корень: x = {x:.4f}"
    else:
        sqrt_d = math.sqrt(d)
        x1 = (-b + sqrt_d) / (2*a)
        x2 = (-b - sqrt_d) / (2*a)
        return f"Два корня: x1 = {x1:.4f}, x2 = {x2:.4f}"

if __name__ == "__main__":
    print(solve_quadratic(1, -3, 2))
