import os

from weather_sdk import get_new_event, SMSServer

token1 = os.getenv('FORECAST_TOKEN')
town_title = 'Курск'
token = os.getenv('SMS_TOKEN')
server = SMSServer(token)

new_event = get_new_event(token1, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{town_title}: {event_time} {event_date} {event_area} ожидается {phenomenon_description}. Будьте внимательны и осторожны.'''

sms_message = sms_template.format(phenomenon_description = phenomenon_description,town_title = town_title, event_time = event_time, event_date = event_date, event_area = event_area) 
    


server.send(sms_message)

# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: При выводе переменной получился такой резултат: Регион:  Погода:
# Вывод: прогноза нет

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: Переменная вывела: Курск
# Вывод: Гипотеза 2.1 не верна

# Гипотеза 2.2: В town_title не название города
# Способ проверки: Выведу переменную town_title
# Код для проверки: print(town_title)
# Установленный факт: Переменная вывела: Курск
# Вывод: Гипотеза 2.2 не верна

# Гипотеза 3: token на самом деле пуст
# Способ проверки: Выведу переменную token
# Код для проверки: print(token)
# Установленный факт: Переменная вывела: None
# Вывод: token пуст

# Гипотеза 4.1: Может, `token` всё ещё пуст?
# Способ проверки: Выведу переменную token
# Код для проверки: print(token)
# Установленный факт: Переменная вывела токен
# Вывод: Гипотеза 4.1 не верна

# Гипотеза 4.2: Может, в токене не то значение, не `85b98d96709fd49a69ba8165676e4592`?
# Способ проверки: Выведу переменную token
# Код для проверки:print(token)
# Установленный факт: Переменная вывела не тот токен
# Вывод: Гипотеза 4.2 верна

# Гипотеза 4.3: Может, значение `85b98d96709fd49a69ba8165676e4592` успевает измениться до строчки `new_event = ...`?
# Способ проверки: Выведу переменную token до строчки `new_event = ...`
# Код для проверки: print(token)
# Установленный факт: Да,значение успевает измениться до строчки `new_event = ...`
# Вывод:  Гипотеза 4.3 верна

# Гипотеза 5.1: Переменная `event_time` пуста/в ней не время
# Способ проверки: Выведу переменную
# Код для проверки: print(event_time)
# Установленный факт: Переменная вывела время
# Вывод: Переменная работает

# Гипотеза 5.2: Переменная `event_date` пуста/в ней не дата
# Способ проверки: Выведу переменную
# Код для проверки: print(event_date)
# Установленный факт: Переменная вывела дату
# Вывод: Переменная работает

# Гипотеза 5.3: Переменная `event_area` пуста/в ней не место
# Способ проверки: Выведу переменную
# Код для проверки: print(event_area)
# Установленный факт: Переменная вывела место
# Вывод: Переменная работает

# Гипотеза 5.4: Переменная `phenomenon_description` пуста/в ней не описание погодного явления
# Способ проверки: Выведу переменную
# Код для проверки: print(phenomenon_description)
# Установленный факт: Переменная вывела погодное явление
# Вывод: Переменная работает

# Гипотеза 6: Ошибка в шаблоне ?
# Способ проверки: Проверка шаблона на наличие ошибок в регистре/языке
# Код для проверки: town_title,event_time,event_date,event_area,sms_template
# Установленный факт: Шаблон в порядке
# Вывод: Гипотеза 6 не верна

# Гипотеза 7: Ошибка в скобках?
# Способ проверки: Уберу скобки в шаблоне
# Код для проверки: sms_template = '''town_title: event_time event_date event_area ожидается phenomenon_description. Будьте внимательны и осторожны.'''
# Установленный факт: Программа работает,но не выдает желаемый результат
# Вывод: Гипотеза 7 не верна

# Гипотеза 8: .format() не видит переменных
# Способ проверки: подстановка переменных
# Код для проверки: sms_message = sms_template.format(phenomenon_description = phenomenon_description,town_title = town_title, event_time = event_time, event_date = event_date, event_area = event_area) 
# Установленный факт: .format не видел переменных
# Вывод: Код работает,мы идеальны!