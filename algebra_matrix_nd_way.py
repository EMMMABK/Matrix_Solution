class MatrixApp:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.coefficients = []

    def create_matrix(self):
        try:
            self.n = int(input("Введите количество строк (n): "))
            self.m = int(input("Введите количество столбцов (m): "))

            if self.m < 2 or self.n < 1:
                print("Ошибка: количество столбцов должно быть не меньше 2.")
                return

            equations = ["Формула:"]
            for i in range(self.n):
                equation = ' + '.join(f'a{i + 1}{j + 1} * x{j + 1}' for j in range(self.m - 1))
                equations.append(f"{equation} = b{i + 1}")
            print("\n".join(equations))

        except ValueError:
            print("Ошибка: Введите корректные числовые значения.")

    def solve_matrix(self):
        if self.n == 0 or self.m == 0:
            print("Сначала создайте матрицу.")
            return

        print("Введите коэффициенты матрицы:")
        self.coefficients = []
        for i in range(self.n):
            line = input(f"Строка {i + 1}: ").strip().split()
            if len(line) != self.m:
                print(f"Ошибка: неправильное количество значений в строке {i + 1}")
                return
            self.coefficients.append([float(x) for x in line])

        print("\nВведенная матрица:")
        self.print_matrix()

        solution = self.gauss_elimination()
        if solution is not None:
            print("\nРешение системы:")
            for i, sol in enumerate(solution):
                print(f"x{i + 1} = {sol}")

    def print_matrix(self):
        for row in self.coefficients:
            print(" ".join(f"{val:.2f}" for val in row))

    def gauss_elimination(self):
        A = [row[:] for row in self.coefficients]
        n = self.n
        m = self.m

        for i in range(n):
            max_row = max(range(i, n), key=lambda k: abs(A[k][i]))
            A[i], A[max_row] = A[max_row], A[i]

            if abs(A[i][i]) < 1e-10:
                continue

            for k in range(i + 1, n):
                factor = A[k][i] / A[i][i]
                for j in range(i, m):
                    A[k][j] -= factor * A[i][j]

            print(f"\nПосле преобразования строки {i + 1}:")
            self.print_matrix()

        # Проверка на бесконечные решения и свободные переменные
        infinite_solutions = False
        free_vars = []
        dependent_vars = []
        
        for i in range(n):
            if all(abs(A[i][j]) < 1e-10 for j in range(m - 1)):
                if abs(A[i][m - 1]) > 1e-10:
                    print("Система не имеет решений.")
                    return None
                infinite_solutions = True
            elif abs(A[i][i]) < 1e-10:
                free_vars.append(i)  # Запоминаем свободные переменные
            else:
                dependent_vars.append(i)  # Запоминаем зависимые переменные

        x = [0] * (m - 1)
        for i in range(n - 1, -1, -1):
            if abs(A[i][i]) > 1e-10:
                x[i] = A[i][m - 1] / A[i][i]
                for j in range(i):
                    A[j][m - 1] -= A[j][i] * x[i]

        if infinite_solutions:
            print("\nСистема имеет бесконечное количество решений.")
            # Выводим одно из решений
            print("Одно из решений:")
            for i in range(m - 1):
                if i in free_vars:
                    print(f"x{i + 1} = свободная переменная")
                else:
                    print(f"x{i + 1} = {x[i]}")

            # Упрощаем вывод для свободных переменных
            print("\nНекоторые возможные решения:")
            for free_var in free_vars:
                for value in range(-1, 2):  # Задаем диапазон для свободной переменной
                    temp_solution = x[:]
                    temp_solution[free_var] = value  # Меняем свободную переменную
                    for dep_var in dependent_vars:
                        temp_solution[dep_var] = A[dep_var][m - 1] / A[dep_var][dep_var]
                    print(f"При x{free_var + 1} = {value}: " + ", ".join(f"x{i + 1} = {temp_solution[i]:.2f}" for i in range(m - 1)))
        else:
            print("\nСистема имеет одно решение:")
            for i in range(m - 1):
                print(f"x{i + 1} = {x[i]}")

        return x


if __name__ == "__main__":
    app = MatrixApp()
    while True:
        command = input("\nВведите 'create' для создания матрицы, 'solve' для решения, 'exit' для выхода: ").strip().lower()
        if command == 'create':
            app.create_matrix()
        elif command == 'solve':
            app.solve_matrix()
        elif command == 'exit':
            break
        else:
            print("Неизвестная команда.")
