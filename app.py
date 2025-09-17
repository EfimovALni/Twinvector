import math

class Cell18650:
    def __init__(self, name, voltage, capacity, max_current, resistance):
        self.name = name
        self.v = voltage         # номинальное напряжение (В)
        self.ah = capacity       # ёмкость одной ячейки (А·ч)
        self.i_max = max_current # макс. ток одной ячейки (А)
        self.r = resistance      # внутреннее сопротивление (Ом)

# Типы ячеек 18650 по назначению
TYPES = {
    "1": Cell18650("Panasonic NCR18650B (energy)", 3.6, 3.2, 6.5, 0.045),
    "2": Cell18650("Samsung 25R (power)", 3.6, 2.5, 20.0, 0.022),
    "3": Cell18650("LG HG2 (balanced)", 3.6, 3.0, 15.0, 0.030)
}

def ask_float(prompt):
    while True:
        try:
            value = input(prompt).replace(',', '.')
            return float(value)
        except ValueError:
            print("❌ Введите число!")

def select_cell():
    print("\nВыберите тип 18650 ячейки:")
    for key, cell in TYPES.items():
        print(f"  {key}) {cell.name}: {cell.v}В, {cell.ah}А·ч, {cell.i_max}А, {cell.r*1000:.0f} мОм")
    while True:
        choice = input("Ваш выбор (1/2/3): ")
        if choice in TYPES:
            return TYPES[choice]
        print("❌ Неверный выбор!")

def calculate_config(target_v, min_i, cell):
    print("\n📊 Расчёт...")

    # шаг 1: минимальное S
    s = math.ceil(target_v / cell.v)
    print(f"🔹 Минимальное число ячеек в серии (S): ceil({target_v} / {cell.v}) = {s}")

    # шаг 2: минимальное P по току
    p = math.ceil(min_i / cell.i_max)
    print(f"🔹 Минимальное число параллельных (P): ceil({min_i} / {cell.i_max}) = {p}")

    # шаг 3: проверка просадки напряжения
    r_total = s * (cell.r / p)
    v_nom = s * cell.v
    v_load = v_nom - min_i * r_total
    print(f"🔹 Номинальное напряжение батареи: {s} * {cell.v} = {v_nom:.2f} В")
    print(f"🔹 Сопротивление пакета: R = {s} * ({cell.r:.3f} / {p}) = {r_total:.4f} Ом")
    print(f"🔹 Просадка при {min_i} А: {min_i} * {r_total:.4f} = {min_i * r_total:.2f} В")
    print(f"🔹 Напряжение под нагрузкой: {v_nom:.2f} - просадка = {v_load:.2f} В")

    if v_load < target_v:
        print("⚠️ Просадка слишком большая, увеличим S или P...")
        while v_load < target_v:
            p += 1
            r_total = s * (cell.r / p)
            v_load = v_nom - min_i * r_total
        print(f"✅ Новое P = {p} → напряжение под нагрузкой = {v_load:.2f} В")

    total_cells = s * p
    pack_capacity = p * cell.ah
    pack_energy = pack_capacity * v_nom
    print("\n✅ Результат:")
    print(f"  Рекомендуемая конфигурация: {s}S{p}P")
    print(f"  Всего ячеек: {total_cells}")
    print(f"  Ёмкость: {pack_capacity:.2f} А·ч")
    print(f"  Энергия: ≈ {pack_energy:.1f} Вт·ч")
    print(f"  Допустимый ток: {p} * {cell.i_max} = {p * cell.i_max:.1f} А")

def main():
    print("=== 🔋 Подбор аккумулятора 18650 (SxP) ===")
    target_v = ask_float("Введите требуемое напряжение, В: ")
    min_i = ask_float("Введите требуемый ток нагрузки, А: ")
    cell = select_cell()
    calculate_config(target_v, min_i, cell)

if __name__ == "__main__":
    main()
