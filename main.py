import requests, os

url = "https://spclient.wg.spotify.com/signup/public/v1/account/"


while True:
    os.system("cls")

    email = input("Enter email: ")
    password = input("Enter password: ")
    name = input("Enter name: ")

    payload = {
        'creation_point': 'https://login.app.spotify.com/?utm_source=spotify&utm_medium=desktop-win32-store&utm_campaign=msft_1&referral=msft_1&referrer=msft_1',
        'key': '4c7a36d5260abca4af282779720cf631',
        'platform': 'desktop',
        'birth_month': '4',
        'displayname': f'{name}',
        'birth_day': '12',
        'password_repeat': f'{password}',
        'creation_flow': 'desktop',
        'referrer': 'msft_1',
        'iagree': '1',
        'password': f'{password}',
        'birth_year': '1998',
        'gender': 'male',
        'email': f'{email}',
        'username': f'{name}'
        }

    headers = {
        'Host': 'spclient.wg.spotify.com',
        'client-token': 'AAD0FIQS2mUNeTalJyIQyiswa7WFnTRCkYIQDTrCdLThJVxhGeUWswLkEm1wlKHHd0TGI1uWz8mSFCwGVYNjeZDF+p4LsknfroAOmwMyuwvOtAxXpSgcp0JY8VNo2ATJPZXhuh/ckNEFSdbDErsFuXTcXf2QFAmIkbizztsDEue0r7z2BY21zNzpJbje4GYBvmBRIlg6eYmz1yNDAneetd+RAMdDWrQmlK4TMD8YRsIkD+UxIY4P7Q==',
        'Cookie': '__gads=ID=b2928c2f22f3c8b2:T=1615518277:S=ALNI_MbruMuMNn1y7OYJUcnjwcxn6ZEzVg'
        }

    r = requests.post(url, headers=headers, data=payload)

    print(r.text, r.status_code)

    if r.json()['status'] == 1:
        try: 
            with open('claimed.txt', "a") as prime:
                prime.write(f'{email} : {password} : {name}\n')
        except:
            print(f'{email} : {password} : {name}\n')

    input()