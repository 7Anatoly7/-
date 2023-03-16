# Запуск игры
import random
words = ['звезда', 'космос', 'планета', 'галактика', 'комета', 'астероид', 'вселенная']
# Выбор случайного слова из списка
hidden_word = random.choice(words)
find_letters = set()
used_letters = set()
alphabet = set('абвгдеёжзийклмнопростуфхцчшщъыьэюя')
count = 0
# Начало игры
print('!help - вывод текущей справки\n'
      '!use - показать использованные буквы\n'
      '!remain - показать оставшиеся буквы\n'
      '!surrender - сдаться\n'
      '!exit - выйти из игры')
while True:
    # Подсчёт количества попыток
    count += 1
    # Вывод звёздочек или букв, если они угаданы
    for letter in hidden_word:
        if letter not in find_letters:
            print('*', end='')
        else:
            print(letter, end='')
    print()
    # Проверка, найдены ли все буквы в слове
    if set(hidden_word) == find_letters:
        print('Ура, победа! Вы угадали слово!')
        question2 = input('Хотите другое загаданное слово?(да/нет) ').lower()
        is_out = False
        while True:
            if question2 == 'да':
                hidden_word = random.choice(words)
                break
            elif question2 == 'нет':
                print('До свидания!')
                is_out = True
                break
            else:
                print('Команда введена неверно. Попробуйте заново')
                question2 = input('Хотите другое загаданное слово?(да/нет) ').lower()
        if is_out:
            break
    # Ввод буквы или всего слова целиком
    players_letter = input('Введите букву или всё слово: ').lower().strip()
    # Проверка, введена ли одна буква и буква ли это вообще
    if len(players_letter) == 1 and 'а' <= players_letter <= 'я':
        # Проверка, есть ли буква в слове и не была ли она уже названа
        if players_letter in hidden_word and players_letter not in used_letters:
            print('Ура, вы угадали букву!')
            find_letters.add(players_letter)
        elif players_letter in used_letters:
            print('Такую букву вы уже называли . _ .')
        else:
            print('Увы, такой буквы нет :(')
    # Проверка на то, является ли словом(состоит только из букв)
    elif players_letter.isalpha():
        # Проверка, угадано ли слово
        if players_letter == hidden_word:
            print('Ура, победа! Вы угадали слово!')
            question2 = input('Хотите другое загаданное слово?(да/нет) ').lower()
            is_out = False
            while True:
                if question2 == 'да':
                    hidden_word = random.choice(words)
                    break
                elif question2 == 'нет':
                    print('До свидания!')
                    is_out = True
                    break
                else:
                    print('Команда введена неверно. Попробуйте заново')
                    question2 = input('Хотите другое загаданное слово?(да/нет) ').lower()
            if is_out:
                break
        elif ' ' in players_letter:
            print('Загадано только одно слово')
        elif len(players_letter) < len(hidden_word):
            print('Вводите по одной букве')
        elif len(players_letter) > len(hidden_word):
            print('Введённая строка превышает длину загаданного слова')
        else:
            print('Увы, вы не угадали слово :(')
    # Проверка на то, может ли это быть командой
    elif players_letter[0] == '!':
        # Проверка, есть ли эта команда в списке команд
        if players_letter[1:] in ['help', 'use', 'remain', 'surrender', 'exit']:
            # Выполнение команд
            if players_letter[1:] == 'help':
                print('!help - вывод текущей справки\n'
                      '!use - показать использованные буквы\n'
                      '!remain - показать оставшиеся буквы\n'
                      '!surrender - сдаться\n'
                      '!exit - выйти из игры')
            elif players_letter[1:] == 'use':
                print(used_letters)
            elif players_letter[1:] == 'remain':
                print(alphabet - used_letters)
            elif players_letter[1:] == 'surrender':
                question1 = input('Вы уверены, что хотите сдаться? ').lower()
                if question1 == 'да':
                    print('Загаданное слово:', hidden_word)
                    question2 = input('Хотите другое загаданное слово?(да/нет) ').lower()
                    is_out = False
                    while True:
                        if question2 == 'да':
                            hidden_word = random.choice(words)
                            break
                       elif question2 == 'нет':
                            print('До свидания!')
                            is_out = True
                            break
                        else:
                            print('Команда введена неверно. Попробуйте заново')
                            question2 = input('Хотите другое загаданное слово?(да/нет) ').lower()
                    if is_out:
                        break
                elif question1 == 'нет':
                    continue
                else:
                    print('Попробуйте заново')
            elif players_letter[1:] == 'exit':
                question1 = input('Вы уверены, что хотите выйти? ').lower()
                if question1 == 'да':
                    print('До свидания!')
                    break
                elif question1 == 'нет':
                    continue
                else:
                    print('Попробуйте заново')
        else:
            print('Такой команды не существует')
    else:
        print('Неверный ввод...')
print('Количество попыток:', count)



