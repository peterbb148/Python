import json

json_string = '{"Response": {"MetaInfo": {"RequestId": "rargADY1R1hHv8l0sNZqPrJp4Ziqn7JV"}, "Status": "accepted", "TotalCount": 0, "ValidCount": 0, "InvalidCount": 0, "ProcessedCount": 0, "PendingCount": 0, "SuccessCount": 0, "ErrorCount": 0}}'

parsed_json = json.loads(json_string)
print(parsed_json["Response"]["MetaInfo"]["RequestId"])