from kafka import KafkaConsumer
import json
import time

time.sleep(30)

consumer = KafkaConsumer('new-log-topic', group_id='indexer', bootstrap_servers=['kafka:9092'])
                        #spark_topic

for message in consumer:
    #get the userID and the itemID to add it to the queue
    item = json.loads((message.value).decode('utf-8'))

    #check to make sure this works lol
    user_id = item['user_id']
    item_id = item['item_id']
    with open('log.txt', 'a') as file:
        file.write(str(user_id) + '\t' + str(item_id) + '\n')