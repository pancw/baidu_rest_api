#!/usr/bin/env python
#coding=utf8

import base64
import requests

API_KEY = "YZlVOyVTlpopG13A8cmnN2eu"
SECRET_KEY = "c989613febf535b24e0387a4fcf2ec95"

#tokenUrl = "http://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_secret={api_key}&client_id={secret_key}".format(api_key=API_KEY, secret_key=SECRET_KEY)

result = requests.get('http://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_secret=c989613febf535b24e0387a4fcf2ec95&client_id=YZlVOyVTlpopG13A8cmnN2eu').json()

token = result["access_token"]
print result

#d = open('./voice.wav', 'rb').read()
d = open('./amr.txt', 'rb').read()

print len(d)

data = {
    "format": "amr",
    "rate": 8000,
    "channel": 1,
    "token": token, #"24.82ee3624056a96c898fa34f56ee3ad86.2592000.1482482296.282335-8939388",
    "cuid": "123",
    "len": len(d),
    "lan": "zh",
    "speech": base64.encodestring(d).replace('\n', '')
}
print requests.post('http://vop.baidu.com/server_api', json=data, headers={'Content-Type': 'application/json'}).text
