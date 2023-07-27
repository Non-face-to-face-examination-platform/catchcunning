![image](https://github.com/Non-face-to-face-examination-platform/catchcunning/assets/102767676/4b5007af-f198-476e-9cae-2660e067b474)# SW개발보안 경진대회(소개딩 해커톤)

# 비대면 시험 응시 플랫폼 ‘Catch Cunning’

노션에서 읽으시고 싶으시다면 -> [Catch Cunning in Notion](https://www.notion.so/readme-fa3486fa7ee74676a9f6f260317dfa71)

#### 소개딩 수상 기사
- ![Article](https://www.etnews.com/20220901000170)
- ![학과 소식](https://cse.yu.ac.kr/cse/community/news.do?mode=view&articleNo=6814205&article.offset=0&articleLimit=10)


## 1. 아이디어 소개

비대면 면접, 회의, 시험 등이 COVID-19 감염병으로 인해 사용이 많이 되었고, 아직까지도 그 편리함으로 인해 사용되고 있다. 그러나, 편리함의 이면에는 대면 시험과 달리 감독관이 부정행위를 탐지하고 여러 응시자의 화면을 지켜보는 것이 힘들다는 단점이 있다.
이러한 문제를 해결하기 위해 우리는 부정행위를 차단하고, 인공지능의 사용을 통해 감독관의 화면을 보조하여 시험 감독을 효율적으로 할 수 있는 비대면 시험 응시 플랫폼, ‘Catch Cunning’을 만들었다.

## 2. 기술

**2.1. API/라이브러리/framework**

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![ML5JS](https://img.shields.io/badge/ml5.js-ED225D?style=for-the-badge&logo=p5.js&logoColor=white)
![Agora](https://img.shields.io/badge/agora_api-099DFD?style=for-the-badge&logo=agora&logoColor=white)
![kakaotalk](https://img.shields.io/badge/kakaotalk_api-FFCD00?style=for-the-badge&logo=kakaotalk&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)

**2.2. 배포**

~~[catchcunning.site](http://catchcunning.site)~~

![AWS EC2](https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)
![AWS SES](https://img.shields.io/badge/AWS_SES-232F3E?style=for-the-badge&logo=amazonaws&logoColor=white)
![uWSGI](https://img.shields.io/badge/uwsgi-00BF6F?style=for-the-badge&)
![NginX](https://img.shields.io/badge/NGinX-009639?style=for-the-badge&logo=nginx&logoColor=white)

## 3. 기능 설명

### 3.1. 전체적인 기능

Google Meet, Zoom과 같은 webRTC 기능을 사용하기 위해 agora의 API를 사용하였고, 부정행위 감지를 위해 AI 라이브러리 중 하나인 ML5js의 poseNet을 사용하였다. 응시자가 고개를 돌리는 등의 부정행위를 감지하면, 감독관의 시험장 페이지에서 해당 응시자의 화상카메라 화면이 빨간색 테두리로 바뀌고 경고 문구를 함께 출력하여 감독관이 응시자가 부정행위를 하였는지를 확인할 수 있다.

다른 브라우저나 메신저 프로그램 등을 이용한 부정행위는 자바스크립트의 document.fullscreenElement와 hasFocus 함수를 활용하여 제한하였다. 시험을 시작하면 전체화면 모드로 전환되어 응시자가 응시중인 브라우저 외에 다른 브라우저나 프로그램을 볼 수 없도록 하였다. 전체화면 모드가 종료되면 이를 감지하여, 3초안에 시험 재개를 하지 않으면 부정행위 방지를 위해서 자동으로 시험이 종료되도록 하였다. Alt+Tab, Window 키 등의 단축키를 사용한 화면 전환으로 브라우저가 비활성화 되면 부정행위를 한 것으로 간주하여 곧바로 시험을 종료시키도록 하였다.

실제 대면 시험장 수준의 관리감독 기능을 최대한 구현하여, 온라인 시험 환경에서도 모두가 공정한 시험을 치를 수 있다. 응시자 모두가 노력한 만큼의 공정한 결과를 얻을 수 있기를 바란다.

카카오톡 API를 활용하여, 사용자가 사이트에 접속하거나 로그인을 하면 서버 관리자에게 카카오톡으로 알림을 보내어 사이트에 누가 접속하였는지 확인할 수 있도록 하였다.

사이트 상단의 ‘화면 캡쳐’ 버튼을 누르면 캡쳐된 화면 이미지가 관리자 이메일로 전송되게 하였다. 혹시나 사이트에서 기능의 문제가 발생하면 사용자는 버튼을 클릭하여 관리자에게 캡쳐한 화면 이미지를 이메일로 보낼 수 있고, 관리자는 무슨 문제가 있는지를 신속하게 확인할 수 있다.

### 3.2. 로그인, 회원가입

시험을 치르기 전, 웹사이트에 회원가입을 하여 계정을 생성하고 로그인을 하여야 시험 응시가 가능하다. 회원가입을 하는 사용자는 이메일, 이름, 비밀번호를 입력하고, 감독관/응시자 여부를 체크한다.

### 3.3. 시험 응시장 생성

시험 감독관은 응시자들이 접속하여 시험을 치를 수 있는 방(응시장)을 생성할 수 있다.

- ‘방 코드 생성’ 버튼으로 각 방에 해당하는 방 코드를 랜덤으로 생성할 수 있고 코드를 복사할 수 있다.
- 이미지 파일로 시험 문제를 업로드 할 수 있다.
- 생성된 방 코드를 감독관이 시험 응시자들에게 공유하면 응시자가 해당 응시장에 참가할 수 있다.

### 3.4. 시험 응시

**3.4.1. 응시자**

감독관으로부터 방 코드를 공유받은 응시자는 해당 방에 접속할 수 있다. 접속 후, 응시자가 시험 시작 버튼을 클릭하면 시험 페이지를 불러오고 전체화면으로 시험 응시가 가능해진다. 응시자는 시험 시작 후 전체화면을 나가려고 하거나, 다른 브라우저로 이동을 시도 할 경우 부정행위로 간주하여 방에서 강제로 퇴장된다.

**3.4.2. 감독관**

모든 응시자가 방에 참가하고, 감독관이 부정행위 감지 버튼을 클릭하면 AI가 응시자의 고개 돌림 여부를 판단하여 부정행위를 감지할 수 있게 된다.

## 4. Demo

### 4.1. How to Start

agora api 토큰 발급 및 사용 : [https://github.com/divanov11/mychat](https://github.com/divanov11/mychat)

```bash
$ pip install -r requirements.txt
$ python3 manage.py runsslserver 0:3000 --certificate django.crt --key django.key
```

[https://localhost:3000/](https://localhost:3000/) 접속

### 4.2. Screenshots

- 메인페이지

![Untitled](https://user-images.githubusercontent.com/77189999/188304230-87505446-b0a1-4d58-9e53-2a1c826b29c7.png)

- Footer → 모든 페이지에 적용

![Untitled 1](https://user-images.githubusercontent.com/77189999/188304232-b81be920-947a-4a64-804f-0f25e179f7d4.png)

- 로그인 페이지

![Untitled 2](https://user-images.githubusercontent.com/77189999/188304233-17c7e0b4-b43d-4bb3-b206-6bd2f9cf9744.png)

- 회원가입 페이지

![Untitled 3](https://user-images.githubusercontent.com/77189999/188304234-6b6bb5b7-3afb-4919-82cf-e8857a54ea4c.png)

- 미션 1) 화면캡처 → 해당 화면 이메일로 전송

![Untitled 4](https://user-images.githubusercontent.com/77189999/188304215-9e28eea0-fe46-4434-b045-0e58049b5a0c.png)

- 미션 2) 액션 발생 시 (페이지 전환 등) 카카오톡으로 알림

![Untitled 5](https://user-images.githubusercontent.com/77189999/188304217-bb35a634-efa6-4d55-9f56-29db48850708.png)

**감독관**

- 시험 응시장 생성 페이지

![Untitled 6](https://user-images.githubusercontent.com/77189999/188304218-b2d2c796-899e-44ca-b47b-fb48de87ff23.png)

- 감독관 시험 응시장 접속 페이지

![Untitled 7](https://user-images.githubusercontent.com/77189999/188304221-8e41eee5-4f9d-4413-9d57-05fe274d415c.png)

- 감독관 시험 응시장

![Untitled 8](https://user-images.githubusercontent.com/77189999/188304222-92cbae86-0d5a-4285-8bb0-2ee37cc6ea48.png)

**응시자**

- 응시자 시험장 입장 준비 페이지 1

![Untitled 9](https://user-images.githubusercontent.com/77189999/188304225-a0d39b52-3400-4386-ad25-d4830c56c28f.png)

- 응시자 시험장 입장 준비 페이지 2

![Untitled 10](https://user-images.githubusercontent.com/77189999/188304226-1ba454b9-33d2-4f58-94e0-b76ddcb62787.png)

- 응시자 시험 응시 화면

![Untitled 11](https://user-images.githubusercontent.com/77189999/188304227-2c15a093-e322-454a-b5e9-d29ad6eef8f7.png)

- 부정행위 1 (탭 변경)

![Untitled 12](https://user-images.githubusercontent.com/77189999/188304228-a2999437-c1ce-4386-b5d0-7737f0f72ffb.png)

- 부정행위 2 (전체화면 해제)

![Untitled 13](https://user-images.githubusercontent.com/77189999/188304229-59552860-5844-4d0f-8e49-85bb5b3e257e.png)

### 만든사람들

<table border="1">
    <th>
        <img src="https://img.shields.io/badge/frontend-02569B?style=for-the-badge&logo=flutter&logoColor=white"></img>
    </th>
    <th>
        <img src="https://img.shields.io/badge/backend-092E20?style=for-the-badge&logo=django&logoColor=white"></img>
    </th>
    <th>
        <img src="https://img.shields.io/badge/backend-092E20?style=for-the-badge&logo=django&logoColor=white"></img>
        <img src="https://img.shields.io/badge/ML-ED225D?style=for-the-badge&logo=p5.js&logoColor=white"></img>
    </th>
    <th>
        <img src="https://img.shields.io/badge/Special Thanks-000000?style=for-the-badge"></img>
    </th>
    <tr>
        <td align="center">
            <img src="https://avatars.githubusercontent.com/u/92203597?v=4" width="100px;"> <br/>
            <a href="https://github.com/Junyoung-WON">원준영</a>
        </td>
        <td align="center">
            <img src="https://avatars.githubusercontent.com/u/102767676?v=4" width="100px;"> <br/>
            <a href="https://github.com/iamdudumon">김두현</a>
        </td>
        <td align="center">
            <img src="https://avatars.githubusercontent.com/u/77189999?v=4" width="100px;"> <br/>
            <a href="https://github.com/jjaegii">최재혁</a>
        </td>
        <td align="center">
            <img src="https://avatars.githubusercontent.com/u/84281599?v=4" width="100px;"> <br/>
            <a href="https://github.com/Gordned">김재현</a>
        </td>
    </tr>
</table>
