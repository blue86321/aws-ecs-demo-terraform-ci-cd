# Web Backend

## How to Run in Local Docker

### Run

- Docker

```bash
# Ctrl-C to stop
docker compose -f compose.local.yaml up
```

- Visit Docs

```
http://localhost:8000/docs
```

### Destroy

```bash
docker compose -f compose.local.yaml down -v --rmi all
```
