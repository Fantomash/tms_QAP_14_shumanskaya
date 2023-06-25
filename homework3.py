#1.2 Определить переменные всех типов и выведете их на экран
number = 5
my_name = "Harry"
my_dict = {'animal': "Kangaroo", 'height': 200}
my_list = [1, 2.34, "Kangaroo", None, my_dict]
animal, height = "Kangaroo", 200
my_set = {"Kangaroo", 200, True}
is_paid = True

#1.3 Найти значение выражений
x1 = ((17/2)*3)+2
x2 = 2+((17/2)*3)
x3 = (19%4)+((15/2)*3)
x4 = (15+6)-(10*4)
x5 = ((17/2)%2)*(3**3)
print(x1, x2, x3, x4, x5)

#1.4 Создать три переменные, содержащие возраст трех ближайших соседей, найти сумму и вывести ее на экран.
age1, age2, age3 = 10, 28, 34
age_sum = age1 + age2 + age3
age_average = age_sum/3

print("Сумма: ", age_sum, "Среднее: ", age_average)

#1 Привести к целому типу -1.6, 2.99
a = -1.6
b = 2.99
a = int(a)
b = int(b)
print(a, b)

#2 Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
address = 'www.my_site.com#about'
print(address.replace("#", "/"))

#3 Напишите программу, которая добавляет ‘ing’ к слову ‘stroka’
word = "stroka"
append = "ing"
print(word + append)

#4 В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou"
raw_name = "Ivanou Ivan"
full_name = raw_name.split()
surname = full_name[0]
name = full_name[-1]
print(name, surname)

#5 Напишите программу которая удаляет пробел в начале, в конце строки
text = " Lorem ipsum dolor sit amet "
text1 = text.strip()

#6 Создайте словарь, связав его с переменной school, и наполните его данными которые бы отражали количество учащихся
#в десяти разных классах (например, 1а, 1б, 2б, 6а, 7в и т.д.).
school = {'1B': 10, '2G': 15, '3B': 12, '4C': 23, '5Y': 11, '6D': 9, '7A': 22, '8G': 24, '9E': 18, '10A': 20}

#7 Создайте список и извлеките из него списка второй элемент.
print("Второй элемент списка: ", my_list[1])

#8 Вывести входит ли строка1 в строку2 (пример: employ и employment )
s1, s2 = "employ", "employment"
print(s1 in s2)

# 9 Вывести нужные символы
x = "My name is Agent Smith"
print(x[1]) #y
print(x[3:-5:3]) #nesgt
