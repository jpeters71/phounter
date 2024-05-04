from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from datetime import datetime, timedelta
from utils import setup_logger

import logging
import st7735
import sys


setup_logger()
logger = logging.getLogger(__name__)


def main():
    try: 
        disp = st7735.ST7735(
                port=0, 
                cs=st7735.BG_SPI_CS_BACK, 
                dc='GPIO24', 
                backlight='GPIO17', 
                rst='GPIO25', 
                width=128, 
                height=128, 
                rotation=90, 
                invert=False,
                spi_speed_hz=125_000_000,
                offset_top=1,
                offset_left=1,
            )

        WIDTH = disp.width
        HEIGHT = disp.height

        img = Image.new('RGB', (WIDTH, HEIGHT), (0, 0, 0))
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf', size=10)

        start_dt = datetime.now()
        while True:
            curr_dt = datetime.now()
            if curr_dt > (start_dt + timedelta(seconds=1)):
                draw.rectangle([(0,0), (128,11)], fill=(0, 0, 0), outline=(0,0,0))
                draw.text((0, 0), f'Time: {curr_dt.strftime("%H:%M:%S")}', font=font, fill=(255, 255, 255))
                logger.info(f'Logging time: {curr_dt}')
                start_dt = curr_dt
                disp.display(img)


    except Exception as e:
        print(f'ERROR: {e}')
        logger.exception('Exception!')



if __name__ == '__main__':
    main()

