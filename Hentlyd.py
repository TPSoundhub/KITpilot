import requests

url = "https://raw.githubusercontent.com/TPSoundhub/KITpilot/master/Projlyd/Baggrund.wav"
dest = "/home/pi/Python_test/Baggrund.wav"
r=requests.get(url)

with open(dest, 'wb') as f:
    f.write(r.content)
    

url = "https://raw.githubusercontent.com/TPSoundhub/KITpilot/master/Projlyd/Lyd1.wav"
dest = "/home/pi/Python_test/Lyd1.wav"
r=requests.get(url)

with open(dest, 'wb') as f:
    f.write(r.content)

url = "https://raw.githubusercontent.com/TPSoundhub/KITpilot/master/Projlyd/Lyd2.wav"
dest = "/home/pi/Python_test/Lyd2.wav"
r=requests.get(url)

with open(dest, 'wb') as f:
    f.write(r.content)
        
