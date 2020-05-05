# -*- coding: utf-8 -*-
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
import random

vk_session = vk_api.VkApi(token='33027c7e4293698597ddd7a503549a6cd885382819e7ff6c2c9c09cb908624e69b562b5301b3debf6e375')
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)


def create_keyboard(answer):
    keyboard = VkKeyboard(one_time=False)
    if answer == 'начать':
        keyboard.add_button('да', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)
    elif answer == 'Начать':
        keyboard.add_button('да', color=VkKeyboardColor.POSITIVE)
        keyboard.add_line()
        keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)
    # elif answer == 'да':
    # keyboard.add_button('Отправьте мне страну Европы, у которой хотите узнать столицу(Пишите с большой буквы)',
    # color=VkKeyboardColor.POSITIVE)
    # keyboard.add_line()
    # keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)
    # elif answer == 'Отправьте мне страну Европы, у которой хотите узнать столицу(Пишите с большой буквы)':
    # keyboard.add_button('Нидерланды', color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button('Швейцария', color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button('Андорра', color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button('Греция', color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button('Сербия', color=VkKeyboardColor.POSITIVE)
    # keyboard.add_button('Германия', color=VkKeyboardColor.POSITIVE)
    ##keyboard.add_button('', color=VkKeyboardColor.POSITIVE)
    ##keyboard.add_button('', color=VkKeyboardColor.POSITIVE)
    ##keyboard.add_button('', color=VkKeyboardColor.POSITIVE)
    ##keyboard.add_button('', color=VkKeyboardColor.POSITIVE)
    ##keyboard.add_button('', color=VkKeyboardColor.POSITIVE)
    ##keyboard.add_button('', color=VkKeyboardColor.POSITIVE)
    # keyboard.add_line()
    # keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)
    # elif answer == 'Андорра':
    # keyboard.add_button('Да, я хочу узнать больше о Андорре', color=VkKeyboardColor.POSITIVE)
    # keyboard.add_line()
    # keyboard.add_button('Пока', color=VkKeyboardColor.NEGATIVE)


def send_answer(vk_session, id_type, id, message=None, attachment=None, keyboard=None):
    vk_session.method('messages.send',
                      {id_type: id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648),
                       'attachment': attachment, 'keyboard': keyboard})


