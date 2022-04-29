from json import JSONEncoder

class util_encoder(JSONEncoder):
    def default(self, obj):
        return obj.__dict__