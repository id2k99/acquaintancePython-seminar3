# 17. Дан список.
# Определите сколько в нём встречается различных чисел

# список из неповторяющихся элементов
nums = [5, 2, 4, 5, 7, 2]
print(set(nums))

# элементы которые встречаются один раз
uniqNums = [i for i in nums if nums.count(i) == 1] # генератор списка
print(uniqNums)

uniqNums1 = [] #тот же генератор, только расписаный циклом
for i in nums:
    if nums.count(i) == 1:
        uniqNums1.append(i)

print(uniqNums)
print(uniqNums1) 
