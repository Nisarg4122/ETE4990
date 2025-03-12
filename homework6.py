#1
even_or_odd = lambda x: "Even" if x % 2 == 0 else "Odd"
print(even_or_odd(5))
print(even_or_odd(10))

#2
sum_list = lambda lst: sum(lst)
print(sum_list([1, 2, 3, 4, 5]))

#3
sort_numbers = lambda lst: sorted(lst)
numbers = [5, 2, 9, 1, 7]
sorted_numbers = sort_numbers(numbers)
print(sorted_numbers)

#4
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers) 

#5
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)

#6
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)

#7
sum_nums = reduce(lambda x, y: x + y, nums)
print(sum_nums)

#8
items = ['alpha', 'beta', 'delta']
enumerated_items = list(map(lambda x: f"Index {x[0]}: {x[1]}", enumerate(items)))
print(enumerated_items)

#9 zip without lambda

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped = list(zip(list1, list2))