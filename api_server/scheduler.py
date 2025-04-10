 # api_server/scheduler.py
import uuid

class Scheduler:
    def __init__(self, node_manager):
        self.node_manager = node_manager

    def schedule_pod(self, cpu_req):
        for node_id, node in self.node_manager.nodes.items():
            if node["available_cpu"] >= cpu_req and node["healthy"]:
                pod_id = str(uuid.uuid4())
                node["pods"].append(pod_id)
                node["available_cpu"] -= cpu_req
                return pod_id
        return "No available node"
