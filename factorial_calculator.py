import math


def compute_factorial(n):
    """Вычисление факториала числа n."""
    return math.factorial(n)


def main():
    """Основная функция программы."""
    while True:
        """Т.к. тип данных int() не вмещает в себя число фактариала более 1558, пишем про диапозон чисел."""
        user_input = input("Введите положительное целое число от 1 до 1558: ")
        try:
            number = int(user_input)
            if number > 1558:
                print("Ошибка: Введенное число больше, чем 1558.")
                continue
            elif number < 1:
                print("Ошибка: Введите положительное число.")
                continue
            result = compute_factorial(number)
            print(f"Факториал числа {number} равен {result}.")
            break
        except ValueError:
            print("Ошибка: Введите корректное целое число.")


if __name__ == "__main__":
    main()
