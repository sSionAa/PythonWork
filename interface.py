from correct_value import *
from methods_notes import *

# интерфейс
file_name = "notes.jsonl"
file_arhive = "arhive.jsonl"

def interface():
    go_notes = True
    while go_notes:
        print("1. Добавить новую заметку\n" +
              "2. Найти заметку\n" +
              "3. Изменить заметку\n" +
              "4. Показать все заметки\n" +
              "5. Удалить заметку\n" +
              "6. Удалить все заметки\n" +
              "7. Показать удаленные заметки\n"
              "8. Закрыть заметки\n")
        input_menu = 0
        flag = False
        while flag != True:
            input_menu = input("Выберите пункт меню: => ")
            flag = is_correct_input(input_menu, 8)
        if int(input_menu) == 1:
            add_note(file_name)
        elif int(input_menu) == 2:
            interface_search()
        elif int(input_menu) == 3:
            interface_search()
            change_note(file_name)
        elif int(input_menu) == 4:
            show_notes(file_name)
        elif int(input_menu) == 5:
            interface_search()
            remove_note(file_name,file_arhive)
        elif int(input_menu) == 6:
            clear(file_name,file_arhive)
        elif int(input_menu) == 7:
            show_notes(file_arhive)
        elif int(input_menu) == 8:
            print("До свидания! Хорошего дня!\n")
            go_notes = False


def interface_search():
    search_in = input("Введите данные для поиска: => ")
    print("Вот что удалось найти: \n")
    print("*"*60)
    search_note(search_in,file_name)
