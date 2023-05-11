TOKEN = '6144629941:AAHu5Jn1q0w4nE7jGpbr9exlA3s-bmZMOWA'

URL = 'https://api.telegram.org/bot{token}/{method}'


UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'
MY_ID = 1056661144

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data

WEATHER_TOKEN = 'd4f86ed273bcae90937826aa76f834fe'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'
