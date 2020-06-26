import urllib.request
import json
import re
import os

def getTranslation(wordURL, language2):
    source = "https://iapi.glosbe.com/iapi3/wordlist?l1=ru&l2=" + language2 + "&q=" + wordURL + "&after=1&includeTranslations=true"
    with urllib.request.urlopen(source) as url: data = json.loads(url.read().decode())
    data = str(data)
    parser = re.findall(r'\w+', data)
    parser.remove('after')
    parser.remove('phrase')
    parser.remove('translations')
    parser.remove('success')
    parser.remove('True')
    if (parser[0] != word):
        return "нет информации"
    else:
        if (len(parser) >= 3):
            if  parser[1] != parser[2].lower():
                return parser[1] + " / " + parser[2]
            elif (len(parser) >= 4) and (parser[1] != parser[3].lower()):
                return parser[1] + " / " + parser[3]
            else:
                return parser[1]
        else:
            return parser[1]
    
while (True):    
    print("Введите слово на русском:")
    word = input()
    wordURL = urllib.parse.quote(word)
    
    print("\nВОСТОЧНОСЛАВЯНСКИЕ ЯЗЫКИ\n")
            
    print("Белорусский: ", getTranslation(wordURL, 'be'))
    print("Украинский: ", getTranslation(wordURL, 'uk'))
    print("Русинский: ", getTranslation(wordURL, 'rue'))
    print("Древнерусский: ", getTranslation(wordURL, 'orv'))

    print("\nЗАПАДНОСЛАВЯНСКИЕ ЯЗЫКИ\n")

    print("Польский: ", getTranslation(wordURL, 'pl'))
    print("Кашубский: ", getTranslation(wordURL, 'csb'))
    print("Силезский: ", getTranslation(wordURL, 'szl'))
    print("Верхнелужицкий: ", getTranslation(wordURL, 'hsb'))
    print("Нижнелужицкий: ", getTranslation(wordURL, 'dsb'))
    print("Полабский: ", getTranslation(wordURL, 'pox'))
    print("Чешский: ", getTranslation(wordURL, 'cs'))
    print("Словацкий: ", getTranslation(wordURL, 'sk'))

    print("\nЮЖНОСЛАВЯНСКИЕ ЯЗЫКИ\n")

    print("Словенский: ", getTranslation(wordURL, 'sl'))
    print("Хорватский: ", getTranslation(wordURL, 'hr'))
    print("Сербский: ", getTranslation(wordURL, 'sr'))
    print("Сербохорватский: ", getTranslation(wordURL, 'sh'))
    print("Боснийский: ", getTranslation(wordURL, 'bs'))
    print("Македонский: ", getTranslation(wordURL, 'mk'))
    print("Болгарский: ", getTranslation(wordURL, 'bg'))
    print("Церковнославянский: ", getTranslation(wordURL, 'cu'))

    print("\nВыбрать новое слово? (да / любое иное слово или символ)")
    word = input()
    if (word != 'да'):
        break
    else:
        os.system('cls')