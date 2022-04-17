import requests

def Getcsrf(Cookie):
    Token = requests.post("https://auth.roblox.com/v1/login", cookies = {
        ".ROBLOSECURITY": Cookie
    })

    return Token.headers['x-csrf-token']
