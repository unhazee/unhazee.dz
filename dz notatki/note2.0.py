def save_exit():
    print('Збережено та закрито')
    exit(0)  # функція припиняє роботу програми


def add():
    file = open('notes.txt', 'a')  # відкриває файл для доповнення
    print()  # костиль який ставить відступ
    file.writelines(f"{input('Введіть нотатку: ')}\n")  # записує в файл нотатку
    file.close()


def earliest():
    try:
        file = open('notes.txt', 'r')  # відкриває файл для читання
        notes = file.readlines()  # читає усі стрічки в файлі
        print("\nВід найранішої до найпізнішої:", ''.join(notes)[:-1], sep='\n')  # виводить упорядковано
        file.close()
    except FileNotFoundError:  # ловить помилку про відсутність файлу
        file = open('notes.txt', 'w')  # створює файл
        file.close()


def latest():  # аналогічно із попередньою функцією
    try:
        file = open('notes.txt', 'r')
        notes = file.readlines()
        print("\nВід найпізнішої до найранішої:", (''.join(notes[::-1]))[:-1], sep='\n')
        file.close()
    except FileNotFoundError:
        file = open('notes.txt', 'w')
        file.close()


def longest():  # аналогічно із попередньою функцією
    try:
        file = open('notes.txt', 'r')
        notes = file.readlines()
        print("\nВід найдовшої до найкоротшої:", (''.join(sorted(notes, key=len)[::-1]))[:-1], sep='\n')
        file.close()
    except FileNotFoundError:
        file = open('notes.txt', 'w')
        file.close()


def shortest():  # аналогічно із попередньою функцією
    try:
        file = open('notes.txt', 'r')
        notes = file.readlines()
        print("\nВід найкоротшої до найдовшої:", ''.join(sorted(notes, key=len))[:-1], sep='\n')
        file.close()
    except FileNotFoundError:
        file = open('notes.txt', 'w')
        file.close()


commands = {  # словник який зберігає команди і відповідно ключу викликає відповідні функції за допомогою lambda ф-їй
    'exit': lambda x: save_exit(),
    'add': lambda x: add(),
    'earliest': lambda x: earliest(),
    'latest': lambda x: latest(),
    'longest': lambda x: longest(),
    'shortest': lambda x: shortest()
}
while True:
    request = input('\nВведіть команду: ')
    if request in commands:  # перевірка чи запит є командою
        commands.get(request)(0)  # виклик функції відповідно команді
    else:
        print('\nНемає такої команди')