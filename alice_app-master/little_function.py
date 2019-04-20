import json
import random


def get_suggest(user_storage):
    if "suggest" in user_storage.keys():
        #for suggest in user_storage["suggest"]:
        #    suggest.append({"title": suggest, "hide": True})

        suggests = [{"title": suggest, "hide": True} for suggest in user_storage["suggest"]]
    else:
        suggests = []

    return suggests, user_storage


def read_data(name: str) -> dict:
    return json.load(open(name + ".json", encoding="utf-8"))


def message_return(response, user_storage, message):
    response.set_text(message)
    response.set_tts(message)
    buttons, user_storage = get_suggest(user_storage)
    response.set_buttons(buttons)
    return response, user_storage


def message_error(response, user_storage):
    message = random.choice(["Я тебя не поняла", "Не очень хорошо поняла, повтори, пожалуйста"])
    return message_return(response, user_storage, message)
