# 1. Avoid comparing directly to `True`, `False`, or `None`

a = True
if a == False:
    # do something

if a:
    # do something

if a is None:
    # do something

# 2. Avoid repeating variable name in compound if statement

if name == 'Kan' or name == 'Man' or name == 'Natty':
    # do something

# # if name in ['Kan', 'Man', 'Natty']:
    # # # do something


# 3. Use `in` to iterate over iterable

# names = ['Kan', 'Man', 'Natty']
# for i in range(len(names)):
    # print(names[i])

# index = 0
# for name in names:
    # print(name)
    # index = index + 1

# 4. Use default parameter of `dict.get`
# persons = {
    # 'name': 'Kan',
    # 'company': 'Pronto'
# }

# if 'age' in persons:
    # print(persons['age'])
# else:
    # persons['age'] = 25


# persons.get('age', 25)

# 5. Use `enumerate` function in loops
# for idx, name in enumerate(names):
    # print(idx, name)


# 6. Use `_` for data that should be ignored

# data = (1, 2, 3, 4, 5)
# first = data[0]
# second = data[1]
# third = data[2]

# first, *second, third = data
# print(first, second, third)


# 7. Use (for) `else` after iterator is exhausted!

# checked = True
# spam = [True, True, True, False]
# for s in spam:
    # if not spam:
        # checked = False
        # break

# if checked:
    # print('all are spam')

# for s in spam:
    # if not spam:
        # checked = False
        # break
# else:
    # print('all are spam')


# 8. List comprehension to create a transformed list
# numbers = [1, 2, 3, 4, 5]
# results = []
# for n in numbers:
    # results.append(n * n)

# # -----------

# results = [n*n for n in numbers if n % 2 == 0]


# 9. Use context manager to ensure resources are managed
# f = open('filename', 'r')
# for row in f.readlines():
    # print(row)
# f.close()

# with open('filename', 'r') as f:
    # for row in f.readlines():
        # print(row)


# 10. Use generator to lazily load infinite sequences

def fibo(number):
    current_value, next_value = 0, 1
    for _ in range(number):
        print(current_value)
        current_value, next_value = next_value, current_value + next_value

# fibo(10)

def fibo(number):
    current_value, next_value = 0, 1
    for _ in range(number):
        yield current_value
        current_value, next_value = next_value, current_value + next_value

gen = fibo(10)
print(list(gen))

# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))


# def fibo(number):
    # current_value, next_value = 0, 1
    # for _ in range(number):
        # print(current_value)
        # current_value, next_value = next_value, current_value + next_value


# fibo(10)


# def fibo():
    # current_value, next_value = 0, 1
    # while True:
        # yield current_value
        # current_value, next_value = next_value, current_value + next_value


# gen = fibo()
# for _ in range(10):
    # print(next(gen))
