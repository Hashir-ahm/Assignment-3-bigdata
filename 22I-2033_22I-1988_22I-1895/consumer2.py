from kafka import KafkaConsumer
from collections import Counter
from itertools import combinations

counter_var = 0  # Counter variable to limit the loop
threshold_val = 3  # Threshold value for item count

unique_items = set()  # Set to store unique ASIN IDs
item_list = []  # List to store all purchased items
item_list2 = []  # List to store purchased items in each message

# Kafka consumer configuration
consumer_instance = KafkaConsumer('amazon_stream',
                                  bootstrap_servers=['localhost:9092'],
                                  auto_offset_reset='earliest',
                                  enable_auto_commit=True,
                                  group_id='my-group')

# Iterate through messages from Kafka
for message in consumer_instance:
    if counter_var == 4000:  # Break loop after processing 4000 messages
        break

    # Extract data from message
    item_data = eval(message.value.decode('utf-8'))  # Convert message value to dictionary
    asin_id = item_data.get('asin', '')  # Get ASIN ID of the item
    also_purchased = item_data.get('also_purchased', [])  # Get list of also_purchased items
    
    item_list.extend(also_purchased)  # Extend main list with also_purchased items
    item_list2.append(also_purchased)  # Append also_purchased items to list
    unique_items.add(asin_id)  # Add ASIN ID to set of unique items

    counter_var =var +1
    print("\n\n\n\n\n\n\n\n\n\n\n\n\nConsumer run:", counter_var)  

consumer_instance.close()  # Close Kafka consumer

# Counting occure of every item
item_counter = Counter(item_list)

data_set2 = []  # List to store items with count greater than threshold
data_set3 = []  # List to store counts corresponding to items in data_set2

# Filter items with count greater than threshold
for item_id in unique_items:
    if item_id in item_list:
        item_count_val = item_list.count(item_id)
        if item_count_val > threshold_val:
            data_set2.append(item_id)  # Add item to data_set2
            data_set3.append(item_count_val)  # Add count to data_set3

# Generate pairs of items
item_pairs = list(combinations(data_set2, 2))

print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nData Set 2:", data_set2)  # Print data_set2
print("\n\nData Set 3:", data_set3)  # Print data_set3

pair_count_list = []  # List to store counts of item pairs
pairs_list2 = []  # List to store item pairs

# Counting  occurre of every item pair
for item_pair in item_pairs:
    count_val = 0
    for arr_item in item_list2:
        if item_pair[0] in arr_item and item_pair[1] in arr_item:
            count_val += 1
    if count_val >= threshold_val:
        pair_count_list.append(count_val)  # Add count to pair_count_list
        pairs_list2.append(item_pair)  

print("\n\n\n\n\n\n\n\n\Pair Counts:", pair_count_list)  # Printing pair_count_list
for item_pair, count_val in zip(pairs_list2, pair_count_list):
    print(item_pair, " : ", count_val, "\n")  # Print each item pair and its count