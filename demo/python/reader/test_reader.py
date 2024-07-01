import pulsar
import logging
from pulsar import Reader


# Create a pulsar client object
client = pulsar.Client(
    'pulsar://localhost:6650',
    logger= logging.getLogger('pulsar')
)

# Create a reader on a topic
reader: Reader = client.create_reader("demo-topic", pulsar.MessageId.earliest)
print("Reading messages from topic {}...".format(reader.topic()))

print("Reading all messages...")
while reader.has_message_available():
    print(reader.read_next().data())

# The seek method is used to move the reader to a specific message id
print("Reading last message...")
print(reader.seek(pulsar.MessageId.latest))
assert reader.has_message_available() == False

print("Reading first message")
reader.seek(pulsar.MessageId.earliest)
print(reader.read_next().data())

client.close()