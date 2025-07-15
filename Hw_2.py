# Імпортуємо модуль
import re  

# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# Функція-генератор, яка знаходить числа у тексті
def generator_numbers(text):

    # Шаблон для пошуку чисел
    pattern = r"\d+\.\d+|\d+"

    # Пошук чисел
    numbers = re.findall(pattern, text) 
    for number in numbers:

        # Повертаємо числа по черзі
        yield number 

# Функція для розрахунку суми чисел 
def sum_profit(text, func):

    # Початкова сума
    number_sum = 0

    # Проходимо по всих числах з генератора
    for number in func(text):

        # Робимо з рядка число і додаєм до суми
        number_sum += float(number)

    # Повертаємо загальний дохід
    return number_sum      

# Викликаємо функцію і передаємо Ій данні
total_income = sum_profit(text, generator_numbers)

# Виводимо загальний дохід
print(f"Загальний дохід: {total_income}")
