# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()  # выполняется
print_params(b=25)  # выполняется
print_params(c=[1, 2, 3])  # выполняется
# print_params(a=1, b=2, c=3, d=4) - здесь ошибка, лишний параметр
print_params(3, 2, 1)  # выполняется
# print(b=1, c=2, a=5) - здесь тоже ошибка, параметры расположены не в том порядке как задано в функции

# 2.Распаковка параметров:
values_list = ['строчка', False, 2.56]
values_dict = {'a': 130, 'b': True, 'c': 'еще строчка'}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [1000, 'тысяча']
print_params(*values_list_2, 42)  # выполняется, так как 2 первых параметра распакованы из списка
