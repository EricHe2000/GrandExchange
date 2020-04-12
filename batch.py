from kafka import KafkaConsumer
import json
from elasticsearch import Elasticsearch
import time

time.sleep(15)
consumer = KafkaConsumer('new-listings-topic', group_id='listing-indexer', bootstrap_servers=['kafka:9092'])
es = Elasticsearch(['es'])

for message in consumer:
    # do something with the "message" in the queue... probably add to ES so we can process it later
    print(json.loads((message.value).decode('utf-8')))
    item = json.loads((message.value).decode('utf-8'))
    es.index(index='listing_index', doc_type='listing', id=item['id'], body=item)

    #commit changes w this command
    es.indices.refresh(index="listing_index")
