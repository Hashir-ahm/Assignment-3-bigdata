Amazon Metadata Streaming Pipeline

Project Overview:
This project aims to build a streaming pipeline for frequent itemset mining using the Amazon Metadata dataset. 

Approach:

Downloading and Sampling the Dataset:
The Amazon Metadata dataset is downloaded and sampled to ensure a manageable size for processing (minimum 15 GB).

Pre-Processing:
Data preprocessing involves cleaning and formatting the dataset for analysis.

Streaming Pipeline Setup:
A producer application streams preprocessed data in real-time.
Three consumer applications subscribe to the producer's data stream.

Frequent Itemset Mining:
One consumer implements the Apriori algorithm.
Another consumer implements the PCY algorithm.
The third consumer performs innovative analyses using techniques suitable for streaming data and stores results in MongoDB.

Database Integration:
MongoDB is chosen for storing results. 

Enhancing Project Execution with a Bash Script:
Using a Bash script to automate the execution of the producer, consumers, and Kafka components.

Conclusion:
This streaming pipeline project demonstrates the implementation of frequent itemset mining algorithms in a real-time streaming environment using the Amazon Metadata dataset. 

Done by:
22I-2033 
Siraj Ali

22I-1988
Hashir Ahmed

22I-1895
Azhaff khalid
