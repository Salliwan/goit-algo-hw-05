def caching_fibonacci():

    # Створюємо словник для кешування
    cashe = {}

    def fibonacci(n):

        # Якщо n менше або дорівнює 0, повертаємо 0
        if n <= 0:
            return 0
        
        # Якщо n дорівнює 1, повертаємо 1
        if n == 1:
            return 1
        
        # Якщо значення для n є у кеші, повертаємо його
        if n in cashe:
            return cashe[n]

        # Обчислюємо та додаємо до кешу
        cashe[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cashe[n]

    # Повертаємо внутрішню функцію fibonacci
    return fibonacci

# Створюємо об'єкт fib, який є функцією Фібоначчі
fib = caching_fibonacci()

