import json

def transform_data(batch_input):
    # List of fields to eliminate from each record
    fields_to_eliminate = ['category', 'tech1', 'description', 'fit', 'title', 'image', 'tech2', 'brand', 'feature', 'rank', 'details', 'main_cat', 'similar_item', 'date', 'price']
    
    # Use dictionary comprehension to create a new dictionary excluding specified fields
    transformed_batch = [{key: value for key, value in record.items() if key not in fields_to_eliminate} for record in batch_input]
    
    return transformed_batch

    
    # Removing specified fields from each record in the batch
    for record in batch_input:
        for field in fields_to_eliminate:
            if field in record:
                del record[field]
    
    return batch_input

# Size of each batch
batch_size_val = 100

# Opening input file for reading and output file for appending
with open('amazon_data.json', 'r') as input_file, open('processed_output.json', 'a') as output_file:
    # Reading data in batches until the end of file
    for line in input_file:
        # Reading  data from input file provided
        batch_input_data = [json.loads(next(input_file)) for _ in range(batch_size_val)]
        
        # Transforming the batch data
        processed_batch = transform_data(batch_input_data)
        
        # here it is writing  the prepared  batch to the output file at the end
        json.dump(processed_batch, output_file, indent=4)