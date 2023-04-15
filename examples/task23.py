# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)

#простой вариант
nums = [1, 2, 3, 1, 2]
count = 0
for i in range(1, len(nums)):
    if nums[i] > nums[i-1]:
        count += 1
print(count)

#вариант с генератором списков
result = [nums[i] for i in range(1, len(nums)) if nums[i] > nums[i-1]]
print(len(result))