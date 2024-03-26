# Проверка данных
def is_correct_input(data, end_index_menu):
    try:
        if data is None:
            return False
        if data.isdigit() is False:
            raise TypeError(
                'Неверно введен номер меню. Введите число от 1 до '+ str(end_index_menu))
        if int(data) < 1 or int(data) > end_index_menu:
            raise ValueError(
                'Неверно введен номер меню. Введите число от 1 до ' + str(end_index_menu))
        return True
    except TypeError as err:
        print(err)
        return False
    except ValueError as e:
        print(e)
        return False
