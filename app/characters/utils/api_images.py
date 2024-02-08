import asyncio
import base64
import json
import aiohttp
import requests
from os import getenv
from dotenv import load_dotenv
from app.config import images_dir


load_dotenv()

API_KEY = getenv('API_KEY')
SECRET_KEY = getenv('SECRET_KEY')

class Text2ImageAPI:
    """API для использования генерации картинок Сбера"""

    def __init__(self, api_key, secret_key):
        self.URL = 'https://api-key.fusionbrain.ai/'
        self.model_url = 'key/api/v1/models'
        self.generate_url = 'key/api/v1/text2image/run'
        self.status_url = 'key/api/v1/text2image/status/'
        self.AUTH_HEADERS = {
            'X-Key': f'Key {api_key}',
            'X-Secret': f'Secret {secret_key}',
        }

    def get_model(self):
        """Возврат: id рабочей модели Сбера"""

        response = requests.get(self.URL + self.model_url, headers=self.AUTH_HEADERS)
        data = response.json()
        return data[0]['id']

    def generate(self,
                 prompt: dict,
                 model: int,
                 images: int = 1,
                 width: int = 1024,
                 height: int = 1024) -> str:
        """Делает запрос на генерацию картинки
            Возврат: uuid - для запросов о состоянии картинки
        """
        prompt = prompt.copy()
        prompt.pop('card_1')
        prompt.pop('card_2')
        prompt.pop('image')
        prompt = ', '.join([i for i in prompt.values()])

        params = {
            "type": "GENERATE",
            "numImages": images,
            "width": width,
            "height": height,
            "generateParams": {
                "query": f"{prompt}"
            }
        }
        data = {
            'model_id': (None, model),
            'params': (None, json.dumps(params), 'application/json')
        }
        response = requests.post(self.URL + self.generate_url, headers=self.AUTH_HEADERS, files=data)
        data = response.json()
        return data['uuid']

    async def check_generation(self, uuid: str, image_name: str) -> None:
        """Запросы проверки состояния генерации по uuid"""
        attempts = 10
        while attempts > 0:
            async with aiohttp.ClientSession(headers=self.AUTH_HEADERS) as session:
                async with session.get(self.URL + self.status_url + uuid) as response:
                    data = await response.json()

            if data['status'] == 'DONE':
                image_base64 = data['images'][0]
                image_data = base64.b64decode(image_base64)

                # Открываем файл для записи бинарных данных изображения
                try:
                    with open(images_dir + fr"\{image_name}.jpg", "wb") as file:
                        file.write(image_data)
                        return
                except:
                    return

            await asyncio.sleep(5)
            attempts += 1


async def run_generate(prompt: dict, image_name: str):
    api = Text2ImageAPI(API_KEY, SECRET_KEY)
    model = api.get_model()
    uuid = api.generate(prompt, model)
    await api.check_generation(uuid, image_name)
    return prompt

# async def run_generate(prompt: dict, image_name: str):
#     await main(prompt, image_name)