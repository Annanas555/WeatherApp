import requests

while True:
    city = input("Введите название города (или введите '!' для выхода): ")
    
    if city == '!':
        break
    
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        weather_data = response.json()
        temperature = round(weather_data['main']['temp'])
        temperature_feels = round(weather_data['main']['feels_like'])
        wind_speed = round(weather_data['wind']['speed'])
        
        print()
        print(f'Погода для населенного пункта {city}:')
        print('Сейчас', str(temperature), '°C')
        print('Ощущается как', str(temperature_feels), '°C')
        print(f'Скорость ветра {wind_speed} м/с')
        print()
    else:
        print('Ошибка при получении данных о погоде. Пожалуйста, попробуйте еще раз.')
