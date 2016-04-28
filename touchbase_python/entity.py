import requests

class EntitySet():
    results = []
    next = ''
    previous = ''
    count = ''
    is_paginated = False

    def __init__(self, json):
        is_paginated = False if type(json) is list else True
        if is_paginated:
            self.results = json['results']
            self.next = json['next']
            self.previous = json['previous']
            self.count = json['count']
            self.is_paginated = is_paginated
        else:
            self.results = json


class Entity():
    URI = ''

    def __init__(self, client):
        self.CLIENT = client
        self.next_url = None

    def list(self, url=None):
        obj = {}
        if not url:
            url = self.CLIENT.get_url(self.URI)
        r = requests.get(url, headers=self.CLIENT.HEADERS)

        json = self.CLIENT.handle_response(r)
        is_paginated = False if type(json) is list else True
        if is_paginated:
            self.next_url = json['next'] if json['next'] else None

        entity_set = EntitySet(json)
        return entity_set

    def list_next(self):
        if self.next_url:
            return self.list(self.next_url)
        else:
            return self.list()

    def detail(self, pk):
        pk = str(pk)
        url = self.CLIENT.get_url(self.URI, pk)
        r = requests.get(url, headers=self.CLIENT.HEADERS)
        json = self.CLIENT.handle_response(r)
        return json
