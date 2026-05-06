import os
import shutil
import random

import requests
from dotenv import load_dotenv
import telegram

from download_image import download_image


def publish_random_comic(last_comic_number, bot, chat_id):
    random_number = random.randint(1,last_comic_number)
    xkcd_url = f'https://xkcd.com/{random_number}/info.0.json'
    response = requests.get(xkcd_url)
    response.raise_for_status()
    data = response.json()

    image_url = data['img']
    message = data['alt']
    filename = 'comic_image.png'
    download_image(image_url, filename)
    file_path = os.path.join('images', filename)

    with open(file_path, 'rb') as f:
        bot.send_photo(
            chat_id=chat_id,
            photo=f,
            caption=message,
            timeout=60
        )

    shutil.rmtree('images')


def get_latests_comic_number():
    xkcd_url = "https://xkcd.com/info.0.json"
    response = requests.get(xkcd_url)
    data = response.json()
    latest_comic = data['num']
    return latest_comic


def main():
    load_dotenv()
    bot = telegram.Bot(token=os.environ['TELEGRAM_BOT_TOKEN'])
    chat_id = os.getenv("TELEGRAM_CHAT_ID")
    os.makedirs('images', exist_ok=True)
    latest_comic = get_latests_comic_number()
    publish_random_comic(latest_comic, bot, chat_id)


if __name__ == '__main__':
    main()