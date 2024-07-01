import pulsar
import logging

import time
import nltk
from nltk.corpus import words
from random import sample, randint

nltk.download('words')

logger = logging.getLogger('pulsar')
logger.setLevel(logging.DEBUG)
client = pulsar.Client(
    'pulsar://localhost:6650',
    logger=logger
)

# Create a producer on a topic
producer: pulsar.Producer = client.create_producer(
    topic="persistent://public/default/rand-word-topic",
    producer_name="wordomatic",
    schema=pulsar.schema.StringSchema(),
)
print("Producing messages to topic {}...".format(producer.topic()))

words = words.words()

try:
    while True:
        rand_words = ' '.join(sample(words, randint(1, 20)))
        time.sleep(1)
        producer.send(rand_words)
except KeyboardInterrupt:
    print("\nShutting down producer & client...")
    producer.close()
    client.close()