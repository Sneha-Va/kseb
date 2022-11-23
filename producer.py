from kafka import KafkaProducer
import random
import time
bootstrap_server = ["localhost:9092"]
topic = "kseb"
producer = KafkaProducer(bootstrap_servers = bootstrap_server)
producer = KafkaProducer()
jsonData = {}
def senddata():
    random_number = random.randint(1,10)
    jsonData = {'consumerid':4,'unit':random_number}
    message = producer.send(topic, bytes(str(jsonData),"utf-8"))
    print(jsonData)
    metadata = message.get()
    time.sleep(5)
while True:
  senddata()    