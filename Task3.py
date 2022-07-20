import requests
import datetime as DT

def requests_Stackoverflow(serch_tag, days_ago):
    url = 'https://api.stackexchange.com/2.3/questions'
    params = {
        'site': 'Stackoverflow',
        'order': 'desc',
        'sort': 'activity',
        'todate': DT.date.today(),
        'fromdate': DT.date.today() - DT.timedelta(days=days_ago),
        'tagged': serch_tag
    }
    response = requests.get(url, params=params)
    resp = response.json()
    print('Все вопросы за последние два дня которые содержат тэг "Python":')
    for item in resp['items']:
        print(f' ID вопроса: {item["question_id"]}, Заголовок вопроса: "{item["title"]}"')
        print(f' Ccылка на вопрос №{item["question_id"]}: {item["link"]}')


if __name__ == '__main__':
    requests_Stackoverflow('python', days_ago=2)