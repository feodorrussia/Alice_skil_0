import json, random, requests


def get_suggest(user_storage):
    if "suggests" in user_storage.keys():
        suggests = []
        for suggest in user_storage["suggests"]:
            suggests.append({"title": suggest, "hide": True})
    else:
        suggests = []
    return suggests, user_storage


def read_data(name: str) -> dict:
    return json.load(open(name + ".json", encoding='utf-8'))


def message_return(response, user_storage, message):
    response.set_text(message)
    response.set_tts(message)
    buttons, user_storage = get_suggest(user_storage)
    response.set_buttons(buttons)
    return response, user_storage


def message_error(response, user_storage, answer):
    message = random.choice(["Я тебя не поняла, повтори, пожалуйста.", "Повторите, пожалуйста."])#[]=answer
    return message_return(response, user_storage, message)
