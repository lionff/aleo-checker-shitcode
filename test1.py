from bs4 import BeautifulSoup
import time
import requests
import telebot


while True:

# поиск в определённой зоне
    url = 'https://www.aleo.network/leaderboard/ALEOWALLET'

    token = 'telegram_token'
    bot = telebot.TeleBot(token)
    chat_id = 'chat_id'

# делаем запрос и получаем html
    html_text = requests.get(url).text

# используем парсер lxml
    soup = BeautifulSoup(html_text, 'lxml')

    ad = soup.find('span', class_ = 'text-aleo-green')

    f = open("test.txt", "w")
    f.write(str(ad))
    f.close() 

    data = []
    with open("test.txt") as f:
        for line in f:
            data.append([str(x) for x in line.split()])  


    data1 = []
    with open("test1.txt") as f:
        for line in f:
            data1.append([str(x) for x in line.split()])        

    a1 = ''.join(map(str, data))
    a2 = ''.join(map(str, data1))

    if a1 != a2:
        bot.send_message(chat_id, ad)
        f = open("test1.txt", "w")
        f.write(str(ad))
        f.close()  

    print(a1)
    print(a2)
    time.sleep(1200) #10