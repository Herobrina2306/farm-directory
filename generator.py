# Вычисление премии и создание словаря в одну строку (однострочный гениратор)

names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

# Создаём словарь и прописываем в нём ключь из одного словаря, и значение взятое из расчёта двух других. 
result = {names[i]: salary[i] * int(bonus[i][:-1]) / 100 for i in range(len(salary))}
print(result)



# Гениратор чисел фибоначи. 
def fibonacci():
    j = [0, 1]
    for i in j:
        yield i # оператор замораживает генератор и возобнавляет работу с этого места при следующем вызове.
        f = j[-1] + j[-2]
        j.append(f)

    


f = fibonacci()
for i in range(10):
    print(next(f))