import numpy as np

def get_matrix_input():
    matrix = []
    print("Введите элементы матрицы коэффициентов построчно (вводите строки через пробел):")
    print("Когда закончите ввод матрицы, просто нажмите Enter.")
    while True:
        row = input(f"Введите строку {len(matrix) + 1} (или нажмите Enter для завершения ввода): ")
        if not row:
            break
        row = list(map(float, row.split()))
        matrix.append(row)
    
    # Проверка на квадратную матрицу
    if len(matrix) > 0 and all(len(row) == len(matrix) for row in matrix):
        return np.array(matrix)
    else:
        print("Ошибка: Матрица должна быть квадратной (одинаковое количество строк и столбцов).")
        return None

def get_rhs_input(n):
    print("Введите элементы правой части (свободные члены) через пробел:")
    rhs = list(map(float, input().split()))
    if len(rhs) != n:
        print(f"Ошибка: Должно быть {n} свободных членов.")
        return None
    return np.array(rhs)

def cramer_rule(matrix, rhs):
    n = len(matrix)
    det_A = np.linalg.det(matrix)  # Основной определитель матрицы

    if det_A == 0:
        raise ValueError("Определитель основной матрицы равен 0, система не имеет уникальных решений.")

    # Массив для хранения решений
    solutions = []

    # Проходим по каждому столбцу и заменяем его на вектор правых частей
    for i in range(n):
        matrix_copy = matrix.copy()
        matrix_copy[:, i] = rhs  # Заменяем i-й столбец на свободные члены
        det_A_i = np.linalg.det(matrix_copy)  # Определитель новой матрицы
        x_i = det_A_i / det_A  # Находим решение для x_i
        solutions.append(x_i)

    return solutions

# Основная программа
try:
    matrix = get_matrix_input()
    if matrix is not None:
        n = len(matrix)
        rhs = get_rhs_input(n)
        if rhs is not None:
            try:
                solutions = cramer_rule(matrix, rhs)
                print("Решения системы:")
                for i, sol in enumerate(solutions, 1):
                    print(f"x_{i} = {sol}")
            except ValueError as e:
                print(e)
except ValueError:
    print("Ошибка: Введите корректные числовые значения.")
