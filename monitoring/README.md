# Monitoring

According to <https://flower.readthedocs.io/en/latest/prometheus-integration.html#celery-flower-prometheus-grafana-integration-guide>, use prometheus and grafana to monitor celery workers.

## Start

Start worker(with `-E`) and flower with cmd first, and then

```bash
./start.sh
```

> Edit `prometheus.yml` first if flower is started with docker or not in localhost.

## Configure

Open [Grafana](http://localhost:3000/), use admin/admin for credentials.

And then add datasource, select Prometheus and enter url: <http://localhost:9090>, click `Save & test`.

Add dashboard by `import` and select `celery-monitoring-grafana-dashboard.json` in current path. Select `Prometheus` and click `Import`.

Finished.
