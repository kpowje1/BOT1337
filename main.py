import telebot

bot = telebot.TeleBot('')#здесь токен бота
#если будет возникать ошибка 'TeleBot' object has no attribute 'message_handler' , попробуйте обновить библиотеку
# pip install --upgrade pyTelegramBotAPI
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
trans = {
        'а' : 'a',
        'б' : '6',
        'в' : 'B',
        'г' : 'r',
        'д' : 'D',
        'е' : 'e',
        'ё' : 'e',
        'ж' : '}|{',
        'з' : '3',
        'и' : 'u',
        'й' : 'u`',
        'к' : 'k',
        'л' : 'JI',
        'м' : 'M',
        'н' : 'H',
        'о' : 'o',
        'п' : 'n',
        'р' : 'p',
        'с' : 'c',
        'т' : 'T',
        'у' : 'y',
        'ф' : 'qp',
        'х' : 'x',
        'ц' : 'u,',
        'ч' : '4',
        'ш' : 'w',
        'щ' : 'w,',
        'ъ' : "'b",
        'ы' : 'bl',
        'ь' : 'b',
        'э' : '3',
        'ю' : '10',
        'я' : '9',
        'А' : 'A',
        'Б' : '6',
        'В' : 'B',
        'Г' : 'r',
        'Д' : 'D',
        'Е' : 'E',
        'Ё' : 'E',
        'Ж' : '}|{',
        'З' : '3',
        'И' : 'U',
        'Й' : 'U`',
        'К' : 'K',
        'Л' : 'JI',
        'М' : 'M',
        'Н' : 'H',
        'О' : 'O',
        'П' : '/7',
        'Р' : 'P',
        'С' : 'C',
        'Т' : 'T',
        'У' : 'Y',
        'Ф' : 'qp',
        'Х' : 'X',
        'Ц' : 'U,',
        'Ч' : '4',
        'Ш' : 'W',
        'Щ' : 'W,',
        'Ъ' : '`b',
        'Ы' : 'bl',
        'Ь' : 'b',
        'Э' : '3',
        'Ю' : '10',
        'Я' : '9'
        }

@bot.message_handler(content_types=['dice'])
def get_text_messages(message):
    casedv = {
    1 : 'плохо, пробуй ещё',
    2 : 'Лучше чем один',
    3 : 'Бог любит троицу',
    4 : 'фантастическая',
    5 : 'отлично',
    6 : 'Получается максимум'
    }
    bot.reply_to(message, casedv.get(message.dice.value))

@bot.message_handler(content_types=['text']) #проверка на восприятие текста
def get_text_message1337(message):
    if message.text.lower() == 'цвет':
            keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
            keyboard1.row('1','2')
            bot.send_message(message.chat.id,'qq', reply_markup=keyboard1)
    else:
            text1 = ''
            for t in message.text:
                if t in trans.keys():
                    text1 += trans.get(t)
                else: text1 += t
            bot.reply_to(message, text1)

bot.polling(none_stop=True)
