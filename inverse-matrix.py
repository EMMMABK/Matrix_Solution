import numpy as np

def get_matrix_input():
    matrix = []
    print("Введите элементы матрицы построчно (вводите строки через пробел):")
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

def handle_nan_inf(value, prev_value):
    if np.isnan(value) or np.isinf(value):
        return prev_value
    return value

def print_step_by_step(matrix, steps):
    print("Шаги решения:")
    for step in steps:
        print(np.array(step), "\n")

def inverse_matrix(matrix):
    n = len(matrix)
    steps = []

    # Создаем расширенную матрицу (матрица | единичная матрица)
    identity_matrix = np.eye(n)
    aug_matrix = np.hstack((matrix, identity_matrix))
    steps.append(aug_matrix.copy())

    # Прямой ход
    for i in range(n):
        # Делаем главный элемент равным 1
        aug_matrix[i] = aug_matrix[i] / aug_matrix[i][i]
        steps.append(aug_matrix.copy())

        # Делаем нули в остальных строках
        for j in range(n):
            if i != j:
                prev_row = aug_matrix[j].copy()  # Сохраняем предыдущее состояние строки
                aug_matrix[j] = aug_matrix[j] - aug_matrix[i] * aug_matrix[j][i]
                
                # Обрабатываем случаи с nan и inf
                aug_matrix[j] = np.array([handle_nan_inf(aug_matrix[j][k], prev_row[k]) for k in range(n + n)])

                steps.append(aug_matrix.copy())

    # Обратная матрица
    inverse = aug_matrix[:, n:]

    return inverse, steps

# Основная программа
try:
    matrix = get_matrix_input()
    if matrix is not None:
        try:
            inv_matrix, steps = inverse_matrix(matrix)
            print_step_by_step(matrix, steps)
            print("Обратная матрица:")
            print(inv_matrix)
        except ValueError as e:
            print(e)
        except np.linalg.LinAlgError:
            print("Матрица не является обратимой.")
except ValueError:
    print("Ошибка: Введите корректные числовые значения.")
