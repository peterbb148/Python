#import ssl
import shutil
import tempfile
import requests
#import urllib.request
# context = ssl._create_unverified_context()

api_url_base = 'https://batch.geocoder.api.here.com/6.2/jobs'
AppId = 'wNXOex8tYhuzcQwvQ2xl'
AppCode = '66mivF5Y3Tq6dzd4ShYgew'
JobId = 'uQYJhfTJllxVBdHCYI4UeE42vxFb1ei5'
headers = {'Accept': 'application/json', 'accept-charset':'UTF-8'}
url = 'https://batch.geocoder.api.here.com/6.2/jobs/' + JobId + '/result?app_id=wNXOex8tYhuzcQwvQ2xl&app_code=66mivF5Y3Tq6dzd4ShYgew'

r = requests.get(url, headers=headers)
open(f"results.zip", 'wb').write(r.content)