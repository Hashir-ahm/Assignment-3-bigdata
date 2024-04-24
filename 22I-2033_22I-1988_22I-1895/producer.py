import json
from kafka import KafkaProducer
from time import sleep

# details of connection
brk = ['localhost:9092']
t_n = 'amazon_stream'

# initializing the producer of kafka
def serialize_json(x):
    return json.dumps(x).encode('utf-8')
prd = KafkaProducer(bootstrap_servers=brk, value_serializer=serialize_json)

# reading  the data from json and streaming on to the  kafka
def streaming_json(json_filepath):
    with open(json_filepath, 'r') as file:
        for line in file:
            try:
                data_record = json.loads(line.strip())
                prd.send(t_n, value=data_record)
                print('kafka"s data:', data_record)
                # Adjusting sleep time if needed
                sleep(1)

            except json.JSONDecodeError as json_error:
                print(f"Error in decoding: {json_error}. skipped line")
                continue
            except Exception as e:
                print(f"sending back the error to kafka: {e}")
                continue

# json file's path
file_p = 'amazon_data.json'

# calling function
streaming_json(file_p)

# program running till user's input
input("hit enter to exit the program")