# -*- coding: utf-8 -*-
import telebot
import requests
import config
import bs4

# Создание бота с указанным токеном доступа
access_token = "390259084:AAECTCnWgEG0l6H5fqboOuH1ckMzKtaXqeY"
bot = telebot.TeleBot(access_token)

# Бот будет отвечать только на текстовые сообщения
@bot.message_handler(commands=['monday'])
def get_monday(message):
    _, group = message.text.split()
    web_page = get_page(group)
    times_lst, lessons_lst = get_schedule_monday(web_page)
    resp = ''
    for time, lesson in zip(times_lst, lessons_lst):
        resp += '<b>{}</b>, {}\n'.format(time, lesson)
    bot.send_message(message.chat.id, resp, parse_mode='HTML')

def echo(message):
    bot.send_message(message.chat.id, message.text)



def get_page(group, week='now'):
    url = 'https://ifspo.ifmo.ru/schedule/get?num={gr}&week={week}.html'.format(
        gr = group,
        week = week
    )
    print(url)
    response = requests.get(url)
    web_page = response.content
    return web_page

def get_schedule_monday(web_page,):
    soup = bs4.BeautifulSoup(web_page, 'html5lib')
    schedule_table = soup.find("table", attrs={"class": "weekday-table"})
    times_list = schedule_table.find_all("div", attrs={"class": "period"})
    times_list = [time.span.text for time in times_list]
    #locations_list = schedule_table.find_all("div", attrs={"class": "place"})
    #locations_list = [room.span.text for room in locations_list]
    while schedule_table !='NULL':
        lessons_list = schedule_table.find_all("div", attrs={"class": "lesson_name "})
        lessons_list += schedule_table.find_all("div", attrs={"class": "lesson_name oddlesson"})
        lessons_list += schedule_table.find_all("div", attrs={"class": "lesson_name segryslesson"})
        lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
    return times_list, lessons_list

if __name__ == '__main__':
    bot.polling(none_stop=True)