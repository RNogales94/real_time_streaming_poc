from data_generator import DataGenerator
from queue_manager import QueueManager

from config import RABBITMQ_CONNECTION_STRING, OPENWEATHERMAP_API_KEY

# (lat, lon)
interesting_points = [
    (52.084516, 5.115539),
]

generator = DataGenerator(api_key=OPENWEATHERMAP_API_KEY)
queue_manager = QueueManager(connection_string=RABBITMQ_CONNECTION_STRING)

for lat, lon in interesting_points:
    data_stream = generator.get_data(lat, lon)
    for measure in data_stream:
        print(measure)
        queue_manager.publish(measure)



