import requests
from .models import TeleSettings


def SendTelegram(tg_name, tg_phone):
    if TeleSettings.objects.get(pk=1):
        settings = TeleSettings.objects.get(pk=1)
        token = str(settings.tg_token)
        chat_id = str(settings.tg_chat)
        text = str(settings.tg_text)
        api = 'https://api.telegram.org/bot'
        method = api + token + '/sendMessage'

        if text.find('{') and text.find('}') and text.rfind('{') and text.rfind('}'):
            par_1 = text[0:text.find('{')]
            par_2 = text[text.find('}')+1:text.rfind('{')]
            par_3 = text[text.rfind('}')+1:-1]
            text_slise = par_1 + " "+ str(tg_name)+ par_2+ " "+ str(tg_phone) +par_3
        else:
            text_slise = text
        try:
            req = requests.post(method, data={
                'chat_id':chat_id,
                'text':text_slise
                })
        except:
            pass
        finally:
            if req.status_code != 200:
                print('Oшибка отправка ')
            elif req.status_code != 500:
                    print('Oшибка 500 ')
            else:
                print("Ok")
    else:
        pass
