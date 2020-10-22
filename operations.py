import os
import glob

def clean_old(disk):
    print('clearing %s' % disk)
    # to_remove =
    #     glob.glob(os.path.join(disk + ':/', 'Garmin', 'GPX', '*.gpx') +
    #     glob.glob(os.path.join(disk + ':/', 'Garmin', 'CustomMaps', '*.kmz') +
    #     glob.glob(os.path.join(disk + ':/', 'Garmin', 'BirdsEye', '*.jnx')
#
    # for f in to_remove:
    #     try:
    #         os.remove(f)
    #     except OSError as e:
    #         print("Error: %s : %s" % (f, e.strerror))
