import json


def get_button(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


start_keyboard = {
    "one_time": True,
    "buttons": [
        [get_button("help", "secondary")]
    ]
}
second_keyboard = {
    "one_time": True,
    "buttons": [
        [get_button("следующий профиль", "positive")],
        [get_button("добавить в избранное", "positive"), get_button("список избранных", "positive")],
        [get_button("изменить поисковые данные", "primary"), get_button("help", "primary")],
        [get_button("Добавить в черный список", "negative")]
    ]
}
start_keyboard = json.dumps(start_keyboard, ensure_ascii=False).encode("utf-8")
start_keyboard = str(start_keyboard.decode("utf-8"))
second_keyboard = json.dumps(second_keyboard, ensure_ascii=False).encode("utf-8")
second_keyboard = str(second_keyboard.decode("utf-8"))

how_search_message = """Введите данные в формате 'поиск город пол возраст от\до'
                    Пример ввода: 'Поиск Москва женский 18 25'
                    Для разделения используйте только пробел, в конце его использовать не нужно.
                    Проверьте введенные данные если вы не получили результат"""
error_message = {
    "name_error": """Сначала нужно ввести данные для поиска
                 Введите 'help' если не знакомы с навигацией бота""",
    "key_error": """Данные введены некорректно
                    Введите 'help' если не знакомы с навигацией бота"""
}

bot_messages = {
    "help": """КОМАНДА HELP
                
                Для начала нужно ввести поисковые данные:
                МЕТОД: "Поиск <город> <пол> <возраст от> < возраст до>"
                пол = женский, мужской, любой
                возраст = любые цифровые значения
                город = используйте название города, а не индекс
                
                 ПРИМЕР ВВОДА: "Поиск Москва женский 18 25"
                 
                 Используйте только пробел для разделения.
                 Вначале и в конце предложения пробел использовать не нужно
                 
                 После найденного пользователя используйте кнопки навигаций:
                 Следующий пользователь - Будет выдавать вам поочередно следующий
                 профиль по вашим критериям. Используйте после введенных данных
                 для поиска
                 Добавить в избранное - используйте на последнем найденном профиле
                 если хотите добавить его в ваш список фаворитов. 
                 А команда "список избранных" выдаст вам текущий список
                 Добавить в черный список - если вы больше не хотите что бы данный
                 профиль выходил вам в рекомендации
                 
                """,
    "начать": """Введите данные в формате 'поиск город пол возраст от\до'
                    Пример ввода: 'Поиск Москва женский 18 25'
                    Для разделения используйте только пробел, в конце его использовать не нужно.
                    Проверьте введенные данные если вы не получили результат.
                    Введите 'help' для более подробной инструкции """

}
