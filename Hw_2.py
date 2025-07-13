import re # Імпортуємо модуль 

# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

# Функція-генератор, яка знаходить числа у тексті
def generator_numbers(text): 
    pattern = r"\b\d+\.\d+|\d+\b" # Шаблон для пошуку чисел
    numbers = re.findall(pattern, text) # Пошук чисел
    for number in numbers:
        yield number # Повертаємо числа по черзі

# Функція для розрахунку суми чисел 
def sum_profit(text, func):
    number_sum = 0 # Початкова сума
    for number in func(text): # Проходимо по всих числах з генератора
        number_sum += float(number) # Робимо з рядка число і додаєм до суми
    return number_sum   # Повертаємо загальний дохід   

total_income = sum_profit(text, generator_numbers) # Викликаємо функцію і передаємо Ій данні
print(f"Загальний дохід: {total_income}") # Виводимо загальний дохід
