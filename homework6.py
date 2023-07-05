import random
import string

# 1 Дан файл целых чисел, содержащий не менее четырех элементов.
# Вывести первый, второй, предпоследний и последний элементы данного
# файла. Если чисел меньше 3 выводить ошибку

nums_1 = [random.randint(0, 500) for _ in range(10)]
with open('nums.txt', 'w') as f:
    f.write(str(nums_1))

int_list = [int(x) for x in nums_1]
if len(int_list) < 3:
    print("The file is too short")
else:
    print(int_list[0])
    print(int_list[1])
    print(int_list[-2])
print("---The end of exercise #1---" + '\n')


# 2 Дан файл целых чисел. Создать два новых файла, первый из которых
# содержит четные числа из исходного файла, а второй — нечетные (в том
# же порядке). Если четные или нечетные числа в исходном файле
# отсутствуют, то соответствующий результирующий файл оставить
# пустым.

f_even = open('even_numbers.txt', 'w')  # файл для чётных чисел
f_odd = open('odd_numbers.txt', 'w')  # файл для нечётных чисел
nums_2 = [random.randint(0, 500) for _ in range(30)]

with open('nums2.txt', 'w') as f:
    f.write(str(nums_2))

int_list_2 = [int(x) for x in nums_2]
for i in int_list_2:
    if i%2 == 0:
        f_even = open('even_numbers.txt', 'a')
        f_even.write(str(i) + '\n')
    elif i%2 != 0:
        f_odd = open('odd_numbers.txt', 'a')
        f_odd.write(str(i) + '\n')

f1 = open('even_numbers.txt')
print("The even numbers: " + '\n' + f1.read())
f2 = open('odd_numbers.txt')
print("The odd numbers: " + '\n' + f2.read())
f_even.close()
f_odd.close()
print("---The end of exercise #2---" + '\n')


# 3 Дан файл вещественных чисел. Заменить в нем все элементы на их квадраты.

nums_3 = [random.uniform(0, 500) for _ in range(3)]

with open('float_nums.txt', 'w') as f3:
    f3.write(str(nums_3))

f3 = open('float_nums.txt', 'r')
data = list(map(float, nums_3))
data_square = [num ** 2 for num in data]
# print("Nums are ", data)
# print("Modified nums are ", data_square)
with open('float_nums.txt', 'w') as f3:
    for num in data_square:
        f3.write(str(num) + '\n')
f3 = open('float_nums.txt')
print(f3.read())
f3.close()
print("---The end of exercise #3---" + '\n')


# 4 Даны два файла произвольного типа. Поменять местами их
# содержимое. Файлы должны быть бинарного типа

f4_1 = open('first.bin', 'wb')
f4_2 = open('second.bin', 'wb')
temp_file = open('temp.bin', 'wb')

nums_4 = [1, 5, 17, 234, 99]
random_line = ''.join(random.choices(string.ascii_letters + string.digits, k = 15))
arr1, arr2 = bytearray(nums_4), bytearray(random_line, 'utf-8')
f4_1.write(arr1)
f4_2.write(arr2)
f4_1.close()
f4_2.close()

f4_1 = open('first.bin', 'rb')
temp_file = open('temp.bin', 'wb')
temp_file.write(f4_1.read())
f4_1.close()
temp_file.close()

f4_2 = open('second.bin', 'rb')
f4_1 = open('first.bin', 'wb')
f4_1.write(f4_2.read())
f4_2.close()
f4_1.close()

with open('temp.bin', 'rb') as temp_file, open('second.bin', 'wb') as f4_2:
    f4_2.write(temp_file.read())

print("---The end of exercise #4---" + '\n')






