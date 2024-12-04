import pika

# Connect to RabbitMQ (using the same network and credentials)
connection = pika.BlockingConnection(pika.ConnectionParameters('rabbit-1', 5672, '/', pika.PlainCredentials('guest', 'guest')))
channel = connection.channel()

# Declare the queue (ensure the queue exists)
channel.queue_declare(queue='your-queue-name')

# Publish a message
channel.basic_publish(exchange='',
                      routing_key='your-queue-name',
                      body='Hello, RabbitMQ from Python!')

print("Message Sent!")

# Close the connection
connection.close()
