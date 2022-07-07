from datetime import datetime
from importlib.resources import open_binary
import requests

print('Hello World!')

print('testing cicd bni')

response = requests.get('https://google.com')
waktu = datetime.now()
with open('tempResponse/'+str(waktu)+'.txt','w') as f:
    f.write(response)