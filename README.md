# SlavicComparator
Small program written in Python, allowing you to input a word in **English** / **Russian** and get its translations from all other Slavic languages. Translations are done with Glosbe API, GUI implemented with Tkinter.

Note that I initially started to code this project in Russian, eventually coming up with the idea it should be in English as well. That's why it has **two versions**, for both languages. The only difference between them is their interface and the word you input (either in Russian or English).

Now to the files and folders:

* **SlavicComparatorGUI.py** - основная часть программы.

* **SlavicComparatorFunctions.py** - модуль, в который были выведены все функции, никак не взаимодействующие с Tkinter (только посредством основной части).

* **/console_version** - папка, в которой хранится консольная версия программы. Её более удобно использовать для отладки программы и поиска ошибок (главный код там почти одинаковый), да и работает немного быстрее.


Известные (потенциальные) ошибки:

* Если в наборе данных, полученных c Glosbe API, появится ещё какое-нибудь лишнее техническое слово, то результат перевода может оказаться неправильным. Для уже известных мне "аномальных" данных есть регулярные выражения, все эти данные обрабатывающие - если появится что-то новое, то это скорее всего сразу будет заметно.

* Наличие в латинских словах (из перевода) похожих кириллических символов никак не обработано. Например, если два перевода будут отличаться лишь буквой "о" (одна из которых - латинская, а другая - кириллическая), то программа сочтёт эти два слова разными и выведет их вместе, хоть визуально они и одинаковы. Тем не менее, такой ситуации я сам ещё не встречал, в отличие от обратной (наличие латинских букв в кириллическом слове), однако вот это уже обработано.

* В консольной версии программы некоторые символы могут не отображаться. Особенно хорошо это видно на примере церковнославянских слов, которые иногда записаны глаголицей.
