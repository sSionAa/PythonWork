import random
import sys
from msvcrt import getch
from datetime import datetime
import json
import os

# сохранение заметки



def add_note(file_name):
    note = {}
    id_note = chr(random.randint(65, 90)) + \
        chr(random.randint(65, 90)) + str(random.randint(0, 1001))
    theme_note = input("Введите краткое описание заметки: => ")
    if len(theme_note) > 30:
        theme_note = theme_note[:31]
    if theme_note == "" or theme_note == None or theme_note == ' ':
        theme_note = "Тема отсутствует"
    print("Текст заметки (после окончания ввода нажмите Enter и ESC): => ")
    text_note = ''
    for line in sys.stdin:
        text_note = text_note+line
        key = ord(getch())
        if key == 27:
            break
    note["id"] = id_note
    note["тема"] = theme_note
    datetime_note = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    note["дата_и_время заметки"] = datetime_note
    note["дата_и_время_изменения_заметки"] = datetime_note
    note["заметка"] = text_note
    with open(file_name, "a", encoding='utf-8') as notes_file:
        json.dump(note, notes_file, ensure_ascii=False)
        notes_file.write('\n')
    print("\nЗаметка сохранена\n")

# удаление заметки


def remove_note(file_name,file_arhive):
    id_note = input("Введите id заметки, которую необходимо удалить: => ")
    print()
    with open(file_name, "r", encoding="utf-8") as notes_file:
        data = [json.loads(jline) for jline in notes_file]
        data_new = []
        for v in data:
            if id_note == v["id"]:
                with open(file_arhive, 'a', encoding='utf-8') as a_file:
                    json.dump(v, a_file, ensure_ascii=False)
                    a_file.write('\n')
                print("Заметка", id_note, "удалена\n")
            else:
                data_new.append(v)
    if len(data) == len(data_new):
        print("Указанный id не обнаружен. Поробуйте еще раз.\n")
    else:
        with open(file_name, 'w', encoding='utf-8') as record_file:
            for d in data_new:
                json.dump(d, record_file, ensure_ascii=False)
                record_file.write('\n')
# очищение файла


def clear(file_name,file_arhive):
    print('*'*60)
    answer = input("Вы уверены, что хотите удалить все заметки?(Д/Н) =>")
    print()
    if answer.lower() in ["y", 'yes', "да", "д"]:
        with open(file_name,'r+', encoding="utf-8") as notes_file:
            data = [json.loads(jline) for jline in notes_file]
            with open(file_arhive, 'a', encoding='utf-8') as a_file:
                for d in data:
                    json.dump(d, a_file, ensure_ascii=False)
                    a_file.write('\n')
            notes_file.truncate(0) 
            
        print('*'*60)
        print("Все заметки удалены\n")


# изменение заметки


def change_note(file_name):
    id_note = input("Введите id заметки, которую необходимо изменить: => ")
    new_note = {}
    with open(file_name, "r", encoding="utf-8") as notes_file:
        data = [json.loads(jline) for jline in notes_file]
        data_new = []
        for v in data:
            if id_note == v["id"]:
                theme_note = input("Введите краткое описание заметки: => ")
                if len(theme_note) > 30:
                    theme_note = theme_note[:31]
                if theme_note == "" or theme_note is None or theme_note == ' ':
                    theme_note = v["тема"]
                print("Текст заметки (после окончания ввода нажмите Enter и ESC): => ")
                text_note = ''
                for line in sys.stdin:
                    text_note = text_note+line
                    key = ord(getch())
                    if key == 27:
                        break
                new_note["id"] = v["id"]
                new_note["тема"] = theme_note
                datetime_note = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                new_note["дата_и_время заметки"] = v["дата_и_время заметки"]
                new_note["дата_и_время_изменения_заметки"] = datetime_note
                new_note["заметка"] = text_note
                data_new.append(new_note)
                print("\nЗаметка", id_note, "изменена\n")
            else:
                data_new.append(v)
    if data_new==data:
        print("Заметок с id",id_note,"не найдено. Попробуйте еще раз.\n")
    else:
        with open(file_name, 'w', encoding='utf-8') as record_file:
            for d in data_new:
                json.dump(d, record_file, ensure_ascii=False)
                record_file.write('\n')

# поиск заметки


def search_note(search_in,file_name):
    if search_in in ["None", '', " "]:
        show_notes(file_name)
        return
    count=0
    with open(file_name, "r", encoding="utf-8") as notes_file:
        data = [json.loads(jline) for jline in notes_file]
        for v in data:
            for val in v.values():
                if search_in.lower() in val.lower() or val.lower() in search_in.lower():
                    count+=1
                    for key, value in v.items():
                        if key == "заметка":
                            print("*"*60)
                            print(value.rstrip())
                        else:
                            print(f"{key}{" "*(30-len(key))} : {value.rstrip()}")
                    print()
                    break
    if count==0:
        print("К сожалению, ничего не нашлось, попробуйте еще раз.\n")
        

# показать все заметки


def show_notes(file_name):
    with open(file_name, "r", encoding="utf-8") as notes_file:
        data = [json.loads(jline) for jline in notes_file]
        if len(data)==0:
            print("\nНет заметок\n")
            return
        for v in data:
            for key, value in v.items():
                if key == "заметка":
                    print("*"*60)
                    print(value.rstrip())
                else:
                    print(f"{key}{" "*(30-len(key))} : {value.rstrip()}")

            print('\n', "*"*60, sep='')
