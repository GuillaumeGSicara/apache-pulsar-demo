import time
import pulsar
import logging


# Create a pulsar client object
logger = logging.getLogger('pulsar')
logger.setLevel(logging.ERROR)
client = pulsar.Client(
    'pulsar://localhost:6650',
    logger=logger
)


# Create a consumer on a topic
consumer: pulsar.Consumer = client.subscribe(
    topic="persistent://public/default/rand-word-topic",
    subscription_name="wordomatic-subscription",
    consumer_name="wordomatic-consumer"
)

def process_words(words: str) -> None:
    print("INFO: Processing message...")
    print("Received message: ", words)
    print("Receveid message is of length: ", len(words))
    print("Received message has {} words".format(len(words.split())))
    time.sleep(0.2)


# Place consumer cursor at the earliest message (for developement purposes)
consumer.seek(pulsar.MessageId.earliest)

try:
    while True:
        # Receive a message from the topic
        received_message: pulsar.Message = consumer.receive()

        # Do something with the received message
        process_words(received_message.data())

        # Acknowledge the received message
        consumer.acknowledge(received_message.message_id())

        consumer.get_last_message_id()

except KeyboardInterrupt:
    print("\nShutting down consumer & client...")
    consumer.close()
    client.close()