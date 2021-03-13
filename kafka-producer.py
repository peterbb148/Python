import json
from kafka import KafkaClient
from kafka import SimpleProducer
from kafka import KafkaProducer

kafka = KafkaClient("XXXX.XXX.XX.XX:XXXX")
print(kafka)
producer = SimpleProducer(kafka, )
print(producer)
task_op = {
    "'message": "Hai, Calling from AWS Lambda"
}
print(json.dumps(task_op))
producer.send_messages("topic_atx_ticket_update",json.dumps(task_op).encode('utf-8'))
print(producer.send_messages)
