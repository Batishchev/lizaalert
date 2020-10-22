import os
import glob
import shutil
import zipfile
import pathlib

def clean_old(disk):
    print('Чистим диск %s' % disk)
    to_remove = glob.glob(
        os.path.join(disk + ':/', 'Garmin', 'GPX', '*.gpx')
    ) + glob.glob(
        os.path.join(disk + ':/', 'Garmin', 'CustomMaps', '*.kmz')
    ) + glob.glob(
        os.path.join(disk + ':/', 'Garmin', 'BirdsEye', '*.jnx')
    )

    for f in to_remove:
        try:
            print('Удаляем %s' % f)
            # os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

def copy_new(disk):
    if not os.path.exists('new_maps'):
        new_maps = glob.glob('*.zip')

        if len(new_maps) == 0:
            print('Не смогли найти архив с картами')
            return

        with zipfile.ZipFile(new_maps[0], 'r') as zip_ref:
            zip_ref.extractall('new_maps')

    target_gpx = pathlib.Path(disk + ':/', 'Garmin', 'GPX')
    target_gpx.mkdir(parents=True, exist_ok=True)
    for f in glob.glob(os.path.join('new_maps', 'Garmin', 'GPX', '*.gpx')):
        print('Копируем %s' % f)
        shutil.copy(f, target_gpx)

    target_kmz = pathlib.Path(disk + ':/', 'Garmin', 'CustomMaps')
    target_kmz.mkdir(parents=True, exist_ok=True)

    source_kmz = glob.glob(os.path.join('new_maps', 'Garmin', 'CustomMaps', '*.kmz'))
    while len(source_kmz) > 1:
        print('Нашли несколько kmz')
        for i in range(len(source_kmz)):
            print('%i - %s' % (i+1, source_kmz[i]))

        try:
            index = int(input('Выберите нужный kmz: '))

            if index < 1 or index > len(source_kmz):
                continue

            source_kmz = [source_kmz[index-1]]
        except:
            continue
    source_kmz = source_kmz[0]
    print('Копируем %s' % source_kmz)
    shutil.copy(source_kmz, target_kmz)

    target_jnx = pathlib.Path(disk + ':/', 'Garmin', 'BirdsEye')
    target_jnx.mkdir(parents=True, exist_ok=True)
    for f in glob.glob(os.path.join('new_maps', 'Garmin', 'BirdsEye', '*.jnx')):
        print('Копируем %s' % f)
        shutil.copy(f, target_jnx)
