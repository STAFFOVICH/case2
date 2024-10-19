import random


def guess_number():
    # Выбираем случайное число от 1 до 100
    number = random.randint(1, 100)

    print("Я загадал число от 1 до 100 за 6 попыток. ")

    for _ in range(6):  # Разрешаем пользователю сделать 6 попыток
        guess = int(input("Попробуйте угадать число: "))

        if guess == number:
            print("Вы угадали число!")
            break
        elif guess < number:
            print("Слишком маленькое число.")
        else:
            print("Слишком большое число.")
    else:
        print("Вы использовали все попытки. Число было", number)


guess_number()
