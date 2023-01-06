import requests
import json
from os.path import dirname, join


class Request():
    def __init__(self):
        self.url = None
        self.headers = None
        self.data = None

    def to_json(self, key):
        self.headers[key] = json.dumps(self.headers[key])
        return self

    def get(self):
        return requests.get(url=self.url, headers=self.headers, data=self.data)

    def post(self):
        return requests.post(url=self.url, headers=self.headers, data=self.data)
    

class RequestBuilder:
    def __init__(self):
        self.request = Request()
        self.request.headers = {}
        self.request.headers['Authorization'] = 'sl.BWVtOook5wcYMlEIgMtFTHt8mpblYH1w9c_o17aTiiBhGh0Xl8Y-1t987FWi_sFwKlS88zKmewAORHpWjbs05SpkUEo8HvUbebM5IcVN6Ig_XVlNBX58oedRoiZwvp9cpEATYl0'

    def set_url(self, url):
        self.request.url = url
        return self

    def set_headers(self, headers):
        self.request.headers.update(headers)
        return self

    def set_data(self, data):
        self.request.data = data
        return self

    def build(self):
        return self.request


def upload_file():
    url = 'https://content.dropboxapi.com/2/files/upload'
    headers = {'Dropbox-API-Arg': {'autorename': False,
                                   'mode': 'overwrite',
                                   'mute': True,
                                   'path': '/cat.png',
                                   'strict_conflict': False},
               'Content-Type': 'application/octet-stream'}
    with open(join(dirname(__file__), 'cat.png'), 'rb') as file:
        data = file
        request = RequestBuilder() \
            .set_url(url) \
            .set_headers(headers) \
            .set_data(data) \
            .build()
        response = request.to_json('Dropbox-API-Arg').post()
        return response


def get_metadata():
    url = 'https://api.dropboxapi.com/2/files/get_metadata'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'include_deleted': False,
                       'include_has_explicit_shared_members': False,
                       'include_media_info': False,
                       'path': '/cat.png'})
    request = RequestBuilder() \
        .set_url(url) \
        .set_headers(headers) \
        .set_data(data) \
        .build()
    response = request.post()
    return response


def delete_file():
    url = 'https://api.dropboxapi.com/2/files/delete'
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({'path': '/cat.png'})
    request = RequestBuilder() \
        .set_url(url) \
        .set_headers(headers) \
        .set_data(data) \
        .build()
    response = request.post()
    return response