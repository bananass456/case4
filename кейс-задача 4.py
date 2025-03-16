import random

def guess_the_number():
    # Загадать случайное число от 1 до 100
    number_to_guess = random.randint(1, 100)
    
    # Максимальное количество попыток
    attempts = 10
    
    print("Добро пожаловать в игру 'Угадай число'!")
    print(f"Я загадал число от 1 до 100. У тебя есть {attempts} попыток, чтобы угадать.")
    
    while attempts > 0:
        # Запрашиваем у пользователя его предположение
        guess = input("Введите ваше предположение: ")
        
        # Проверка, является ли ввод числом
        try:
            guess = int(guess)
        except ValueError:
            print("Пожалуйста, введите целое число.")
            continue
        
        # Проверка диапазона
        if guess < 1 or guess > 100:
            print("Число должно быть от 1 до 100. Попробуйте снова.")
            continue
        
        # Проверка, угадал ли пользователь
        if guess < number_to_guess:
            print("Загаданное число больше!")
        elif guess > number_to_guess:
            print("Загаданное число меньше!")
        else:
            print(f"Поздравляю! Ты угадал число {number_to_guess}!")
            break
        
        # Уменьшаем количество оставшихся попыток
        attempts -= 1
        
        if attempts > 0:
            print(f"У тебя осталось {attempts} попыток.")
        else:
            print(f"Ты не угадал число. Загаданное число было {number_to_guess}.")
            break

# Запуск игры
guess_the_number()
