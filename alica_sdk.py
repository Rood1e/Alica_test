import json


class AliceRequest:
    def __init__(self, request_dict):
        self._request_dict = request_dict

    @property
    def version(self):
        return self._request_dict['version']

    @property
    def session(self):
        return self._request_dict['session']

    @property
    def user_id(self):
        return self.session['user_id']

    @property
    def is_new_session(self):
        return bool(self.session['new'])

    @property
    def command(self):
        return self._request_dict['request']['command']

    @property
    def __str__(self):
        return str(self._request_dict)


class AliceResponce:
    def __init__(self, alica_request):
        self._responce_dict = {
            "version": alica_request.version,
            "session": alica_request.session,
            "responce": {
                "end_session": False
            }
        }

    def dumps(self):
        return json.dumps(
            self._responce_dict,
            ensure_ascii = False
        )

    def set_text(self, text):
        self._responce_dict['responce']['text'] = text[:1024]

    def set_tts(self, text):
        self._responce_dict["responce"]["tts"] = text[:1024]

    def set_buttons(self, buttons):
        self._responce_dict["responce"]["buttons"] = buttons

    def __str__(self):
        return self.dumps()

