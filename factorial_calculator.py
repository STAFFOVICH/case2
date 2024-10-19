import math


def compute_factorial(n):
    """Вычисление факториала числа n."""
    return math.factorial(n)


def main():
    """Основная функция программы."""
    while True:
        user_input = input("Введите положительное целое число от 1 до 1558: ")
        try:
            number = int(user_input)
            if number < 1:
                print("Ошибка: Введите положительное число.")
                continue
            result = compute_factorial(number)
            print(f"Факториал числа {number} равен {result}.")
            break
        except ValueError:
            print("Ошибка: Введите корректное целое число.")


if __name__ == "__main__":
    main()

