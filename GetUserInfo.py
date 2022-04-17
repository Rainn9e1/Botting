import requests

def GetUserInfo(Cookie):
    UserinfoRequest = requests.get(f"https://www.roblox.com/mobileapi/userinfo", cookies = {
        ".ROBLOSECURITY": Cookie
    })

    Data = UserinfoRequest.json()

    return Data
