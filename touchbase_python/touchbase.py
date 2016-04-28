import requests
from visualize import Media
from uploadify import Filezilla
from blogify import Post

class Client():
    TOKEN = None
    HEADERS = {}
    ROOT_URL = 'http://app.touchbase.se/'
    API_URL = ROOT_URL + 'api/v1/'
    AUTH_URL = ROOT_URL + 'api-token-auth/'

    def __init__(self):
        self.media = Media(self)
        self.filezilla = Filezilla(self)
        self.post = Post(self)
        print 'Hello, I am client'

    def authenticate(self, username, password):
        params = {
            'username': username,
            'password': password
        }
        r = requests.post(self.AUTH_URL, data=params)
        json = self.handle_response(r)
        if json:
            self.TOKEN = json.get('token')
            self.HEADERS['Authorization'] = 'Bearer %s' % self.TOKEN

    def handle_response(self, response):
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 401:
            print 'Unauthorized'
        elif response.status_code == 403:
            print 'Forbidden'
        elif response.status_code == 404:
            print 'Not Found'
        else:
            print response.status_code
        return None

    def get_url(self, uri, pk=None):
        if pk:
            url = self.API_URL + uri + pk
        else:
            url = self.API_URL + uri
        print url
        return url
