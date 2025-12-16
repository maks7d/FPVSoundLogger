import uasyncio as asyncio
from lib.fpv_sound_logger import FpvSoundLogger

async def main():
    fpv = FpvSoundLogger()
    fpv.start()    
    while True:
        await asyncio.sleep(1)

asyncio.run(main())