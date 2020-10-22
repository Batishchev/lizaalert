import os

def check_disk(d):
    # return True
    os.path.exists(os.path.join(d + ':/', 'Garmin', 'GPX', 'Current'))

def find_disks():
    # return ['C:', 'D:']
    return [chr(x) + ':' for x in range(65, 91) if check_disk(chr(x))]
