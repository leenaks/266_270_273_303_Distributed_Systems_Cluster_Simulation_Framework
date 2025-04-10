 # api_server/health_monitor.py
import time

class HealthMonitor:
    def __init__(self, node_manager):
        self.node_manager = node_manager
        self.heartbeat_times = {}

    def receive_heartbeat(self, node_id):
        self.heartbeat_times[node_id] = time.time()
        self.node_manager.nodes[node_id]["healthy"] = True

    def check_health(self):
        current_time = time.time()
        for node_id, last_time in self.heartbeat_times.items():
            if current_time - last_time > 10:  # 10s timeout
                self.node_manager.nodes[node_id]["healthy"] = False
