import requests
import re
import os
from dotenv import load_dotenv
from .models import TeleSettings

load_dotenv()

TOKEN = os.environ.get('TOKEN')


def send_telegram(name: str, phone: str):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_message)

        str_name = name if name else '-'

        text = re.sub('name', str_name, text)
        text = re.sub('phone', phone, text)
        req = f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={text}'
        try:
            requests.get(req)
        except:
            print('Ощибка отправки')



