import pulsar
import logging


# Create a pulsar client object
logger = logging.getLogger('pulsar')
logger.setLevel(logging.ERROR)
client = pulsar.Client(
    'pulsar://localhost:6650',
    logger=logger
)

# Create a reader on a topic
reader: pulsar.Reader = client.create_reader(
    topic="persistent://public/default/rand-word-topic",
    start_message_id=pulsar.MessageId.earliest,
    reader_name="wordomatic-reader"
)
print("Reading messages from topic {}...".format(reader.topic()))

print("Reading all messages...")
while reader.has_message_available():
    print(reader.read_next().data())

print("Moving reading cursor to first message")
reader.seek(pulsar.MessageId.earliest)
print(reader.read_next().data())

client.close()