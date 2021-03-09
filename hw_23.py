# Задача 3
#Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень).
# Напишите решения через list и через dict.


# Объявляем список seasons_list
seasons_list = ['winter', 'spring', 'summer', 'autumn']

# Объявляем список seasons_dict
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}

# Организуем пользовательский ввод номера месяца
month = int(input("Введите месяц по номеру "))

# Проверяем условия пользовательского ввода и выводим результат при true
if month ==1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])

# Иначе №1
elif month == 3 or month == 4 or month ==5:
    print(seasons_dict.get(2))
    print(seasons_list[1])

# Иначе №2
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

# Иначе №3
elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")

        