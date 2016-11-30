#!/usr/bin/env python
#coding=utf8

import base64
import requests

result = requests.get('http://openapi.baidu.com/oauth/2.0/token?grant_type=client_credentials&client_secret=c989613febf535b24e0387a4fcf2ec95&client_id=YZlVOyVTlpopG13A8cmnN2eu').json()

token = result["access_token"]
print result

#d = open('./voice.wav', 'rb').read()
d = open('./amr.txt', 'rb').read()

data = {
    "format": "amr",
    "rate": 8000,
    "channel": 1,
    "token": token,
    "cuid": "123",
    "len": len(d),
    "lan": "zh",
    "speech": base64.encodestring(d).replace('\n', '')
}
print requests.post('http://vop.baidu.com/server_api', json=data, headers={'Content-Type': 'application/json'}).text
