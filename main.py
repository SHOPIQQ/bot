import telebot
from telebot import types
bot = telebot.TeleBot('6097489332:AAHzBwn8RZDZv5U7kdvK4Nt11GXcVU3fNlw')
@bot.message_handler(commands=['start'])
def welcome(x):
    f=types.ReplyKeyboardMarkup(resize_keyboard=True)
    i1=types.KeyboardButton('Рассчитать стоимость')
    i2=types.KeyboardButton('Сделать заказ')
    i3=types.KeyboardButton('Популярные вопросы')
    i4=types.KeyboardButton('Надежность сервиса')
    f.add(i1,i2,i3,i4)

    bot.send_message(x.chat.id, 'Добро пожаловать в бота помощника!',reply_markup=f)
@bot.message_handler(content_types=['text'])
def f(x):
    if(x.chat.type=='private'):
        if(x.text=='Рассчитать стоимость'):
            f=types.InlineKeyboardMarkup(row_width=1)
            i1=types.InlineKeyboardButton('Обувь', callback_data="i1")
            i2=types.InlineKeyboardButton('Одежда',callback_data="i2")
            i3=types.InlineKeyboardButton('Техника',callback_data="i3")
            f.add(i1, i2, i3)
            bot.send_message(x.chat.id, '<b>Вид товара📦</b>', reply_markup=f,parse_mode='html')
        elif(x.text=='Сделать заказ'):
            bot.send_message(x.chat.id,'<b>Напишите @shopiqqadmin (9:00-03:00 МСК)</b>', parse_mode='html')
        elif(x.text=='Популярные вопросы'):
            bot.send_message(x.chat.id, c,parse_mode='html')
        elif(x.text=='Надежность сервиса'):
            bot.send_message(x.chat.id, f'<b>{b}</b>', parse_mode='html')
            bot.send_photo(x.chat.id, w)
            bot.send_message(x.chat.id,f'<b>{d}</b>',parse_mode='html')
            bot.send_video_note(x.chat.id,q)
        else:
            bot.send_message(x.chat.id, 'Я не знаю как ответить')

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    try:
        if call.message:
            bot.send_message(call.message.chat.id, '<b>Введите стомость в ¥\nЕсли вы не знаете стоимость'
                                                   '-свяжитесь @shopiqqadmin</b>',parse_mode='html')
            if(call.data=='i1'):
                bot.register_next_step_handler(call.message, obuv)
            if(call.data=='i2'):
                bot.register_next_step_handler(call.message,odezda)
            if(call.data=='i3'):
                bot.register_next_step_handler(call.message,tehno)

    except Exception as e:
        print(repr(e))
def obuv(x):
    if(x.text.isdigit()):
        if(int(x.text)>3000):
            bot.send_message(x.chat.id,f'<b>{int(int(x.text)*kurs*1.15)}</b>{u}',parse_mode='html')
        elif(int(x.text)<3000)and(int(x.text)>1000):
            bot.send_message(x.chat.id,f'<b>{int(int(x.text)*kurs*1.25)}</b>{u}',parse_mode='html')
        elif (int(x.text) < 1000) and (int(x.text) > 500):
            bot.send_message(x.chat.id, f'<b>{int(int(x.text) * kurs * 1.3)}</b>{u}', parse_mode='html')
        else:
            bot.send_message(x.chat.id, f'<b>{int(int(x.text) * kurs * 1.37)}</b>{u}', parse_mode='html')
    else:
        bot.send_message(x.chat.id,'введите только число, если вы не знаете стоимость'
        'свяжитесь @shopiqqadmin')
        bot.register_next_step_handler(x,obuv)
def odezda(x):
    if(x.text.isdigit()):
        bot.send_message(x.chat.id, f'<b>{int(int(x.text)*kurs*1.35)}</b>{u1}',parse_mode='html')
    else:
        bot.send_message(x.chat.id, 'введите только число, если вы не знаете стоимость'
                                    'свяжитесь @shopiqqadmin')
        bot.register_next_step_handler(x,odezda)
