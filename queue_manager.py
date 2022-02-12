import pika


class QueueManager:
    def __init__(self, connection_string: str):
        self.connection = pika.BlockingConnection(pika.URLParameters(connection_string))
        self.channel = self.connection.channel()
        self.queue_name = 'weather'

    def __init_channels(self) -> None:
        self.channel.queue_declare(queue=self.queue_name)

    def publish(self, data: str) -> None:
        self.channel.basic_publish(exchange='',
                                   routing_key=self.queue_name,
                                   body=str(data))






