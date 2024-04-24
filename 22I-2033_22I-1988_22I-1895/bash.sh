#!/bin/bash

# Launch Zookeeper in a new terminal
gnome-terminal --title="Zookeeper" -- bash -c "zookeeper-server-start.sh config/zookeeper.properties && read -p 'Press Enter to exit...'" &

# Wait for 2 seconds before proceeding
sleep 2

# Launch Kafka Server in a new terminal
gnome-terminal --title="Kafka Server" -- bash -c "kafka-server-start.sh config/server.properties && read -p 'Press Enter to exit...'" &

# Wait for 4 seconds before proceeding
sleep 4

# Start Kafka Producer in a new terminal
gnome-terminal --title="Kafka Producer" -- bash -c "python3 data_producer.py && read -p 'Press Enter to exit...'" &

# Wait for 2 seconds before proceeding
sleep 2

# Start Kafka Consumer 1 in a new terminal
gnome-terminal --title="Kafka Consumer 1" -- bash -c "python3 data_consumer1.py && read -p 'Press Enter to exit...'" &

# Wait for 2 seconds before proceeding
sleep 2

# Start Kafka Consumer 2 in a new terminal
gnome-terminal --title="Kafka Consumer 2" -- bash -c "python3 data_consumer2.py && read -p 'Press Enter to exit...'" &

# Wait for 2 seconds before proceeding
sleep 2

# Start Kafka Consumer 3 in a new terminal
gnome-terminal --title="Kafka Consumer 3" -- bash -c "python3 data_consumer3.py && read -p 'Press Enter to exit...'" &