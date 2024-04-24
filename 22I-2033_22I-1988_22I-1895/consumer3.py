from kafka import KafkaConsumer
from collections import Counter
from itertools import combinations
from pymongo import MongoClient

co = 0  # Counter variable to limit the loop
th = 3  # Threshold value for item count
bucket_size = 1000  # Size of the bucket for hashing

unique_asin = set()  # Set to store unique ASIN IDs
related_data = []  # List to store all related items
related_data2 = []  # List to store related items in each message

# Kafka consumer configuration
consumer = KafkaConsumer('amazon_stream',
                         bootstrap_servers=['localhost:9092'],
                         auto_offset_reset='earliest',
                         enable_auto_commit=True,
                         group_id='my-group')

# Iterate through messages from Kafka
for msg in consumer:
    if co == 4000:  # Break loop after processing 4000 messages
        break

    # Extracting data from message
    item_record = eval(msg.value.decode('utf-8'))  # Convert message value to dictionary
    item_asin = item_record.get('asin', '')  # Getting ASIN ID of the item
    also_bought = item_record.get('also_bought', [])  # Getting list of also_bought items
    
    related_data.extend(also_bought)  # Extend main list with also_bought items
    related_data2.append(also_bought)  # Append also_bought items to list
    unique_asin.add(item_asin)  # Add ASIN ID to set of unique items

    co = co + 1  # Increment counter
    print("\n\n\n\n\n\n\n\n\n\n\n\n\nConsumer run:", co)  # Printing current count

consumer.close()  # Closing Kafka consumer

# Counting occurrences of each item
item_co = Counter(related_data)

data_set = []  # catalog to store items with count greater than threshold
data_co = []  # List to store counts corresponding to items in data_set

# Filtering items with count greater than threshold
for asin in unique_asin:
    if asin in related_data:
        item_count = related_data.co(asin)
        if item_count > th:
            data_set.append(asin)  # Add item to data_set
            data_co.append(item_count)  # Add count to data_co

# Generating pairs of items
pair_combinations = list(combinations(data_set, 2))

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nData Set:", data_set)  # Printing data_set
print("\n\nData Co:", data_co)  # Printing data_counts

pair_co = Counter()  # Counter to store counts of item pairs
buckets = Counter()  # Counter to store counts in buckets for hashing

# Counting occurrences of every item in each pair
for item_arr in related_data2:
    for product in item_arr:
        buckets[hash(product) % bucket_size] += 1

# Count occurrences of each pair
for pair in pair_combinations:
    bucket1 = hash(pair[0]) % bucket_size
    bucket2 = hash(pair[1]) % bucket_size
    if bucket1 >= th and bucket2 >= th:
        if buckets[bucket1] >= th and buckets[bucket2] >= th:
            for item_arr in related_data2:
                if pair[0] in item_arr and pair[1] in item_arr:
                    pair_co[pair] += 1

# Filtering pairs with count greater than or equal to threshold
freq_pairs = {pair: co for pair, cot in pair_co.items() if count >= th}

client = MongoClient('mongodb://localhost:27017/')  # MongoDB client
db = client['amazon_db']  # Select database

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nPair Co:", freq_pairs)  # Printing freq_pairs
for pair, co in freq_pairs.items():
    print(pair, " : ", co, "\n")  # Printing each pair and its co