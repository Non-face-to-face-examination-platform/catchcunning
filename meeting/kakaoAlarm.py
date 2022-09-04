import json
from signal import alarm
import requests
import sys
 

def sendToMeMessage(text):

    header = {"Authorization": 'Bearer ' + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send" #나에게 보내기 주소

    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },

        "button_title": "바로 확인"
    }
    data = {"template_object": json.dumps(post)}
    return requests.post(url, headers=header, data=data)

alarm = ""
for arg in sys.argv:
    alarm += (str(arg))
    

message = alarm.replace("meeting/kakaoAlarm.py", "")


# alarm = sys.argv[1]

# if len(sys.argv) != 2:
#     print("Insufficient arguments")
#     sys.exit()



text = "나에게 보내는 카톡: " + message
KAKAO_TOKEN = '0xq_Ag6t2tvVSej9tdSieMF8_yYBRbhnx83QGizoCil1KQAAAYMHcEif'

print(sendToMeMessage(text).text)


# import requests
# import json

# url = 'https://kauth.kakao.com/oauth/token'
# client_id = '5150e927350491eae8a6f52e4a81c17f'
# redirect_uri = 'https://example.com/oauth'
# code = 'qeW907Pscxzck_KBY1VJUd-aZOcZxtIzjRlrGm31HZk3DIC-hvqgdPF26PPOUTffvOSH8Ao9dNkAAAGC19zKwA'

# data = {
#     'grant_type':'authorization_code',
#     'client_id':client_id,
#     'redirect_uri':redirect_uri,
#     'code': code,
#     }

# response = requests.post(url, data=data)
# tokens = response.json()

# #발행된 토큰 저장
# with open("token.json","w") as kakao:
#     json.dump(tokens, kakao)
