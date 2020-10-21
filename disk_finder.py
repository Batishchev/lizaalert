
import time

# Начинаем чекать диски. Если не нашли, ставим таймаут и пробуем снова.

def disk_finder(chan):
    chan.send(('log', 'Инициализация'))
    time.sleep(1)
    chan.send(('log', 'Ищем диск'))
    time.sleep(1)
    chan.send(('disk', 'Z'))
    chan.send(('testcommand', 'testmessage'))
