import sys
import time
import asyncio
from multiprocessing import Pipe
from disk_finder import DiskFinder
import operations

class Main():
    available_disks = []
    current_disk = ''

    def __init__(self):
        self.disk_finder = DiskFinder()

    def main(self):
        while True:
            available_disks = self.disk_finder.disks

            print(available_disks)

            time.sleep(1)

            if len(available_disks) <= 0:
                continue
            elif len(available_disks) == 1:
                self.current_disk = available_disks[0]
            else:
                self.current_disk = available_disks[0]



Main().main()

# async def disk_found(disks):
#     [disk, *_] = disks
#
#     if len(disks) == 1:
#         print('Нашли диск %s \n' % disk)
#     else:
#         print('Нашли диски %a \n' % disks)
#
#         disk = input('Введите букву диска, или q для пропуска: ')
#
#         if disk == 'q':
#             return
#         elif not check_disk(disk):
#             print('Неверный диск')
#             return await disk_found(disks)
#
#     print('1. Очистить старые карты')
#
#     task = input('Что делаем: ')
#
#     if task == '1':
#         print('Очищено')
#
# asyncio.run(main())
