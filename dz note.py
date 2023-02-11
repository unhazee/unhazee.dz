def note():
    list_01 = list()  # порожній список
    print("add")  # виводим текст з проханням
    add = input("Введіть нататку")  # вводим перший елемент списку
    list_01.append(add)  # доповнюєм наш список першим елементом
    while True:
        _input_ = input()  # перемінна яка буде запрошувати ввод данних
        if _input_ == "add":  # якщо add то просимо ввести нову нотатку
            add2 = input("Введіть нататку")
            list_01.append(add2)  # доповнєм нові данні в наш список
        elif _input_ == "earliest":  # ключ earliest виводить збережені нотатки у хронологічному порядку
            c = ('\n'.join(list_01))
            print(c)  # від найранішої до найпізнішої
        elif _input_ == "latest":  # ключ latest виводить збережені нотатки у хронологічному порядку
            list_01.reverse()
            v = (('\n'.join(list_01)))
            print(v)  # - від найпізнішої до найранішої
            list_01.reverse()
        elif _input_ == "longest":  # ключ longest - виводить збережені нотатки у порядку їх довжини
            long = sorted(list_01, key=len, reverse=True)
            print('\n'.join(long))  # - від найдовшої до найкоротшої
        elif _input_ == "shortest":  # ключ shortest - виводить збережені нотатки у порядку їх довжини
            short = sorted(list_01, key=len)
            print('\n'.join(short))  # - від найкоротшоїдо найдовшої


acting = note()
print(acting)
