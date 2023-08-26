import json
import os
import requests
from celery import shared_task
from main.models import Habit


@shared_task
def send_to_bot(*args, **kwargs):
    bot_token = os.getenv('TELEGRAM_TOKEN')
    chat_id = os.getenv('CHAT_ID')
    habit_id = json.loads(args[0])
    habit = Habit.objects.get(pk=habit_id)
    message_text = (f'Пора {habit.action} '
                    f'в {habit.place} '
                    f'в течение {habit.length}')
    api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': message_text
    }

    response = requests.post(api_url, data=data)

    if response.status_code == 200:
        print('Привычка отправлена в бот')
    else:
        print(f'Ошибка: {response.status_code} - {response.text}')
