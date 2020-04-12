from kafka import KafkaConsumer
import json
import time

consumer = None

while (consumer is None):
    try:
        consumer = KafkaConsumer('new-log-topic', group_id='indexer', bootstrap_servers=['kafka:9092'])
    except:
        print("still waiting")

for message in consumer:
    #get the userID and the itemID to add it to the queue
    item = json.loads((message.value).decode('utf-8'))

    #check to make sure this works lol
    user_id = item['user_id']
    item_id = item['item_id']
    with open('log.txt', 'a') as file:
        file.write(str(user_id) + '\t' + str(item_id) + '\n')