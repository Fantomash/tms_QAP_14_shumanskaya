# 1 Напишите декоратор, который проверял бы тип параметров
# функции, конвертировал их если надо и складывал:
# @typed(type=’str’)
# def add_two_symbols(a, b):
# return a + b
# add_two_symbols("3", 5) -> "35"
# add_two_symbols(5, 5) -> 55
# add_two_symbols('a', 'b') -> 'ab’
# @typed(type=’int’)
# def add_three_symbols(a, b, с):
# return a + b + с
# add_three_symbols(5, 6, 7) -> 18
# add_three_symbols("3", 5, 0) -> 8
# add_three_symbols(0.1, 0.2, 0.4) -> 0.7000000000000001

def typed(type):
    def decorator(func):
        def wrapper(*args):
            args = (type(arg) for arg in args)
            return func(*args)
        return wrapper
    return decorator

@typed(str)
def add_two_symbols(a, b):
    return a + b

print(add_two_symbols("3", 5))
print(add_two_symbols(5, 5))
print(add_two_symbols('a', 'b'))

@typed(type=int)
def add_three_symbols(a, b, с):
    return a + b + с

print(add_three_symbols(5, 6, 7))
print(add_three_symbols("3", 5, 0))
print(add_three_symbols(0.1, 0.2, 0.4))

# 2 Лексикографическое возрастание
# На вход подаётся некоторое количество (не больше сотни)
# разделённых пробелом целых чисел (каждое не меньше 0 и не
# больше 19). Выведите их через пробел в порядке
# лексикографического возрастания названий этих чисел в
# английском языке.Т.е., скажем числа 1, 2, 3 должны быть
# выведены в порядке 1, 3, 2, поскольку слово two в словаре
# встречается позже слова three, а слово three -- позже слова one
# (иначе говоря, поскольку выражение 'one' < 'three' < 'two'
# является истинным)
# number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5:
# 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12:
# 'twelve',13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17:
# 'seventeen', 18: 'eighteen', 19: 'nineteen'}

number_names = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5:
'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12:
'twelve',13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17:
'seventeen', 18: 'eighteen', 19: 'nineteen'}

input_numbers = input("Введите числа от 0 до 19, разделённые пробелом: ")
numbers = input_numbers.split()
input_names = [number_names[int(num)] for num in numbers]
sorted_numbers = sorted(input_names)
print(sorted_numbers)