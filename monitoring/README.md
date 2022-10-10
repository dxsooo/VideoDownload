# Monitoring

Use Prometheus and Grafana to monitor workers and RabbitMQ in celery mode.

## Start

For RabbitMQ, prometheus metrics is exposed in `http://host:15692/metrics`

> Remember to forward port to host machine if RabbitMQ is setup with docker

For Celery workers, start worker(with `-E`) and flower with cmd first.

Edit `prometheus.yml` to set flower and RabbitMQ host.

Finally,

```bash
./start.sh
```

## Use

Open [Grafana](http://localhost:3000/), use admin/admin for credentials. Switch to dashboard `General/celery-monitoring` for celery and `General/rabbitmq-overview` for RabbitMQ.

## Reference

- <https://flower.readthedocs.io/en/latest/prometheus-integration.html#celery-flower-prometheus-grafana-integration-guide>
- <https://www.rabbitmq.com/prometheus.html>
