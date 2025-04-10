# api_server/app.py
from flask import Flask, request, jsonify
from node_manager import NodeManager

app = Flask(__name__)
node_manager = NodeManager()

@app.route('/add_node', methods=['POST'])
def add_node():
    data = request.json
    cpu_cores = data.get('cpu_cores')
    node_id = node_manager.register_node(cpu_cores)
    return jsonify({"message": "Node added", "node_id": node_id})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
