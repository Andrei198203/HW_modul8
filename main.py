from datetime import datetime, timedelta


# Функція виведення
def get_birthdays_per_week(users):
    # Словник зберігання іменинників
    birthdays_by_day = {
        "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": [],
        "Saturday": [],
        "Sunday": []
    }

    # Поточна дата
    current_date = datetime.now()

    # День тижня
    current_weekday = current_date.strftime('%A')

    # Різниця між поточним днем і понеділком
    days_until_monday = (current_date.weekday() - 0) % 7

    # Дата наступного понеділка
    next_monday = current_date + timedelta(days=days_until_monday)

    # Додання користувачів до відповідних днів тижня
    for user in users:
        name = user['name']
        birthday = user['birthday']
        day_of_week = (next_monday + timedelta(days=(birthday.weekday() - 0) % 7)).strftime('%A')
        birthdays_by_day[day_of_week].append(name)

    # Вивод по днях тижня
    for day, names in birthdays_by_day.items():
        if names:
            print(f"{day}: {', '.join(names)}")


# Як використати
users = [
    {"name": "Sergii", "birthday": datetime(2023, 8, 28)},
    {"name": "Olga", "birthday": datetime(2023, 8, 29)},
    {"name": "Oleg", "birthday": datetime(2023, 8, 30)},
    {"name": "Yana", "birthday": datetime(2023, 8, 31)},
]

get_birthdays_per_week(users)
