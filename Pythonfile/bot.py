import requests
import bs4
from datetime import date
site = "https://sinoptik.com.ru/погода-москва"
html_list = ['']
temp = []
day_weekday = 0

def connect_site(site):
    global html_list
    r = requests.get(site)
    html_list=bs4.BeautifulSoup(r.text, "html.parser")

def parse_temp():
    global temp
    for i in range(1, 9):
        temp.append(html_list.select('.temperature .p'+str(i))[0].getText())

                    
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
    #функция для получения данных сайта 
    connect_site(site)
    #функция для обработки данных сайта 
    parse_temp()
     #функция для вывода дня недели 
    print(get_weekday())
    #Ночь
    print(temp[0] + " Ночью (0:00)")
    print(temp[1] + " Ночью (3:00)")
    #Утро  
    print(temp[2] + " Утром (6:00)")
    print(temp[3] + " Утром (9:00)")
    #День
    print(temp[4] + " Днем (12:00)")
    print(temp[5] + " Днем (15:00)")
    #Вечер
    print(temp[6] + " Вечером (18:00)")
    print(temp[7] + " Вечером (21:00)")
    #нформация о данных
    print("Данные взяты с сайта sinoptik.ru по городу Москва")
    input("Что бы закрыть программу, нажмите ENTER")
