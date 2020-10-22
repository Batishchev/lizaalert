import os
import glob
import shutil
import zipfile
import pathlib

def get_free_archive_path():
    archive = pathlib.Path('archive')
    archive.mkdir(parents=True, exist_ok=True)
    all_archives = [f for f in os.listdir(archive) if os.path.isdir(os.path.join(archive, f))]
    all_archives.sort()
    all_archives.reverse()

    index = 0
    for f in all_archives:
        try:
            index = int(f) + 1
            break
        except:
            continue

    result = pathlib.Path(archive, str(index))
    result.mkdir(parents=True, exist_ok=True)
    return result

def clean_old(disk):
    archive = get_free_archive_path()
    print('Сохраняем диск %s в архив %s' % (disk, archive))

    pathlib.Path(archive, 'GPX').mkdir(parents=True, exist_ok=True)
    for f in glob.glob(os.path.join(disk + ':/', 'Garmin', 'GPX', '*.gpx')):
        try:
            print('Архивируем %s' % f)
            shutil.move(f, os.path.join(archive, 'GPX'))
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    pathlib.Path(archive, 'CustomMaps').mkdir(parents=True, exist_ok=True)
    for f in glob.glob(os.path.join(disk + ':/', 'Garmin', 'CustomMaps', '*.kmz')):
        try:
            print('Архивируем %s' % f)
            shutil.move(f, os.path.join(archive, 'CustomMaps'))
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

    pathlib.Path(archive, 'BirdsEye').mkdir(parents=True, exist_ok=True)
    for f in glob.glob(os.path.join(disk + ':/', 'Garmin', 'BirdsEye', '*.jnx')):
        try:
            print('Архивируем %s' % f)
            shutil.move(f, os.path.join(archive, 'BirdsEye'))
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))


def copy_new(disk):
    # Распаковываем архив, если ещё не распаковали
    if os.path.exists('new_maps') and os.path.isdir('new_maps'):
        shutil.rmtree('new_maps')

    new_maps = glob.glob('*.zip')

    if len(new_maps) == 0:
        print('Не смогли найти архив с картами')
        return

    while len(new_maps) > 1:
        print('\nНашли несколько zip архивов')
        for i in range(len(new_maps)):
            print('%i - %s' % (i+1, new_maps[i]))
        print('0 - пропустить')
        try:
            index = int(input('Выберите нужный zip: '))

            if index == 0:
                return

            if index < 1 or index > len(new_maps):
                continue

            new_maps = [new_maps[index-1]]
            break
        except:
            continue

    with zipfile.ZipFile(new_maps[0], 'r') as zip_ref:
        zip_ref.extractall('new_maps')

    # Копируем GPX
    target_gpx = pathlib.Path(disk + ':/', 'Garmin', 'GPX')
    target_gpx.mkdir(parents=True, exist_ok=True)
    for f in glob.glob(os.path.join('new_maps', 'Garmin', 'GPX', '*.gpx')):
        print('Копируем %s' % f)
        shutil.copy(f, target_gpx)

    target_kmz = pathlib.Path(disk + ':/', 'Garmin', 'CustomMaps')
    target_kmz.mkdir(parents=True, exist_ok=True)

    # Копируем KMZ
    source_kmz = glob.glob(os.path.join('new_maps', 'Garmin', 'CustomMaps', '*.kmz'))
    while len(source_kmz) > 1:
        print('\nНашли несколько kmz')
        for i in range(len(source_kmz)):
            print('%i - %s' % (i+1, source_kmz[i]))
        print('0 - пропустить')

        try:
            index = int(input('Выберите нужный kmz: '))

            if index == 0:
                source_kmz = []
                break

            if index < 1 or index > len(source_kmz):
                continue

            source_kmz = [source_kmz[index-1]]
            break
        except:
            continue

    for f in source_kmz:
        print('Копируем %s' % f)
        shutil.copy(f, target_kmz)

    # Копируем JNX
    target_jnx = pathlib.Path(disk + ':/', 'Garmin', 'BirdsEye')
    target_jnx.mkdir(parents=True, exist_ok=True)
    for f in glob.glob(os.path.join('new_maps', 'Garmin', 'BirdsEye', '*.jnx')):
        print('Копируем %s' % f)
        shutil.copy(f, target_jnx)

    if os.path.exists('new_maps') and os.path.isdir('new_maps'):
        shutil.rmtree('new_maps')
