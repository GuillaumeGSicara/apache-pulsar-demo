
# Boot the PostgresDB

You can boot the postgresdb using the local `docker-compose.yaml`

```bash
docker compose up --build --force-recreate
```

Create the table in your postgres DB

```sql
CREATE TABLE IF NOT EXISTS pulsar_postgres_jdbc_sink
(
    ID SERIAL PRIMARY KEY,
    NAME VARCHAR(255) NOT NULL
);
```

# Download the JDBC sink

Valid url as of 2/07/2023

```bash
curl -L https://www.apache.org/dyn/closer.lua/pulsar/pulsar-3.3.0/connectors/pulsar-io-jdbc-postgres-3.3.0.nar\?action\=download -o pulsar-io-jdbc-postgres-3.3.0.nar
```
