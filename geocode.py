import csv
import json
import requests

csv_reader = csv.reader('Addresses.csv', delimiter=';')


api_url_base = 'https://batch.geocoder.api.here.com/6.2/jobs'
AppId = 'wNXOex8tYhuzcQwvQ2xl'
AppCode = '66mivF5Y3Tq6dzd4ShYgew'
MailTo = 'ext.p.birkholm-buch@dsv.com'
Options = '&action=run&header=true&inDelim=;&outDelim=;&outcols=relevance,matchlevel,country,state,county,city,district,street,postalcode,latitude,longitude&outputcombined=false'
JobId = "YYaSXEjKWQqsKBFMZRpt3KwBOFN4Xoxw"
url = 'https://batch.geocoder.api.here.com/6.2/jobs/YYaSXEjKWQqsKBFMZRpt3KwBOFN4Xoxw/result?app_id=wNXOex8tYhuzcQwvQ2xl&app_code=66mivF5Y3Tq6dzd4ShYgew'
url = "https://batch.geocoder.api.here.com/6.2/jobs" + "?app_id=" + AppId + "&app_code=" + AppCode + "&mailto=" + MailTo + Options

headers = {'Accept': 'application/json', 'accept-charset':'UTF-8'}

f = open("Addresses.csv", "r") 
body = f.read()
r = requests.post(url, data=body, headers=headers)
parsed_json = json.loads(r.text)
JobId = parsed_json["Response"]["MetaInfo"]["RequestId"]
print(f'JobId is {JobId}')