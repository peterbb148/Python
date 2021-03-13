import json
import base64

event = '{"eventSource": "aws:kafka", "eventSourceArn": "arn:aws:kafka:eu-west-1:483459036065:cluster/dev-kafka-global/20d5ee4b-d0f8-4a86-b7ca-677445dd05b2-4", "records": {"devops-0": [{"topic": "devops", "partition": 0, "offset": 9, "timestamp": 1602080974973, "timestampType": "CREATE_TIME", "key": "", "value": "eyAibWVzc2FnZSIgOiAiSGVsbG8gZGVhciBMYW1iZGEgZnJvbSBLYWZrYSIgfQ=="}]}}'

json_obj = json.loads(event)
print(base64.b64decode(json_obj['records']['devops-0'][0]['value']).decode('utf-8'))
