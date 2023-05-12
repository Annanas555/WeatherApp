<h1>Приложение для получения погоды</h1>
<p>Это простое приложение позволяет получить информацию о погоде для заданного города, используя API сервиса OpenWeatherMap. Вы можете получить текущий прогноз погоды или прогноз на завтра.</p>
<h2>Установка</h2>
<ol>
  <li>Склонируйте репозиторий с помощью следующей команды:</li>
  <pre><code>git clone https://github.com/your-username/WeatherApp.git</code></pre>
  <li>Перейдите в каталог проекта:</li>
  <pre><code>cd WeatherApp</code></pre>
  <li>Установите зависимости, выполнив следующую команду:</li>
  <pre><code>pip install requests pillow</code></pre>
</ol>
<h2>Использование</h2>
<ol>
  <li>Запустите программу с помощью следующей команды:</li>
  <pre><code>python weather.py</code></pre>
  <li>Введите название города, для которого вы хотите получить погоду. Чтобы выйти из программы, введите символ '!'.</li>
  <li>Если вы хотите узнать текущий прогноз погоды, просто введите название города (например, "Москва"). Программа выведет текущую температуру, ощущаемую температуру и скорость ветра.</li>
  <li>Если вы хотите узнать прогноз погоды на завтра, добавьте слово "Завтра" после названия города (например, "Москва Завтра"). Программа выведет прогноз на завтра, включая температуру, ощущаемую температуру и скорость ветра.</li>
</ol>
<h2>Примеры команд</h2>
<ul>
  <li>Москва - получить текущий прогноз погоды для Москвы.</li>
  <li>Санкт-Петербург Завтра - получить прогноз погоды на завтра для Санкт-Петербурга.</li>
  <li>! - выйти из программы.</li>
</ul>
<h2>Отображение погодных условий</h2>
<p>При выводе прогноза погоды программа будет отображать иконку, соответствующую текущим погодным условиям. Вот некоторые из используемых иконок:</p>
<ul>
  <li>☀️ - ясно</li>
  <li>🌙 - ясно (ночь)</li>
  <li>⛅ - малооблачно</li>
  <li>🌙⛅ - малооблачно (ночь)</li>
  <li>☁️ - облачно</li>
  <li>🌙☁️ - облачно (ночь)</li>
  <li>☁️☁️ - пасмурно</li>
  <li>🌙☁️☁️ - пасмурно (ночь)</li>
  <li>🌧️ - легкий дождь</li>
  <li>🌙🌧️ - легкий дождь (ночь)</li>
  <li>🌦️ - дождь</li>
  <li>🌙🌦️ - дождь (ночь)</li>
  <li>⛈️ - гроза</li>
  <li>🌙⛈️ - гроза (ночь)</li>
  <li>🌨️ - снег</li>
  <li>🌙🌨️ - снег (ночь)</li>
  <li>🌫️ - туман</li>
  <li>🌙🌫️ - туман (ночь)</li>
</ul>
<p>Приложение также будет выводить текстовое описание погоды на основе полученных данных.</p>
<h2>Примеры использования</h2>

![image](https://github.com/Annanas555/WeatherApp/assets/128131401/a03a0b0b-0792-4256-9ca5-c2fe9b1d0247)

![image](https://github.com/Annanas555/WeatherApp/assets/128131401/024962b7-3135-4512-8142-2166cd456ee4)

<p>Теперь приложение для получения погоды имеет новые функции, включая прогноз погоды на завтра и отображение погодных иконок и описаний. Пользуйтесь им с удовольствием!</p>
