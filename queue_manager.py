import pika
from config import RABBITMQ_CONNECTION_STRING

connection_string = RABBITMQ_CONNECTION_STRING
connection = pika.BlockingConnection(pika.URLParameters(RABBITMQ_CONNECTION_STRING))
channel = connection.channel()

channel.queue_declare(queue='weather')

channel.basic_publish(exchange='',
                      routing_key='weather',
                      body="hello")
