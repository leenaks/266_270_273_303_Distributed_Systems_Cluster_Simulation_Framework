# api_server/app.py
from flask import Flask, request, jsonify
from node_manager import NodeManager
from scheduler import Scheduler
from health_monitor import HealthMonitor

app = Flask(__name__)
node_manager = NodeManager()
scheduler = Scheduler(node_manager)
monitor = HealthMonitor(node_manager)

@app.route('/add_node', methods=['POST'])
def add_node():
    data = request.json
    cpu_cores = data.get('cpu_cores')
    node_id = node_manager.register_node(cpu_cores)
    return jsonify({"message": "Node added", "node_id": node_id})

@app.route('/launch_pod', methods=['POST'])
def launch_pod():
    data = request.json
    cpu_req = data.get('cpu')
    pod_id = scheduler.schedule_pod(cpu_req)
    return jsonify({"pod_id": pod_id})

@app.route('/heartbeat', methods=['POST'])
def heartbeat():
    data = request.json
    monitor.receive_heartbeat(data["node_id"])
    return jsonify({"message": "Heartbeat received"})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
