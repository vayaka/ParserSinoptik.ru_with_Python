import requests
import bs4
from datetime import date
site = "https://sinoptik.com.ru/погода-москва"
html_list = ['']
temp = ['']
day_weekday = 0

def connect_site(site):
    global html_list
    r = requests.get(site)
    html_list=bs4.BeautifulSoup(r.text, "html.parser")

def parse_temp():
    global temp
    p1_temp=html_list.select('.temperature .p1')
    p2_temp=html_list.select('.temperature .p2')
    p3_temp=html_list.select('.temperature .p3')
    p4_temp=html_list.select('.temperature .p4')
    p5_temp=html_list.select('.temperature .p5')
    p6_temp=html_list.select('.temperature .p6')
    p7_temp=html_list.select('.temperature .p7')
    p8_temp=html_list.select('.temperature .p8')
    temp[0] = p1_temp[0].getText()
    temp.append(p2_temp[0].getText())
    temp.append(p3_temp[0].getText())
    temp.append(p4_temp[0].getText())
    temp.append(p5_temp[0].getText())
    temp.append(p6_temp[0].getText())
    temp.append(p7_temp[0].getText())
    temp.append(p8_temp[0].getText())
def get_weekday():
    global day_weekday
    day_weekday = date.today().weekday()
    if day_weekday == 0:
        return "Погода на подельник"
    elif day_weekday == 1:
        return "Погода на вторник"
    elif day_weekday == 2:
        return "Погода на среду"
    elif day_weekday == 3:
        return "Погода на четверг"
    elif day_weekday == 4:
        return "Погода на пятницу"
    elif day_weekday == 5:
        return "Погода на субботу"
    elif day_weekday == 6:
        return "Погода на воскресение"



if __name__ == '__main__':
    connect_site(site)
    parse_temp()
    print(get_weekday())
    for x in range(5):
        if x == 1:
            print(temp[0] + " Ночью (0:00)")
            print(temp[1] + " Ночью (3:00)")
        if x == 2:
            print(temp[2] + " Утром (6:00)")
            print(temp[3] + " Утром (9:00)")
        if x == 3:
            print(temp[4] + " Днем (12:00)")
            print(temp[5] + " Днем (15:00)")
        if x == 4:
            print(temp[6] + " Вечером (18:00)")
            print(temp[7] + " Вечером (21:00)")
    print("Данные взяты с сайта sinoptik.ru по городу Москва")
    input("Что бы закрыть программу, нажмите ENTER")
