import re
from tkinter import *


# переменная для проверки, была ли уже неудачная попытка ввести слово
anErrorOnceOccured = None


# лимит на 30 вводимых символов в строке
def character_limit(entryWord):
    if len(entryWord.get()) > 30:
        entryWord.set(entryWord.get()[:30])


# событие при клике на кнопку поиска
def buttonClicked():
    global anErrorOnceOccured
    global warningText
    try:
        
        for i in str(entryWord.get()):
            if not bool(re.search('[\u0400-\u04FF]', i)):
                raise StopIteration
                
    except StopIteration:
            anErrorOnceOccured = True
            warningText.grid(column = 0, row = 1, padx = 5, columnspan = 2, sticky = "w")
            
    else:
        if anErrorOnceOccured:
            warningText.grid_forget()
        mainProgramPart()


# основная часть программы
def mainProgramPart():
    pass




# настройки окна
window = Tk()
window.title("Slavic Comparator")
window.geometry('1000x500')

# начальный текст
entryText = Label(window, text = "Введите слово на русском:")
entryText.grid(column = 0, row = 0, padx = 5, pady = 5, sticky = "w")
entryText.config(font = ("Times New Roman", 13))

# строка с вводом
entryWord = StringVar()    # переменная с текстом, введённым в виджет
entryWidget = Entry(window, width = 40, textvariable = entryWord)
entryWidget.grid(column = 1, row = 0, padx = 5, pady = 5)
entryWidget.config(font = ("Times New Roman", 13))

# кнопка для начала поиска
startButton = Button(window, text = "Начать перевод", command = buttonClicked)
startButton.grid(column = 2, row = 0, padx = 40, pady = 5)
startButton.config(font = ("Times New Roman", 11))

# предупреждающий об ошибке текст, если введённое слово неверное
warningText = Label(window, text = "В слове присутствуют не-кириллические символы либо пробелы!")
warningText.config(font = ("Times New Roman", 12), fg = "red")
warningText.grid_forget()

# отслеживаем лимит
entryWord.trace("w", lambda *args: character_limit(entryWord))

window.mainloop