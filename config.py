import os
from dotenv import load_dotenv

load_dotenv()

OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")
RABBITMQ_CONNECTION_STRING = os.getenv("RABBITMQ_CONNECTION_STRING")

if __name__ == '__main__':
    print(OPENWEATHERMAP_API_KEY)
