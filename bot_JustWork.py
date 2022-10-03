#...НАЧАЛО КОДА...

#ИМПОРТИРУЕМ НУЖНЫЕ МОДУЛИ
import telebot 
import config as cf
#
#МЕСТО ДЛЯ ВСЕДОСТУПНЫХ ТЕКСТОВЫХ ПЕРЕМЕННЫХ

#
#ВЫВОДИМ ТОКЕН И ОБЪЯВЛЯЕМ БОТА
print('TOKEN:',cf.TOKEN)
print('...BOT started to @Testrt_Pintester_Creator_Bot...')
bot = telebot.TeleBot(cf.TOKEN)
#  +---------------------------------------+
#  |         НАБОР НУЖНЫХ КОНСТАНТ         |
#  +---------------------------------------+
bwellcome=False
bauth=False
bsingin=False
bsetname=False

#  +---------------------------------------+
#  |       НАБОР НУЖНЫХ ПЕРЕМЕННЫХ         |
#  +---------------------------------------+

wellcome_text='Привет, {0.first_name}! Я - <b>{1.first_name}</b>. Я простой Телеграм-Бот, но я постепенно набираюсь сил и умений! Надеюсь быть тебе полезным...'
tellaboutme='Я - бот JustWork, но друзья зовут меня  просто ДжаВо! Я постоянно обучаюсь и узнаю что-то новое! Теперь ты знаешь обо мне немного больше👾...'
#   ---АВТОРИЗАЦИЯ---
startauth='И снова здравствуйте!\nВведите логин: '
endauth='Введите пароль: '
#   =================
#   ---РЕГИСТРАЦИЯ---
helpsingin='\t-Регистрация-\n\t!!!Инструкции!!!\nДля регистрации необходимо ввести эл.почту и придумать пароль. После выполнения Вам придет пароль на почту, который нужно ввести для подтверждения и окончания регистрации!'
startsingin='Введите адрес эл.почты:'
endsingin='Придумайте пароль:'
endsingininfo='Я могу присылать Вам много полезного на эл.почту поэтому почаще еще проверяйте👾'
#   =================
helpinfo='Вот что я пока умею(скоро все изменится):\n\t1. /tellabout - рассказать меного о себе\n\t2. /setname - могу изменить имя обращения\n\t3. /singin - регистрация(пока в разработке)\n\t4. /auth - авторизация(пока в разработке)'
getdata=''

#  +---------------------------------------+
#  |        НАБОР НУЖНЫХ МЕТОДОВ           |
#  +---------------------------------------+

def wellcome(message):
    if(wellcome==False):
        bot.send_message(message.chat.id,wellcome_text.format(message.chat,bot.get_me()),parse_mode="html")
    else:
        help(message)

def tellabout(message):
     bot.send_message(message.chat.id,tellaboutme)

def help(message):
     bot.send_message(message.chat.id,helpinfo)


def singin_user(message):
     bot.send_message(message.chat.id,helpsingin)
     bsingin=True
     

#  #=========================================#
#  #-----------------------------------------#
#  #=========================================#

#МЕТОД ДЛЯ КОМАНДЫ /START
@bot.message_handler(commands=['start'])
def event(message):
    wellcome(message)
        
        
#МЕТОД ДЛЯ КОМАНДЫ /TELLNAME
@bot.message_handler(commands=['tellabout'])
def event(message):
    tellabout(message)

    
#МЕТОД ДЛЯ КОМАНДЫ /HELP
@bot.message_handler(commands=['help'])
def event(message):
    help(message)

@bot.message_handler(commands=['singin'])
def event(message):
    singin_user(message)
    


#МЕТОД ДЛЯ ОБРАБОТКИ ВВОДИМОГО ТЕКСТА 
@bot.message_handler(content_types=['text'])
def event(message):
    if(bsingin==True):
        print('Регистрация!')
    else:    
        bot.send_message(message.chat.id,message.text)


#RUN BOT...
bot.polling(none_stop=True)