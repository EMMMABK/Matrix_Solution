import numpy as np

def input_matrix(n, m):
    print(f"Введите матрицу ({n} строк и {m} столбцов):")
    matrix = []
    for _ in range(n):
        row = list(map(float, input().strip().split()))
        if len(row) != m:
            raise ValueError("Неправильное количество значений в строке.")
        matrix.append(row)
    return np.array(matrix)

def print_matrix(matrix, n, m):
    for i in range(n):
        row = " ".join(f"{matrix[i][j]:10.2f}" for j in range(m))
        print(row)

def gauss_elimination(A, n, m):
    # Прямой ход метода Гаусса
    for i in range(n):
        # Находим главный элемент
        max_row = i
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[max_row][i]):
                max_row = k
        A[i], A[max_row] = A[max_row], A[i]  # Меняем строки

        # Проверка на деление на ноль
        if abs(A[i][i]) < 1e-10:
            continue  # Пропускаем нулевую строку

        # Приведение к треугольному виду
        for k in range(i + 1, n):
            factor = A[k][i] / A[i][i]
            for j in range(i, m):
                A[k][j] -= factor * A[i][j]

    # Проверка на наличие решений
    infinite_solutions = False
    for i in range(n):
        if all(abs(A[i][j]) < 1e-10 for j in range(m - 1)):
            if abs(A[i][m - 1]) > 1e-10:
                print("Система не имеет решений.\n")
                return None
            else:
                infinite_solutions = True

    # Запрашиваем значение x2 (или другой переменной)
    x2_value = float(input("Введите значение x2: "))
    x = [0] * n
    is_free_variable = [False] * n

    for i in range(n - 1, -1, -1):
        if i == 1:  # Если i == 1, это x2
            x[i] = x2_value
        elif abs(A[i][i]) > 1e-10:
            x[i] = (A[i][m - 1] - sum(A[i][j] * x[j] for j in range(i + 1, n))) / A[i][i]
            for j in range(i - 1, -1, -1):
                A[j][m - 1] -= A[j][i] * x[i]
        else:
            x[i] = 0
            is_free_variable[i] = True

    if infinite_solutions:
        print("\nСистема имеет бесконечное количество решений. Одно из решений:\n")
        for i in range(len(x)):
            if is_free_variable[i]:
                print(f"x{i + 1} = любое значение (присвоено 0)\n")
            else:
                print(f"x{i + 1} = {x[i]:.2f}\n")
    else:
        print("\nСистема имеет одно решение:\n")
        for i in range(len(x)):
            print(f"x{i + 1} = {x[i]:.2f}\n")

    return x

def calculate_inverse(matrix):
    n = matrix.shape[0]
    identity = np.eye(n)
    aug = np.hstack((matrix, identity))

    for i in range(n):
        pivot = aug[i, i]
        if abs(pivot) < 1e-10:
            raise ValueError("Матрица не является обратимой.")

        aug[i] /= pivot

        for j in range(n):
            if j != i:
                aug[j] -= aug[i] * aug[j, i]

        print(f"Шаг {i + 1}:")
        print_matrix(aug, n, n * 2)

    return aug[:, n:]

def main():
    while True:
        print("\nВыберите действие:")
        print("1. Решить систему уравнений")
        print("2. Найти обратную матрицу")
        print("3. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            n = int(input("Введите количество строк: "))
            m = int(input("Введите количество столбцов: "))

            if m < 2 or n < 1:
                print("Ошибка: количество столбцов должно быть не меньше 2.")
                continue

            A = input_matrix(n, m)
            print("\nВведенная матрица:")
            print_matrix(A, n, m)

            solution = gauss_elimination(A, n, m)
            if solution is not None:
                print("\nРешение системы:")
                for i, val in enumerate(solution):
                    print(f"x{i + 1} = {val:.2f}")

        elif choice == "2":
            n = int(input("Введите размер матрицы: "))

            if n <= 0:
                print("Ошибка: размер матрицы должен быть положительным.")
                continue

            matrix = input_matrix(n, n)
            print("\nВведенная матрица:")
            print_matrix(matrix, n, n)

            try:
                inverse = calculate_inverse(matrix)
                print("\nОбратная матрица:")
                print_matrix(inverse, n, n)
            except ValueError as e:
                print(e)

        elif choice == "3":
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
