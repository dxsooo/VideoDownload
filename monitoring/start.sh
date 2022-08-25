#!/bin/bash 

docker run --name Prometheus -d -v $PWD/prometheus.yml:/etc/prometheus/prometheus.yml -p 9090:9090 --network host prom/prometheus

docker run --name Grafana -d -v grafana-storage:/var/lib/grafana -p 3000:3000 --network host grafana/grafana
