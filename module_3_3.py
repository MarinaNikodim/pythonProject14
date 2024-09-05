def print_params(a = 1, b = 'string', c = True):

    print(a, b, c)


print_params()
print_params(77)
print_params(b=25)
print_params(c=[1, 2, 3])

c = [1, 2, 3]

print_params(c)

#2.
values_list = [33, 'house', (77, 78)]
values_dict = {'a': "7", 'b': 'sea', 'c': 356}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = ['Elizabeth', 1999]
print_params(*values_list_2, 42)

