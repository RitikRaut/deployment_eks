from flask import Flask, jsonify
from kubernetes import client, config

app = Flask(__name__)

# Load Kubernetes config
config.load_incluster_config()

v1 = client.CoreV1Api()

@app.route('/pods', methods=['GET'])
def get_pods():
    pods = v1.list_pod_for_all_namespaces(watch=False)
    pod_details = []
    for pod in pods.items:
        pod_info = {
            "pod_name": pod.metadata.name,
            "pod_ip": pod.status.pod_ip,
            "node_name": pod.spec.node_name,
            "node_ip": pod.status.host_ip,
        }
        pod_details.append(pod_info)
    return jsonify(pod_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
