import json
import requests


api_token = 'your_api_token'
api_url_base = 'https://batch.geocoder.api.here.com/6.2/jobs'
AppId = 'wNXOex8tYhuzcQwvQ2xl'
AppCode = '66mivF5Y3Tq6dzd4ShYgew'
MailTo = 'ext.p.birkholm-buch@dsv.com'
Options = '&outdelim=|&outcols=displayLatitude,displayLongitude,locationLabel,houseNumber,street,district,city,postalCode,county,state,country&outputcombined=false'
JobId = "YYaSXEjKWQqsKBFMZRpt3KwBOFN4Xoxw"
url = 'https://batch.geocoder.api.here.com/6.2/jobs/' + JobId + '/result?app_id=wNXOex8tYhuzcQwvQ2xl&app_code=66mivF5Y3Tq6dzd4ShYgew'
url = 'https://batch.geocoder.api.here.com/6.2/jobs/YYaSXEjKWQqsKBFMZRpt3KwBOFN4Xoxw/result?app_id=wNXOex8tYhuzcQwvQ2xl&app_code=66mivF5Y3Tq6dzd4ShYgew'


headers = {'Content-Type': 'application/json',
           'Authorization': 'Bearer {0}'.format(api_token)}

r = requests.get(url)
print(r.text)