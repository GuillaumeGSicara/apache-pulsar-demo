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

## To Do

- Pin Pulsar to a specific version an not latest