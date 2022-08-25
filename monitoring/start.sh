#!/bin/bash 

docker run --name Prometheus -d -v $PWD/prometheus.yml:/etc/prometheus/prometheus.yml --network host prom/prometheus

docker run --name Grafana -d -v grafana-storage:/var/lib/grafana -v $PWD/provisioning:/etc/grafana/provisioning --network host grafana/grafana
