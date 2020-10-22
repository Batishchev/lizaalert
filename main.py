import sys
import asyncio
from multiprocessing import Pipe, Process
from disk_finder import DiskFinder, check_disk
import operations

async def main():
    loop = asyncio.get_running_loop()

    disk_finder = DiskFinder()
    disk_finder.subscribe(disk_found)
    await loop.create_task(disk_finder.monitor())

async def disk_found(disks):
    [disk, *_] = disks

    if len(disks) == 1:
        print('Нашли диск %s \n' % disk)
    else:
        print('Нашли диски %a \n' % disks)

        disk = input('Введите букву диска, или q для пропуска: ')

        if disk == 'q':
            return
        elif not check_disk(disk):
            print('Неверный диск')
            return await disk_found(disks)

    print('1. Очистить старые карты')

    task = input('Что делаем: ')

    if task == '1':
        print('Очищено')

asyncio.run(main())
