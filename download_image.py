import os

import requests


def download_image(image_url, filename):
    image_response = requests.get(image_url)
    image_response.raise_for_status()
    file_path = os.path.join('images', filename)
    with open(file_path, "wb") as file:
        file.write(image_response.content)