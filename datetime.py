from datetime import datetime

datestring = "2020-04-24T09:31:14.824+0000"
date_obj = datetime.strptime(datestring, "%Y-%m-%dT%H:%M:%S.%f%z")
print(date_obj)
print(date_obj.strftime('%Y%m%d-%H%m%S'))