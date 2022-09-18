# Программа по удалению из текста всех слов, содержащих "абв"

def delete_text(input_string):
    """Функция по удалению из текста всех элементов, содержащих 'абв'.
    Аргумент - введенная пользователем строка"""
    any_list = list(input_string.split())
    result_list = list()
    for i in any_list:
        if "абв" not in i:
            result_list.append(i)
    res_string = ""
    for i in result_list:
        res_string = res_string + i + " "
    return res_string

with open("input_task_1.txt", "w") as file_1:
    user_string = str(input("Введите строку: "))
    file_1.write(user_string)

with open("output_task_1.txt", "w") as file_2:
    file_2.write(delete_text(user_string))
