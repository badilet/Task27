# Напишите функцию где исходный список содержит положительные и отрицательные
# числа. Требуется положительные поместить в один список, а отрицательные - в другой.

num_list = [2, -4, 3, -43, 65, 87, -21, 98, -424, 457, -98585, 1132, -5253545, 89]

n = [x for x in num_list if x < 0]
print(n)
n = [x for x in num_list if x >= 0]
print(n)
