# Monitoring

According to <https://flower.readthedocs.io/en/latest/prometheus-integration.html#celery-flower-prometheus-grafana-integration-guide>, use prometheus and grafana to monitor celery workers.

## Start

Start worker(with `-E`) and flower with cmd first, and then

```bash
./start.sh
```

> Edit `prometheus.yml` first if flower is started with docker or not in localhost.

## Use

Open [Grafana](http://localhost:3000/), use admin/admin for credentials. Switch to dashboard `General/celery-monitoring`
