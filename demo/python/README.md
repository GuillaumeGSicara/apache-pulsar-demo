## How To

Create a python virtual environement with the `requirement.txt` to run the following scripts

## Producer

It will create a persistent (see [persistent vs. non-persistent](https://pulsar.apache.org/docs/3.3.x/admin-api-topics/)) message on the `default` namespace for the `public` \

The message will be random words extracted from a nltk corpus.

## Reader

The reader allows you to read without affecting the cluster or creating a consumer with a subscription.

## Consumer

The consumer script will create a subscription on the cluster.
The cluster will send information to the cluster based on it's list of subscription.

The default subscription type is `shared` see [pulsar documentation](https://pulsar.apache.org/docs/next/client-libraries-consumers/) for other subscription types.

the consumer emulates a process before giving an [acknowledgment of message receipt](https://pulsar.apache.org/docs/3.3.x/concepts-messaging/)