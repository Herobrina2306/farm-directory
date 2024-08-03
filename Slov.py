from rabota_s_failom import razdelenie # добавление функции разделения из другого файла

t = open('farm.txt', 'r', encoding='utf-8') # открытие файла в режиме чтения
lis = t.readlines() # превращение документа в список из строк
dict_ = razdelenie(lis) # преобразования списка в словарик

t.close() # закрытие файла
    