for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        answer = event.text
        keyboard = create_keyboard(answer)
        if event.to_me:
            if answer == 'Начать':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Здравствуйте, я бот, который поможет вам запомнить столицы', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Отправьте мне страну Европы, у которой хотите узнать столицу(Пишите с большой буквы)',
                            keyboard=keyboard)

            elif answer == 'начать':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Здравствуйте, я бот, который поможет вам запомнить столицы', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Отправьте мне страну Европы, у которой хотите узнать столицу(Пишите с большой буквы)',
                            keyboard=keyboard)

            elif answer == 'Нидерланды':
                send_answer(vk_session, 'user_id', event.user_id, message='Амстердам', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == '   ':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 17,151,228<br>Площадь: 41,543 км^2<br>Девиз: Я выстою',
                            keyboard=keyboard)

            elif answer == 'Андорра':
                send_answer(vk_session, 'user_id', event.user_id, message='Андорра-ла-Велья', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше об Андорре':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 85,708<br>Площадь: 468 км^2<br>Девиз: Вместе мы сильнее',
                            keyboard=keyboard)

            elif answer == 'Греция':
                send_answer(vk_session, 'user_id', event.user_id, message='Афины', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Греции':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 10,761,523<br>Площадь: 131,957 км^2<br>Девиз: Свобода или смерть',
                            keyboard=keyboard)

            elif answer == 'Сербия':
                send_answer(vk_session, 'user_id', event.user_id, message='Белград', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Сербии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 7,078,110<br>Площадь: 77,474 км^2<br>Девиз: Только единство спасёт сербов',
                            keyboard=keyboard)

            elif answer == 'Германия':
                send_answer(vk_session, 'user_id', event.user_id, message='Берлин', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Германии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 80,457,737<br>Площадь: 357,022 км^2<br>Девиз: Единство, Право, Свобода',
                            keyboard=keyboard)

            elif answer == 'Швейцария':
                send_answer(vk_session, 'user_id', event.user_id, message='Берн', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Швейцарии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 8,292,809<br>Площадь: 41,277 км^2<br>Девиз: Один за всех, все за одного',
                            keyboard=keyboard)

            elif answer == 'Словакия':
                send_answer(vk_session, 'user_id', event.user_id, message='Братислава', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Словакии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 5,445,040<br>Площадь: 49,035 км^2', keyboard=keyboard)

            elif answer == 'Бельгия':
                send_answer(vk_session, 'user_id', event.user_id, message='Брюссель', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Бельгии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 11,570,762<br>Площадь: 30,528 км^2<br>Девиз: Единство создает силу',
                            keyboard=keyboard)

            elif answer == 'Венгрия':
                send_answer(vk_session, 'user_id', event.user_id, message='Будапешт', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Венгрии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 9,825,704<br>Площадь: 93,028 км^2', keyboard=keyboard)

            elif answer == 'Румыния':
                send_answer(vk_session, 'user_id', event.user_id, message='Бухарест', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Румынии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 21,457,116<br>Площадь: 238,391 км^2', keyboard=keyboard)

            elif answer == 'Лихтенштейн':
                send_answer(vk_session, 'user_id', event.user_id, message='Вадуц', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Лихтенштейне':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 38,547<br>Площадь: 160 км^2<br>Девиз: За Бога, Князя и Отечество',
                            keyboard=keyboard)

            elif answer == 'Мальта':
                send_answer(vk_session, 'user_id', event.user_id, message='Валетта', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Мальте':
                send_answer(vk_session, 'user_id', event.user_id, message='Население: 449,043<br>Площадь: 316 км^2',
                            keyboard=keyboard)

            elif answer == 'Польша':
                send_answer(vk_session, 'user_id', event.user_id, message='Варшава', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Польше':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 38,420,687<br>Площадь: 312,685 км^2', keyboard=keyboard)

            elif answer == 'Ватикан':
                send_answer(vk_session, 'user_id', event.user_id, message='Ватикан', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Ватикане':
                send_answer(vk_session, 'user_id', event.user_id, message='Население: 1,000<br>Площадь: 0,44 км^2',
                            keyboard=keyboard)

            elif answer == 'Австрия':
                send_answer(vk_session, 'user_id', event.user_id, message='Вена', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше об Австрии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 8,793,370<br>Площадь: 83,871 км^2', keyboard=keyboard)

            elif answer == 'Литва':
                send_answer(vk_session, 'user_id', event.user_id, message='Вильнюс', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Литве':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 2,793,284<br>Площадь: 65,300 км^2', keyboard=keyboard)

            elif answer == 'Ирландия':
                send_answer(vk_session, 'user_id', event.user_id, message='Дублин', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше об Ирландии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 5,068,050<br>Площадь: 70,273 км^2', keyboard=keyboard)

            elif answer == 'Хорватия':
                send_answer(vk_session, 'user_id', event.user_id, message='Загреб', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Хорватии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 4,270,480<br>Площадь: 56,594 км^2', keyboard=keyboard)

            elif answer == 'Украина':
                send_answer(vk_session, 'user_id', event.user_id, message='Киев', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше об Украине':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 43,952,299<br>Площадь: 603,550 км^2<br>Девиз: Слава Украине!',
                            keyboard=keyboard)

            elif answer == 'Молдавия':
                send_answer(vk_session, 'user_id', event.user_id, message='Кишинёв', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Молдавии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 3,437,720<br>Площадь: 33,851 км^2', keyboard=keyboard)

            elif answer == 'Дания':
                send_answer(vk_session, 'user_id', event.user_id, message='Копенгаген', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Дании':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 5,809,502<br>Площадь: 43,094 км^2<br>Девиз: Помощь Господа, любовь народа, сила Дании',
                            keyboard=keyboard)

            elif answer == 'Португалия':
                send_answer(vk_session, 'user_id', event.user_id, message='Лиссабон', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Португалии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 10,355,493<br>Площадь: 92,090 км^2', keyboard=keyboard)

            elif answer == 'Великобритания':
                send_answer(vk_session, 'user_id', event.user_id, message='Лондон', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Великобритании':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 65,105,246<br>Площадь: 243,610 км^2<br>Девиз: Бог и моё право',
                            keyboard=keyboard)

            elif answer == 'Словения':
                send_answer(vk_session, 'user_id', event.user_id, message='Любляна', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Словении':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 2,102,126<br>Площадь: 20,273 км^2', keyboard=keyboard)

            elif answer == 'Люксембург':
                send_answer(vk_session, 'user_id', event.user_id, message='Люксембург', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Люксембурге':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 605,764<br>Площадь: 2,586 км^2<br>Девиз: Мы хотим остаться теми, кто мы есть',
                            keyboard=keyboard)

            elif answer == 'Испания':
                send_answer(vk_session, 'user_id', event.user_id, message='Мадрид', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше об Испании':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 49,331,076<br>Площадь: 505,370 км^2<br>Девиз: Дальше предела',
                            keyboard=keyboard)

            elif answer == 'Белоруссия':
                send_answer(vk_session, 'user_id', event.user_id, message='Минск', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Белорусии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 9,527,543<br>Площадь: 207,600 км^2<br>Девиз: Жыве Беларусь!',
                            keyboard=keyboard)

            elif answer == 'Монако':
                send_answer(vk_session, 'user_id', event.user_id, message='Монако', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Монако':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 30,727<br>Площадь: 2,02 км^2<br>Девиз: С Божьей помощью',
                            keyboard=keyboard)

            elif answer == 'Россия':
                send_answer(vk_session, 'user_id', event.user_id, message='Москва', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о России':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 142,122,776<br>Площадь: 17,098,242 км^2', keyboard=keyboard)

            elif answer == 'Норвегия':
                send_answer(vk_session, 'user_id', event.user_id, message='Осло', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Норвегии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 5,372,191<br>Площадь: 323,802 км^2', keyboard=keyboard)

            elif answer == 'Фрация':
                send_answer(vk_session, 'user_id', event.user_id, message='Париж', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Франции':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 67,364,357<br>Площадь: 643,801 км^2<br>Девиз: Свобода, Равенство, Братство',
                            keyboard=keyboard)

            elif answer == 'Черногория':
                send_answer(vk_session, 'user_id', event.user_id, message='Подгорица', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Черногории':
                send_answer(vk_session, 'user_id', event.user_id, message='Население: 614,249<br>Площадь: 13,812 км^2',
                            keyboard=keyboard)

            elif answer == 'Чехия':
                send_answer(vk_session, 'user_id', event.user_id, message='Прага', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Чехии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 10,686,269<br>Площадь: 78,867 км^2<br>Девиз: Истина побеждает',
                            keyboard=keyboard)

            elif answer == 'Исландия':
                send_answer(vk_session, 'user_id', event.user_id, message='Рейкьявик', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше об Исландии':
                send_answer(vk_session, 'user_id', event.user_id, message='Население: 343,518<br>Площадь: 103,000 км^2',
                            keyboard=keyboard)

            elif answer == 'Латвия':
                send_answer(vk_session, 'user_id', event.user_id, message='Рига', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Латвии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 1,923,559<br>Площадь: 64,589 км^2', keyboard=keyboard)

            elif answer == 'Италия':
                send_answer(vk_session, 'user_id', event.user_id, message='Рим', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше об Италии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 62,246,674<br>Площадь: 301,340 км^2', keyboard=keyboard)

            elif answer == 'Сам-Марино':
                send_answer(vk_session, 'user_id', event.user_id, message='Сан-Марино', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Сан-Марино':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 33,779<br>Площадь: 61 км^2<br>Девиз: Свобода', keyboard=keyboard)

            elif answer == 'Босния и Герцеговина':
                send_answer(vk_session, 'user_id', event.user_id, message='Сараево', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Боснии и Герцеговине':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 3,849,891<br>Площадь: 51,197 км^2', keyboard=keyboard)

            elif answer == 'Северная Македония':
                send_answer(vk_session, 'user_id', event.user_id, message='Скопье', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Северной Македонии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 2,118,945<br>Площадь: 25,713 км^2<br>Девиз: Свобода или Смерть',
                            keyboard=keyboard)

            elif answer == 'Болгария':
                send_answer(vk_session, 'user_id', event.user_id, message='София', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Болгарии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 7,057,504<br>Площадь: 110,879 км^2<br>Девиз: Единство создаёт силу',
                            keyboard=keyboard)

            elif answer == 'Швеция':
                send_answer(vk_session, 'user_id', event.user_id, message='Стокгольм', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Швеции':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 10,040,995<br>Площадь: 450,295 км^2<br>Девиз: За Швецию - во все времена! ',
                            keyboard=keyboard)

            elif answer == 'Эстония':
                send_answer(vk_session, 'user_id', event.user_id, message='Таллин', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше об Эстония':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 1,244,288<br>Площадь: 45,228 км^2', keyboard=keyboard)

            elif answer == 'Албания':
                send_answer(vk_session, 'user_id', event.user_id, message='Тирана', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше об Албании':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 3,057,220<br>Площадь: 28,748 км^2<br>Девиз: Ты, Албания,даёшь мне честь, даёшь мне имя албанца',
                            keyboard=keyboard)

            elif answer == 'Финляндия':
                send_answer(vk_session, 'user_id', event.user_id, message='Хельсинки', keyboard=keyboard)
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Хотите узнать больше информации об этой стране?', keyboard=keyboard)
            elif answer == 'Да, я хочу узнать больше о Финляндии':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Население: 5,537,364<br>Площадь: 338,145 км^2', keyboard=keyboard)

            elif answer == 'Нет':
                send_answer(vk_session, 'user_id', event.user_id,
                            message='Отправьте мне страну Европы, у которой хотите узнать столицу(Пишите с большой буквы)',
                            keyboard=keyboard)

            elif answer == 'Закончить':
                send_answer(vk_session, 'user_id', event.user_id, message='До скорых встреч!', keyboard=keyboard)

            else:
                send_answer(vk_session, 'user_id', event.user_id, message='Будем считать, что я этого не видел',
                            keyboard=None)
