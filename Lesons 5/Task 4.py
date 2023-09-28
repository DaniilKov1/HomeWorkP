add_new = input("Хотите добавить нового преподавателя? 1- если да 2-если завершить")
final_list =[]
while add_new !="2":
    last_name = input('Фамилия препод')
    job = input("Должность преподавателя")
    amount = input("Введите общее число студентов").split(",")
    final_list.append([last_name,job,amount])
    add_new = input("Хотите добавить нового преподавателя? 1- если да 2-если завершить")
print(final_list)