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
            print(f)
            # os.remove(f)
        except OSError as e:
            print("Error: %s : %s" % (f, e.strerror))

def copy_new():
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
        shutil.copy(f, target_gpx)

    target_kmz = pathlib.Path(disk + ':/', 'Garmin', 'CustomMaps')
    target_kmz.mkdir(parents=True, exist_ok=True)
    for f in glob.glob(os.path.join('new_maps', 'Garmin', 'CustomMaps', '*.kmz')):
        shutil.copy(f, target_kmz)

    target_jnx = pathlib.Path(disk + ':/', 'Garmin', 'BirdsEye')
    target_jnx.mkdir(parents=True, exist_ok=True)
    for f in glob.glob(os.path.join('new_maps', 'Garmin', 'BirdsEye', '*.jnx')):
        shutil.copy(f, target_jnx)
