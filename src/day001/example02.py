import pyowm

owm = pyowm.OWM('ac283ed212edc804f743e6ffee842458')
city = input('Какой город Вас интересует?: ')

observation = owm.weather_at_place(city)
w = observation.get_weather()
temp = w.get_temperature('celsius')['temp']

print("В городе " + city + " сейчас температура: " + str(temp) + " градусов по Цельсию.")