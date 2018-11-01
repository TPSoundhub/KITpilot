import requests

url = "https://raw.githubusercontent.com/TPSoundhub/KITpilot/master/Projlyd/hej-1sek.wav"
dest = "/home/pi/Python_test/hej-1sek.wav"
r=requests.get(url)

with open(dest, 'wb') as f:
    f.write(r.content)
    

