<p align="center">
  <img src="/img/pulsar-demo.png" alt="pulsar logo">
</p>

[![Commitizen friendly](https://img.shields.io/badge/commitizen-friendly-brightgreen.svg)](http://commitizen.github.io/cz-cli/)

## Description

This repo is a playground for poping a local [Apache Pulsar cluster](https://pulsar.apache.org/) and an [Pulsar Manager](https://github.com/apache/pulsar-manager) using Docker Compose


## Configuring Pulsar Manager

When logging to the local url 'http://localhost:9527' you will need to create a super user in order to login. This can be done by running the following commands:
```bash
CSRF_TOKEN=$(curl http://localhost:7750/pulsar-manager/csrf-token) 
```
```bash
curl \
    -H "X-XSRF-TOKEN: $CSRF_TOKEN" \
    -H "Cookie: XSRF-TOKEN=$CSRF_TOKEN;" \
    -H 'Content-Type: application/json' \
    -X PUT http://localhost:7750/pulsar-manager/users/superuser \
    -d '{"name": "<LOGIN_USERNAME>", "password": "<LOGIN_PASSWORD>", "description": "test", "email": "username@test.org"}'
```

:white_check_mark: **Expected output**
```
{"message":"Add super user success, please login"}
```

-------

Once logged in, you will need to create an environement. An environment is linked to your pulsar cluster, from the `docker-compose.yml` you can enter the following values:

<p align="center">
  <img src="/img/pulsar_manager_login_params.png" alt="Your Image Description">
</p>

On sucess you can click on your environement to access the pulsar manager panel


# Start the pulsar shell

to start the pulsar shell you'll first need to get the shell `.tar.gz` distribution here
```bash
curl -L https://www.apache.org/dyn/closer.lua/pulsar/pulsar-3.3.0/apache-pulsar-shell-3.3.0-bin.tar.gz\?action\=download -o apache-pulsar-shell-3.3.0-bin.tar.gz
```

unzip it with
```bash
tar xvfz apache-pulsar-shell-3.3.0-bin.tar.gz 
```

`cd` to the created directory and run the pulsar shell (you'll need a recent java version on your machine > 18)

```bash
cd apache-pulsar-shell-3.3.0
bin/pulsar-shell
```

the output should look something like this:
<p align="center">
  <img src="/img/pulsar-shell-live.png" alt="Your Image Description">
</p>

Check that your are correctly connected to the pulsar cluster declared above
```bash
admin tenants list
````
**Note**: __The created folder apache-pulsar-shell-3.3.0/conf contains the cluster information your pulsar shell will connect to, by default, you should have to change anything in this file__

<p align="center">
  <img src="/img/pulsar-shell-tenants-list.png" alt="Your Image Description">
</p>


## To Do

- Pin Pulsar to a specific version an not latest
- Link a [postgres DB with a sink](https://pulsar.apache.org/docs/next/io-jdbc-sink/) for demo !