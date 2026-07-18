import json


class ResponseParser:

    def parse(self, response):

        return json.loads(response)
