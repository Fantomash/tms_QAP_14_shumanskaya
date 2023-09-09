# 1. Напишите генератор который принимает список
# numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7] и
# возвращает новый список только с положительными числами

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]


def positive_numbers(numbers):
    for number in numbers:
        if number > 0:
            yield number


positive_generator = positive_numbers(numbers)

# Необходимо составить список чисел которые
# указывают на длину слов в строке: sentence = " thequick
# brown fox jumps over the lazy dog", но только если слово
# не "the" с обработкой исключений

sentence = " thequick brown fox jumps over the lazy dog"
words_list = sentence.split()
length = []
for i in words_list:
    try:
        if i != "the":
            length.append(len(i))
    except:
        print("We do not include the word 'the'")

print(length)