def tehno(x):
    if(x.text.isdigit()):
        bot.send_message(x.chat.id,f'<b>{int(int(x.text)*kurs*1.3)}</b>{u1}',parse_mode='html')
    else:
        bot.send_message(x.chat.id, 'введите только число, если вы не знаете стоимость'
                                    'свяжитесь @shopiqqadmin')
        bot.register_next_step_handler(x,tehno)







kurs=13
c=(f'<b>Оригинал❓</b>\n\nДа, строго оригинал. Возможны все проверки.\n\n<b>Сколько дней доставка</b>❓\n\n'
f'Время доставки 9-19 дней с момента получения посылки командой в Китае\n\n'
f'<b>Доставка в другой город.</b>\n\n'
f'Доставляем через СДЭК\n\n'
f'<b>Как забрать свой заказ❓</b>\n\n'
f'Самовывоз в Москве доступен по предварительной договорённости с поддержкой - @Shopiqqadmin\n\n'
f'Адрес самовывоза: м. Проспект вернадского, Удальцова 32с2\n\n'
f'<b>Что если не забрать заказ❓</b>')
b=('<b>Доставили более 5000 товаров клиентам\nотзывы тут @shopiqqcomments\n</b>')
d=('<b>В этом видео только малая часть нашей работы\nПриемка ваших заказов командой в Москве\n'
'Фотоотчеты клиентам, созданные командой в Китае</b>')
u=('<b>₽ - это (цена товаров, доставка до склада в Китае, страховка товара, комиссия,)\n\n'
'В ПОДАРОК К ЛЮБОЙ ОБУВИ КЛАДЁМ ОРИГИНАЛЬНЫЕ НОСКИ NIKE.</b>\n\n'
'ПОСЛЕ ОФОРМЛЕНИЯ ЗАКАЗА ВЫ ВСЕГДА МОЖЕТЕ ОТСЛЕДИТЬ СВОЮ ПОСЫЛКУ В НАШЕЙ ТАБЛИЦЕ. '
'ПЛЮС ЭКСПРЕСС ДОСТАВКА С КИТАЯ В МОСКВУ 499₽/500гр, СРОК 3-19 ДНЕЙ. '
'КАК ТОЛЬКО ВАШ ТОВАР ПРИХОДИТ НА НАШ СКЛАД В КИТАЕ МЫ ВЫШЛЕМ ВАМ ЕГО ДЕТАЛЬНЫЕ ФОТОГРАФИИ\n\n'
'<b>ДЛЯ ОФОРМЛЕНИЯ ЗАКАЗА СВЯЖИТЕСЬ С @SHOPIQQADMIN(скиньте фото товара, длину стопы или размер) и '
'укажите оплата на карту Тинькофф или по сбп</b>')
u1=('<b>₽ - это (цена товаров, доставка до склада в Китае, страховка товара, комиссия,)</b>\n\n'
'ПОСЛЕ ОФОРМЛЕНИЯ ЗАКАЗА ВЫ ВСЕГДА МОЖЕТЕ ОТСЛЕДИТЬ СВОЮ ПОСЫЛКУ В НАШЕЙ ТАБЛИЦЕ. '
'ПЛЮС ЭКСПРЕСС ДОСТАВКА С КИТАЯ В МОСКВУ 499₽/500гр, СРОК 3-19 ДНЕЙ. '
'КАК ТОЛЬКО ВАШ ТОВАР ПРИХОДИТ НА НАШ СКЛАД В КИТАЕ МЫ ВЫШЛЕМ ВАМ ЕГО ДЕТАЛЬНЫЕ ФОТОГРАФИИ\n\n'
'<b>ДЛЯ ОФОРМЛЕНИЯ ЗАКАЗА СВЯЖИТЕСЬ С @SHOPIQQADMIN(скиньте фото товара, длину стопы или размер) и '
'укажите оплата на карту Тинькофф или по сбп</b>')
video=open('/Users/saadharsiev/Downloads/68523dbc-4641-4b8a-aed8-eccdca4c11fd.mp4','rb')
photo=open('/Users/saadharsiev/Downloads/photo_2023-10-27 02.51.42.jpeg','rb')
q=video.read()
w=photo.read()
bot.polling(none_stop=True)
