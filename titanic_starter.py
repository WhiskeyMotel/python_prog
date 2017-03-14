# Практическая работа

#### Задание 1: Скачайте файл с данными о погибших на титанике
import requests
import os

def to_str(lines):
    # Функция возвращает список преобразованных строк,
    # а принимает список байтовых строк
    
    # Отдельно взятую строку байт можно преобразовать в строку
    # символов следующим образом: str(line, 'utf-8')+'\n'
    # Символ перехода на новую строку добавляется, чтобы при
    # записи в файл каждая запись начиналась с новой строки
    
    # Удалите pass и представьте ваше решение
    str_lines = []
    for line in lines:
        str_lines.append(str(line, 'utf-8'))
    return str_lines


def download_file(url):
    # Делаем GET-запрос по указанному адресу
    response = requests.get(url)
    # Получаем итератор строк
    text = response.iter_lines()
    # Каждую строку конвертируем из массива байт в массив символов
    text = to_str(text)

    # Если файла не существует, то создаем его и записываем данные
    if not os.path.isfile("titanic.csv"):
        with open("titanic.csv", "w") as f:
            f.writelines(text)
    return text

#data = download_file("https://raw.githubusercontent.com/haven-jeon/introduction_to_most_usable_pkgs_in_project/master/bicdata/data/titanic.csv")

# Если вы успешно выполнили первое задание, то файл можно не скачивать
# каждый раз, а вместо этого данные читать из файла. Расскомментируйте
# следующую строку и закомментируйте предыдущую
data = open('titanic_ext.csv')

#### Задание 2: Получаем список словарей
# Модуль для работы с файлами в формате CSV
import csv

reader = csv.DictReader(data)
reader.fieldnames[0] = 'lineno'
titanic_data = list(reader)

# Модуль для красивого вывода на экран
from pprint import pprint as pp
pp(titanic_data[:2])
pp(titanic_data[-2:])


#### Задание 3: Узнать количество выживших и погибших на Титанике
def survived(tit_data):
    # Функция возвращает кортеж из двух элементов: количество
    # выживших и число погибших
    total_count = 0
    for person in tit_data:
        if person['survived'] == '1':
            total_count += 1
    print(total_count, len(tit_data) - total_count)

(survived(titanic_data)) # (500, 809)


#### Задание 4: Узнать количество выживших и погибших на Титанике
def survived_by_sex(tit_data):
    ####Функция возвращает список кортежей из двух элементов вида:
    ####(пол, (количество выживших, число погибших))
    ####Подумайте над использованием функции survived()
    survived_male = 0
    dead_male = 0
    total_count = 0
    for person in tit_data:
        if person['survived'] == '1':
            total_count += 1
    for person in tit_data:
        if person['survived'] == '1' and person['sex'] == 'male':
            survived_male += 1
        elif person['survived'] == '0' and person['sex'] == 'male':
            dead_male += 1
    print('female', total_count - survived_male, len(tit_data) - total_count - dead_male, 'male', survived_male, dead_male)

(survived_by_sex(titanic_data)) # [('female', (339, 127)), ('male', (161, 682))]


#### Задание 5: Узнать средний возраст пассажиров
def average_age(tit_data):
    # Функция возвращает средний возраст пассажиров
    total_age = 0
    buf = 0
    for person in tit_data:
        if person['age']!='NA':
            total_age += float(person['age'])
        else:
            buf += 1
    print(total_age/(len(tit_data) - buf))
(average_age(titanic_data)) # 29.88


#### Задание 6: Узнать средний возраст мужчин и женщин по отдельности
def average_age_by_sex(tit_data):
    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, средний возраст)

    # Подумайте над использованием функции average_age()
    total_age_male = 0
    total_age_fem = 0
    total_male = 0
    total_female = 0
    buf_male = 0
    buf_fem = 0
    for person in tit_data:
        if person['sex'] == 'male' and person['age'] != 'NA':
            total_age_male += float(person['age'])
            total_male += 1
        elif person['sex'] == 'male' and person['age'] == 'NA':
            buf_male +=1
            total_male += 1
        if person['sex'] == 'female' and person['age'] != 'NA':
            total_age_fem += float(person['age'])
            total_female += 1
        elif person['sex'] == 'female' and person['age'] == 'NA':
            buf_fem += 1
            total_female += 1
    print('male', total_age_male/(total_male - buf_male), 'female', total_age_fem/(total_female-buf_fem))

(average_age_by_sex(titanic_data)) # [('female', 28.68), ('male', 30.58)]


#### Задание 7: Сколько детей и взрослых было на борту:
#### Получить группы в следующих диапазонах возрастов:
#### [0-14), [14-18), [18-inf]
def group_age(tit_data):
    children = 0
    adults = 0
    old_person = 0
    for person in tit_data:
        if person['age'] != 'NA' and float(person['age'])<14:
            children += 1
        elif person['age'] != 'NA' and 14<=float(person['age'])<18:
            adults += 1
        elif person['age'] != 'NA' and float(person['age'])>=18:
            old_person += 1
    print ('Childrens: ', children, 'Teenagers: ', adults, 'Adults: ', old_person)

group_age(titanic_data)
#### Задание 8: Сколько в каждой группе выживших
def surv_group_age(tit_data):
    children = 0
    adults = 0
    old_person = 0
    for person in tit_data:
        if person['age'] != 'NA' and float(person['age'])<14 and person['survived'] == '1':
            children += 1
        elif person['age'] != 'NA' and 14<=float(person['age'])<18 and person['survived'] == '1':
            adults += 1
        elif person['age'] != 'NA' and float(person['age'])>=18 and person['survived'] == '1':
            old_person += 1
    print ('Childrens: ', children, 'Teenagers: ', adults, 'Adults: ', old_person)

surv_group_age(titanic_data)
#### Задание 9: Сколько в каждой группе выживших по отдельности для
#### мужчин и женщин
def surv_group_age_by_sex(tit_data):
    children_m = 0
    children_f = 0
    adults_m = 0
    adults_w = 0
    old_m = 0
    old_w = 0
    for person in tit_data:
        if person['age'] != 'NA' and float(person['age'])<14 and person['survived'] == '1' and person['sex'] == 'male':
            children_m += 1
        if person['age'] != 'NA' and float(person['age'])<14 and person['survived'] == '1' and person['sex'] == 'female':
            children_f += 1
        elif person['age'] != 'NA' and 14<=float(person['age'])<18 and person['survived'] == '1' and person['sex'] == 'male':
            adults_m += 1
        elif person['age'] != 'NA' and 14<=float(person['age'])<18 and person['survived'] == '1' and person['sex'] == 'female':
            adults_w += 1
        elif person['age'] != 'NA' and float(person['age'])>=18 and person['survived'] == '1' and person['sex'] == 'male':
            old_m += 1
        elif person['age'] != 'NA' and float(person['age'])>=18 and person['survived'] == '1' and person['sex'] == 'female':
            old_w += 1
    print ('Survived:\nfemale Children=', children_f, '\nmale children=', children_m, '\nfemale Teenagers=', adults_w, '\nmale teenagers=', adults_m, '\nfemale Adults=', old_w, '\nmale adults=', old_m)

surv_group_age_by_sex(titanic_data)