import os
import asyncio
from multiprocessing import Pipe, Process, Manager
import time

REFRESH_TIME = 5

def check_disk(d):
    os.path.exists(os.path.join(d + ':/', 'Garmin', 'GPX', 'Current'))

class DiskFinder():

    def __init__(self):
        self._manager = Manager()
        self.disks = self._manager.list()
        self._process = Process(target=self._main)
        self._process.start()

    def _main(self):
        asyncio.run(self._main_async())

    async def _main_async(self):
        await self._monitor()

    def _find_disks(self):
        return ['C:', 'D:']
        # return [chr(x) + ':' for x in range(65, 91) if check_disk(chr(x))]

    async def _monitor(self):
        while True:
            del self.disks[:]
            self.disks.extend(self._find_disks())

            await asyncio.sleep(REFRESH_TIME)
