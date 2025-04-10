# api_server/node_manager.py
import uuid

class NodeManager:
    def __init__(self):
        self.nodes = {}  # node_id -> {cpu, pods, healthy}

    def register_node(self, cpu_cores):
        node_id = str(uuid.uuid4())
        self.nodes[node_id] = {
            "cpu": cpu_cores,
            "available_cpu": cpu_cores,
            "pods": [],
            "healthy": True
        }
        return node_id
