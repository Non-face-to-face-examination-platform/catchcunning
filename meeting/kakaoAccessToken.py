import requests
import json

url = 'https://kauth.kakao.com/oauth/token'
client_id = '5150e927350491eae8a6f52e4a81c17f'
redirect_uri = 'https://example.com/oauth'
code = 'qeW907Pscxzck_KBY1VJUd-aZOcZxtIzjRlrGm31HZk3DIC-hvqgdPF26PPOUTffvOSH8Ao9dNkAAAGC19zKwA'


data = {
    'grant_type':'refresh_token',
    'client_id':client_id,
    "refresh_token": "O803VY7wCx-4ZhDE6sNUifwmA3A3NZgIRBdlnUruCj10EQAAAYMHcnSA"
    }

response = requests.post(url, data=data)
tokens = response.json()

#발행된 토큰 저장
with open("token.json","w") as kakao:
    json.dump(tokens, kakao)