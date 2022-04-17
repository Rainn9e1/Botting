import requests

def GetModelOwner(Cookie, ID):
    SellerRequest = requests.get(f"https://api.roblox.com/Marketplace/ProductInfo?assetId={ID}", cookies = {
        ".ROBLOSECURITY": Cookie
    })

    Data = SellerRequest.json()

    return Data
