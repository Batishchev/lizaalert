import sys
from multiprocessing import Pipe, Process
from disk_finder import disk_finder

def main():
    printer = Printer()
    a, b = Pipe()

    p = Process(target=disk_finder, args=(b,))
    p.start()

    while True:
        (command, message) = a.recv()

        if command == 'log':
            printer.print(message)
            # Пока нет нового сообщения от disk_finder-a
            while not a.poll(1):
                printer.print(message)
            print('')
            continue

        elif command == 'disk':
            print('Нашли диск ' + message + '\n')

            print('1. Копируем карты')
            print('2. Копируем трэки')
            print('3. Ещё что-нибудь')

            print(input('Что делаем: '))

        else:
            print('Необработанная команда (' + command + ', ' + message + ')')

# Класс просто дописывает три точки к логу
class Printer:
    min = 0
    max = 3

    value = min

    def print(self, data):
      sys.stdout.write("\r" + data + ("." * self.value) + (" " * (self.max - self.value)))
      sys.stdout.flush()
      self._inc()

    def _inc(self):
        self.value += 1
        if self.value > 3:
            self.value = self.min

main()
