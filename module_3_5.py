def get_multiplied_digits(number):
    str_number = str(number)
    if int(str_number[0]) != 0:
        first = int(str_number[0])
    else:
        return 1
        #first = 1 Как правильно? Приравнивать переменную к единице или возвращать к единице???
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(40203)
print(result)
