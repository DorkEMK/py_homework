import os
import sys
import datetime
import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime, date, timedelta
import pymystem3
mystem=pymystem3.Mystem()

date_start = datetime.strptime(sys.argv[1],"%Y-%m-%d")
date_finish = datetime.strptime(sys.argv[2],"%Y-%m-%d")
step = timedelta(days=1)

source = 'lenta.ru' # а может не надо

# файл с метаданными
metatable = open('lenta_metadata.csv', 'a')
heads = ['path', 'author','date','source','title','url','wordcount','\n']
metatable.write('\t'.join([head for head in heads]))

current_date = date_start

while current_date  <= date_finish:

    date_for_parsing = current_date.strftime("%Y/%m/%d")

    # получаем список статей за текущую дату
    articles_page = 'https://' + source + '/' + date_for_parsing + '/'
    articles_names = BeautifulSoup(requests.get(articles_page).text, "html5lib").find_all("h3")
    articles = ["http://lenta.ru"+l("a")[0]["href"] for l in articles_names]

    counter = 0

    # для каждой статьи из списка:
    for article in articles:

        metadata = []

        # скачиваем статью
        resp = requests.get(article)
        bs = BeautifulSoup(resp.text, "html5lib")

        # получаем url
        url = article

        # получаем название статьи
        getname = re.compile('/([^/]*)/$') 
        name = getname.search(url)
        if not name:
            print(url)
            sys.exit(1)
        name = name.group(1)

        # получаем пути
        path_to_plain_text = '/'.join(['.', source, 'plain.text', date_for_parsing[:7], (name+'.txt')])
        path_to_parsed_text = '/'.join(['.', source, 'parsed.text', date_for_parsing[:7], (name+ '.tsv')])
        
        # извлекаем автора
        author = BeautifulSoup(" ".join([p.text for p in bs.find_all("p", {"itemprop" : "author"})]), "html5lib").get_text().replace(u'\xa0', u' ')
        if not author:
            author = '-'
        
        # дату можно просто добавить
        # можно извлекать из url
        # getdatesname = re.compile('/(....)/(..)/(..)/([^/]*)/')
        # dates = getdatesname.search(url)
        date = date_for_parsing
        
        # название сайта аналогично дате:
        # getsource = re.compile('https://(.+?)/')
        # source = getsource.match(url)[1]
        
        # получаем заголовок
        title = bs.h1.text.replace(u'\xa0', u' ')

        # достаем и парсим текст
        text = BeautifulSoup(" ".join([p.text for p in bs.find_all("p") if p.attrs.get('itemprop') != 'author']), "html5lib").get_text().replace(u'\xa0', u' ')

        # и записываем его
        directory = os.path.dirname(path_to_plain_text)
        if not os.path.exists(directory):
            os.makedirs(directory)

        with open(path_to_plain_text, 'w') as f:
            f.write(text)

        # открываем файл для записи размеченного текста
        directory = os.path.dirname(path_to_parsed_text)
        if not os.path.exists(directory):
            os.makedirs(directory)

        parsed = open(path_to_parsed_text, 'w')
            

        # обрабатываем и считаем слова
        # mystem снимает частеречную омонимию, но оставляет варианты морфологического разбора
        # оставлять все или отрезать первый зависит от будущего использования файла
        # в общем случае целесообразнее оставить все и при необходимости удалить при использовании
        wordcount = 0 
        for i in mystem.analyze(text):
            if i['text'] == ' ' or i['text'] == '\n':
                continue
            elif len(i) == 1 or i['analysis'] == []:
                parse = i['text']+'\t'+'-'+'\t'+'-'+'\n'
            else:
                parse = i['text']+'\t'+i['analysis'][0]['lex']+'\t'+i['analysis'][0]['gr']+'\n'
                wordcount +=1
            parsed.write(parse)

        # собираем метаданные
        metadata.append(path_to_plain_text)
        metadata.append(author)
        metadata.append(date)
        metadata.append(source)
        metadata.append(title) 
        metadata.append(url)
        metadata.append(str(wordcount))
        
        # записываем в файл метаданные
        metatable.write('\t'.join([i for i in metadata])+'\n')

        counter +=1

    print(date_for_parsing, counter, sep = '\t')

    current_date += step
