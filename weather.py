import requests
from PIL import Image
from io import BytesIO
from datetime import datetime, timedelta

# Словарь символов ASCII-арт для каждой иконки погоды
weather_icons = {
    '01d': '☀️',  # ясно
    '01n': '🌙',  # ясно (ночь)
    '02d': '⛅',  # малооблачно
    '02n': '🌙⛅',  # малооблачно (ночь)
    '03d': '☁️',  # облачно
    '03n': '🌙☁️',  # облачно (ночь)
    '04d': '☁️☁️',  # пасмурно
    '04n': '🌙☁️☁️',  # пасмурно (ночь)
    '09d': '🌧️',  # легкий дождь
    '09n': '🌙🌧️',  # легкий дождь (ночь)
    '10d': '🌦️',  # дождь
    '10n': '🌙🌦️',  # дождь (ночь)
    '11d': '⛈️',  # гроза
    '11n': '🌙⛈️',  # гроза (ночь)
    '13d': '🌨️',  # снег
    '13n': '🌙🌨️',  # снег (ночь)
    '50d': '🌫️',  # туман
    '50n': '🌙🌫️',  # туман (ночь)
}

# Словарь описаний погоды
weather_descriptions = {
    '01d': 'Ясное небо',
    '01n': 'Ясное небо',
    '02d': 'Малооблачно',
    '02n': 'Малооблачно',
    '03d': 'Облачно',
    '03n': 'Облачно',
    '04d': 'Пасмурно',
    '04n': 'Пасмурно',
    '09d': 'Легкий дождь',
    '09n': 'Легкий дождь',
    '10d': 'Дождь',
    '10n': 'Дождь',
    '11d': 'Гроза',
    '11n': 'Гроза',
    '13d': 'Снег',
    '13n': 'Снег',
    '50d': 'Туман',
    '50n': 'Туман',
}

# Программа работает, пока пользователь вводит команды
while True:
    input_string = input("Введите название города, если хотите узнать текущий прогноз\nДобавьте слово 'Завтра', если хотите узнать погоды на завтра\nВведите '!' для выхода: ")
    
    # Завершение работы по нажатию !
    if input_string == '!':
        break

    parts = input_string.split(' ')
    city = parts[0]
    forecast_tomorrow = False
    
    # Поступает команда для прогноза на завтра
    if len(parts) > 1 and parts[1].lower() == 'завтра':
        forecast_tomorrow = True

    if forecast_tomorrow:
        # Получение даты завтрашнего дня
        tomorrow = datetime.now() + timedelta(days=1)
        date_str = tomorrow.strftime('%Y-%m-%d')
        # Прогноз на завтра
        url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    else:
        # Прогноз на сегодня
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    
    # Запрос на получение прогноза
    response = requests.get(url)

    if response.status_code == 200:
        weather_data = response.json()
        
        # Если пользователь запрашивает прогноз на завтра
        if forecast_tomorrow:
            forecast = None
            for item in weather_data['list']:
                if item['dt_txt'].startswith(date_str):
                    forecast = item
                    break

            if forecast is None:
                print('Прогноз на завтра для данного города не найден.')
                continue

            temperature = round(forecast['main']['temp'])
            temperature_feels = round(forecast['main']['feels_like'])
            wind_speed = round(forecast['wind']['speed'])
            icon_code = forecast['weather'][0]['icon']
        else:
            temperature = round(weather_data['main']['temp'])
            temperature_feels = round(weather_data['main']['feels_like'])
            wind_speed = round(weather_data['wind']['speed'])
            icon_code = weather_data['weather'][0]['icon']

        print()
        print(f'Погода для населенного пункта {city}:')
        print('Температура:', str(temperature), '°C')
        print('Ощущается как', str(temperature_feels), '°C')
        print(f'Скорость ветра {wind_speed} м/с')

        if icon_code in weather_icons:
            icon = weather_icons[icon_code]
            print('Погодные условия:', icon, weather_descriptions.get(icon_code, ''))
        else:
            print('Погодные условия:', icon_code)

        print()
    else:
        print('Ошибка при получении данных о погоде. Пожалуйста, попробуйте еще раз.')