import os
import shutil
import random

import requests
from dotenv import load_dotenv
import telegram

from download_image import download_image


def get_latest_comic_number():
    xkcd_url = "https://xkcd.com/info.0.json"
    response = requests.get(xkcd_url)
    latest_comic = response.json()['num']
    return latest_comic


def get_random_comic(latest_comic):
    random_number = random.randint(1, latest_comic)
    xkcd_url = f'https://xkcd.com/{random_number}/info.0.json'
    response = requests.get(xkcd_url)
    response.raise_for_status()
    return xkcd_url


def get_comic_info(xkcd_url):
    response = requests.get(xkcd_url)
    response.raise_for_status()
    xkcd_data = response.json()
    image_url = xkcd_data['img']
    message = xkcd_data['alt']
    return image_url, message


def publish_comic(bot, chat_id, filename, message):
    file_path = os.path.join('images', filename)

    with open(file_path, 'rb') as f:
        bot.send_photo(
            chat_id=chat_id,
            photo=f,
            caption=message,
            timeout=60
        )


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    chat_id = os.getenv("TELEGRAM_CHAT_ID")

    os.makedirs('images', exist_ok=True)

    try:
        latest_comic = get_latest_comic_number()
        xkcd_url = get_random_comic(latest_comic)
        image_url, message = get_comic_info(xkcd_url)
        filename = 'comic_image.png'
        download_image(image_url, filename)
        publish_comic(bot, chat_id, filename, message)
    finally:
        if os.path.exists('images'):
            shutil.rmtree('images')


if __name__ == '__main__':
    main()
