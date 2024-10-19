import numpy as np

# Запрос размеров матрицы
n = int(input("Введите количество строк (n): "))
m = int(input("Введите количество столбцов (m): "))

# Проверка корректности размера матрицы
if m < 1 or n < 1 or m < 2:
    print("Ошибка: количество столбцов должно быть не меньше 2.")
    exit()

# Вывод формулы на основе n и m
equations = []
for i in range(n):
    equation = " + ".join([f"a{i + 1}{j + 1}x{j + 1}" for j in range(m - 1)]) + f" = b{i + 1}"
    equations.append(equation)

print("\nФормула:")
for eq in equations:
    print(eq)

# Запрос коэффициентов
coefficients = []
for i in range(n):
    while True:
        user_input = input(f"Введите a11, a12, ..., a1{m-1}, b{i + 1} (через пробел): ")
        values = list(map(float, user_input.split()))
        
        # Проверка на количество введенных значений
        if len(values) != m:
            print(f"Ошибка: ожидалось {m} значений, но получено {len(values)}. Попробуйте снова.")
        else:
            coefficients.append(values)
            break  # Выход из цикла, если ввод корректен

# Вывод уравнений
print("\nУравнения:")
for i in range(n):
    equation = " + ".join([f"{int(coefficients[i][j])}x{j + 1}" for j in range(m - 1)]) + f" = {int(coefficients[i][-1])}"
    print(equation)

# Вывод матрицы
print("\nМатрица:")
for i in range(n):
    row = " ".join([str(int(coefficients[i][j])) for j in range(m)])  # Преобразуем коэффициенты в строки
    print(f"[{row}]")

# Функция для решения системы уравнений методом Гаусса
def gauss_elimination(coefficients):
    # Преобразуем данные в массив numpy
    A = np.array(coefficients)  # Вся матрица, включая свободные члены
    n, m = A.shape

    # Проверка соответствия размера матрицы
    if m != n + 1:
        print(f"Ошибка: матрица должна быть размером {n} x {n+1} для выполнения метода Гаусса.")
        print(f"Текущий размер матрицы: {n} x {m}")
        print("Рекомендуется использовать другой метод, например, параметрический метод, для решения этой системы.")
        return None

    # Прямой ход метода Гаусса
    for i in range(n):
        # Находим главный элемент
        max_row_index = np.argmax(np.abs(A[i:, i])) + i
        A[[i, max_row_index]] = A[[max_row_index, i]]  # Меняем строки

        # Проверка на деление на ноль
        if np.isclose(A[i, i], 0):  # Проверка на ноль
            if np.all(A[i] == 0):  # Если вся строка нулевая
                print("Ошибка: система имеет бесконечно много решений или несовместна.")
                continue  # Пропустить дальнейшие действия с этой строкой
            else:
                print("Ошибка: деление на ноль. Система уравнений может быть вырождена.")
                continue  # Пропустить дальнейшие действия с этой строкой

        # Приводим к треугольному виду
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j] -= factor * A[i]

        # Округление значений для вывода
        A = np.round(A, decimals=2)

        # Вывод промежуточной матрицы
        print(f"\nПосле преобразования строки {i + 1}:")
        print("Матрица A:")
        for row in A:
            print("[" + " ".join(map(lambda x: f"{int(x)}" if x.is_integer() else f"{x:.2f}", row)) + "]")

    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if np.isclose(A[i, i], 0):  # Проверка на ноль
            if np.isclose(A[i, -1], 0):
                print("Ошибка: система имеет бесконечно много решений.")
                return None
            else:
                print("Ошибка: система несовместна.")
                return None

        # Вычисление значения x[i] с учетом всех известных решений
        sum_ax = np.dot(A[i, i + 1:n], x[i + 1:n])
        x[i] = (A[i, -1] - sum_ax) / A[i, i]

    return x


    # Обратный ход
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        if np.isclose(A[i, i], 0):  # Проверка на ноль
            if np.isclose(A[i, -1], 0):
                print("Ошибка: система имеет бесконечно много решений.")
                return None
            else:
                print("Ошибка: система несовместна.")
                return None

        if i == n - 1:
            x[i] = A[i, -1] / A[i, i]
        else:
            x[i] = (A[i, -1] - np.dot(A[i, i + 1:], x[i + 1:])) / A[i, i]


    return x

# Решение системы
solution = gauss_elimination(coefficients)

# Вывод решения
if solution is not None:
    print("\nРешение системы:")
    for i in range(len(solution)):
        print(f"x{i + 1} = {int(solution[i]) if solution[i].is_integer() else f'{solution[i]:.2f}'}")  # Преобразуем в int для вывода
