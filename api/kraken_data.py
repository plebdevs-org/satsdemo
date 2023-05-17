import requests

base_url = 'https://api.kraken.com/0/public'

def getServerTime():
    resp = requests.get(base_url + '/Time')
    data = resp.json()
    readable_date = data['result']['rfc1123']
    return readable_date

server_time = getServerTime()
print("Server Time:", server_time)

def getSystemStatus(): 
    resp = requests.get(base_url + '/SystemStatus')
    data = resp.json()
    return data['result']

system_status = getSystemStatus()
print("System Status:", system_status)

def getAssetPairs(asset):
    resp = requests.get(base_url + "/AssetPairs?pair=" + asset)
    print('===========================================================================')
    print(base_url + "/AssetPairs?pair=" + asset)
    print('===========================================================================')
    data = resp.json()
    return data['result'][asset]

#Kraken has weird full symbol for BTC/USD as 'XXBTZUSD'
 
info = getAssetPairs('XXBTZUSD')
print(info)
    