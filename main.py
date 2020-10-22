import sys
from disk_finder import *
from operations import *

def main():
    print()
    print('1 - Очистить старые карты')
    print('q - Выход')

    task = input('\nВыберите операцию: ')

    if task == 'q' or task == 'Q':
        return

    elif task == '1':
        disk = select_disk(find_disks())

        if not disk:
            print('Не нашли диск')
        else:
            clean_old(disk)

    main()

def select_disk(disks):
    if len(disks) == 1:
        return disks[0]
    elif len(disks) > 1:
        print('\nНашли диски %a' % disks)
        disk = input('Введите букву диска, или q для пропуска ( %s ): ' % disks[0][0]).upper()

        if disk == 'Q':
            return None
        elif disk == '':
            return disks[0]
        elif check_disk(disk):
            return disk
        else:
            print('Неверный диск')
            return select_disk(disks)

main()
