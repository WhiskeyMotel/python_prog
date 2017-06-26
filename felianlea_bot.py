# -*- coding: utf-8 -*-
import telebot
import requests
import config
import bs4
import datetime

# Создание бота с указанным токеном доступа
access_token = "390259084:AAECTCnWgEG0l6H5fqboOuH1ckMzKtaXqeY"
bot = telebot.TeleBot(access_token)


# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(commands=['monday','tuesday','wednesday','thursday','friday','saturday'])
def get_day(message):
    day, group = message.text.split()
    web_page = get_page(group)
    times_lst, locations_lst, lessons_lst = get_schedule(day, web_page)
    resp = ''
    for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
        resp += '<b>{}</b>\n-{}\n-{}\n'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')

@bot.message_handler(commands=['tomorrow'])
def get_nextday(message):
    _, group = message.text.split()
    web_page = get_page(group)
    day = datetime.date.today().weekday()+1
    print(day)
    if day == 6:
        day = 0
    times_lst, locations_lst, lessons_lst = get_schedule(day, web_page)
    resp = ''
    for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
        resp += '<b>{}</b>\n-{}\n-{}\n'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')

@bot.message_handler(commands=['all'])
def get_all(message):
    _, group = message.text.split()
    web_page = get_page(group)
    resp = ''
    weekday = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота']
    for i in range(5):
        resp += '\n{}:\n'.format(weekday[i])
        times_lst, locations_lst, lessons_lst = get_schedule(i, web_page)
        for time, location, lession in zip(times_lst, locations_lst, lessons_lst):
            resp += '<b>{}</b>\n-{}\n-{}\n'.format(time, location, lession)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')

@bot.message_handler(commands=['nearest'])
def get_nearest_pair(message):
    _, group = message.text.split()
    weekday = datetime.datetime.now().weekday()
    time_now = str(datetime.datetime.now().time().hour) + ':'+ str(datetime.datetime.now().time().minute)
    resp=''
    web_page = get_page(group)
    times_lst, locations_lst, lessons_lst = get_schedule(weekday, web_page)
    for time, location, lesson in zip(times_lst, locations_lst, lessons_lst):
        if  len(time)<11:
            time = '0'+time
            print(time)
        if time_now < time:
            resp = '<b>{}</b>\n-{}\n-{}\n'.format(time, location, lesson)
            break
    bot.send_message(message.chat.id, resp, parse_mode='HTML')




def get_page(group, week=''):
    if week:
        week = str(week) + '/'
    url = 'http://www.ifmo.ru/ru/schedule/0/{group}/{week}raspisanie_zanyatiy_{group}.htm'.format(
        week=week,
        group=group)
    response = requests.get(url)
    web_page = response.text
    return web_page


def get_schedule(day, web_page, ):
    soup = bs4.BeautifulSoup(web_page, 'html5lib')
    schedule_table = soup.find("table", attrs={"id": "{weekday}".format(
        weekday=table_id(day)
    )})

    # Время проведения занятий
    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    # Место проведения занятий
    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    # Название дисциплин и имена преподавателей
    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split('\n') for lesson in lessons_list]
    buffer = [' '.join([info for info in lesson_info if info]) for lesson_info in lessons_list]
    lessons_list = []
    for i in buffer:
        if '\t' in i:
            lessons_list.append(i.replace('\t', ''))
    return times_list, locations_list, lessons_list

def table_id(day):
    print(day)
    if day=='/monday' or day==0:
        return '1day'
    elif day=='/tuesday' or day==1:
        return '2day'
    elif day=='/wednesday' or day==2:
        return '3day'
    elif day=='/thursday' or day==3:
        return '4day'
    elif day=='/friday' or day==4:
        return '5day'
    elif day=='/saturday' or day==5:
        return '6day'


if __name__ == '__main__':
    bot.polling(none_stop=True)