from prometheus_client import start_http_server, Gauge
import random
import time

# Metrics definitions
CPU_LOAD = Gauge('network_cpu_load', 'Current CPU load')
PACKET_LOSS = Gauge('network_packet_loss', 'Packet loss percentage')

def collect_metrics():
    while True:
        CPU_LOAD.set(random.uniform(0, 100))  # Replace with real data
        PACKET_LOSS.set(random.uniform(0, 5))
        time.sleep(5)

if __name__ == '__main__':
    start_http_server(8000)
    print("Prometheus exporter running on http://localhost:8000")
    collect_metrics()