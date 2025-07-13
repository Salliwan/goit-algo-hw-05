import re

# text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

def generator_numbers(text):
    pattern = r"\b\d+\.\d+|\d+\b"
    numbers = re.findall(pattern, text)
    for number in numbers:
        yield number

def sum_profit(text, func):
    number_sum = 0
    for number in func(text):
        number_sum += float(number)
    return number_sum      

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
