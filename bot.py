import telebot
from telebot import types 
import random

bot = telebot.TeleBot("5268431616:AAELWCn8Fc6WCRIk_UdCpdBZUoXldP3cvVI")


f = open('opis.txt', 'r', encoding='UTF-8')
facts = f.read().split(']')
f.close()

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Выбрать ID вопроса")
    btn2 = types.KeyboardButton("Рандомный вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Привет, меня зовут Бот Красавчик. \nЯ создан для того, чтобы помочь подготовиться тебе к стажировке\nЧтобы узнать, что я умею, напиши /help' , reply_markup=keyboard)  



@bot.message_handler(commands=["help"])
def help_(message):
        keyboard = types.InlineKeyboardMarkup()
        with open('instruct.txt', encoding='utf-8') as f:
            m = f.read()
        bot.send_message(message.chat.id, m , reply_markup=keyboard)  



@bot.message_handler(commands=["question"])
def question_(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id, "Вопросы для собеседования:", reply_markup=keyboard)
    with open('questions.txt', encoding='utf-8') as f:
        l = f.read()
    bot.send_message(message.chat.id, l , reply_markup=keyboard)



@bot.message_handler(commands=["add_question"])
def add_(message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton( "Message the developer", url="telegram.me/phin03"))
    bot.send_message(message.chat.id,'Если есть предложения по изменению бота, свяжитесь с разработчиком.',reply_markup=keyboard)



@bot.message_handler(commands=["exit"])
def exit_(message):
    keyboard = types.InlineKeyboardMarkup()
    bot.send_message(message.chat.id,'До скорых встреч',reply_markup=keyboard)
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAEEYxpiTNNN4VJyXPKSSQa-5BqqTiD5gwACMgoAAm4y2AAB_W-265DwO00jBA")

    

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    keyboard = types.InlineKeyboardMarkup()
    if message.text == "1":
        bot.send_message(message.from_user.id, "Вопрос 1:\nЧто такое высокоуровневый и низкоуровневый язык программирования?  \nОтвет:\nНизкоуровневые языки являются менее портируемыми, поскольку их инструкции «машинозависимы». То есть, каждая инструкция написана для конкретной машины. Код, написанный для конкретной машины, не запустится на на компьютере с другой архитектурой. Высокоуровневые языки не зависят от аппаратной части",reply_markup=keyboard)
    if message.text == "2":
        bot.send_message(message.from_user.id, "Вопрос 2:\nЧто такое полнота языка по Тьюрингу?  \n Ответ:\nПолнота по Тьюрингу — характеристика исполнителя (множества вычисляющих элементов) в теории вычислимости, означающая возможность реализовать на нём любую вычислимую функцию.",reply_markup=keyboard)
    if message.text == "3":
        bot.send_message(message.from_user.id, "Вопрос 3:\nКакие есть операторы цикла?  \n Ответ:for и while",reply_markup=keyboard)
    if message.text == "4":
        bot.send_message(message.from_user.id, "Вопрос 4:\nЧто такое компилятор?  \n Ответ:\nКомпиля́тор — программа или техническое средство, выполняющее компиляцию.",reply_markup=keyboard)
    if message.text == "5":
        bot.send_message(message.from_user.id, "Вопрос 5:\nКакие  бывают типы?  \n Ответ:\nВ Python есть несколько стандартных типов данных:Numbers, Strings, Lists, Dictionaries ,Tuples,Sets ",reply_markup=keyboard)
    if message.text == "6":
        bot.send_message(message.from_user.id, "Вопрос 6:\nЧто значит for i in range()?  \n Ответ:\nЦикл",reply_markup=keyboard)
    if message.text == "7":
        bot.send_message(message.from_user.id, "Вопрос 7:\nЧто представляет из себя Agile?  \n Ответ:\nAgile, или Agile software development — гибкий подход к разработке программного обеспечения (ПО)",reply_markup=keyboard)
    if message.text == "8":
        bot.send_message(message.from_user.id, "Вопрос 8:\nЧто такое методология программирования?  \n Ответ:\nМетодология разработки программного обеспечения — совокупность методов, применяемых на различных стадиях жизненного цикла программного обеспечения и имеющих общий философский подход.",reply_markup=keyboard)
    if message.text == "9":
        bot.send_message(message.from_user.id, "Вопрос 9:\nЧто такое модульное программирование  \n Ответ:\nМо́дульное программи́рование — это организация программы как совокупности небольших независимых блоков, называемых модулями, структура и поведение которых подчиняются определённым правилам.",reply_markup=keyboard)
    if message.text == "10":
        bot.send_message(message.from_user.id, "Вопрос 10:\nВ чем разница между кортежем и списком в python?  \n Ответ:\nРазница между списком и кортежем заключается в том, что список объявляется в квадратных скобках и может быть изменен, в то время как кортеж объявляется в скобках и не может быть изменен",reply_markup=keyboard)

    if message.text == "Выбрать ID вопроса":
        keyboard = types.InlineKeyboardMarkup()
        
        bot.send_message(message.chat.id, "Выбирите ID вопроса" , reply_markup=keyboard)
        with open('questions.txt', encoding='utf-8') as f:
            l = f.read()
        bot.send_message(message.chat.id, l , reply_markup=keyboard)
    if message.text == 'Рандомный вопрос' :
        d = random.choice(facts)
        bot.send_message(message.chat.id, d)






bot.polling(none_stop=True, interval=0)
