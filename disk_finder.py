import os
import asyncio

def check_disk(d):
    os.path.exists(os.path.join(d + ':/', 'Garmin', 'GPX', 'Current'))

# Начинаем чекать диски. Если не нашли, ставим таймаут и пробуем снова.
class DiskFinder():

    _handlers = []

    last_disks = {}

    def find_disks(self):
        return {'C:', 'D:'}
        # return set([chr(x) + ':' for x in range(65, 91) if check_disk(chr(x))])

    def subscribe(self, handler):
        self._handlers.append(handler)

    async def monitor(self):
        loop = asyncio.get_running_loop()

        while True:
            disks = self.find_disks()

            if len(disks.difference(self.last_disks)) != 0:
                self.last_disks = disks
                for h in self._handlers:
                    loop.create_task(h(list(disks)))

            await asyncio.sleep(5)
