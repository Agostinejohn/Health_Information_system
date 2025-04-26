from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

# In-memory data stores
clients = {}
programs = {}

# ---------- MODELS ----------
def create_program(name):
    program_id = str(uuid4())
    programs[program_id] = {
        "id": program_id,
        "name": name
    }
    return programs[program_id]

def register_client(name, age):
    client_id = str(uuid4())
    clients[client_id] = {
        "id": client_id,
        "name": name,
        "age": age,
        "enrolled_programs": []
    }
    return clients[client_id]

def enroll_client_in_program(client_id, program_ids):
    if client_id not in clients:
        return None
    for pid in program_ids:
        if pid in programs and pid not in clients[client_id]["enrolled_programs"]:
            clients[client_id]["enrolled_programs"].append(pid)
    return clients[client_id]

# ---------- ROUTES ----------
@app.route('/')
def welcome():
    return "Welcome to the Health Program API!"

@app.route('/programs', methods=['POST'])
def create_health_program():
    data = request.json
    program = create_program(data['name'])
    return jsonify(program), 201

@app.route('/clients', methods=['POST'])
def register_new_client():
    data = request.json
    client = register_client(data['name'], data['age'])
    return jsonify(client), 201

@app.route('/clients/<client_id>/enroll', methods=['POST'])
def enroll_client(client_id):
    data = request.json
    updated_client = enroll_client_in_program(client_id, data['program_ids'])
    if not updated_client:
        return jsonify({"error": "Client not found"}), 404
    return jsonify(updated_client)

@app.route('/clients', methods=['GET'])
def search_clients():
    name_query = request.args.get('name')
    result = [c for c in clients.values() if name_query.lower() in c['name'].lower()]
    return jsonify(result)

@app.route('/clients/<client_id>', methods=['GET'])
def get_client_profile(client_id):
    client = clients.get(client_id)
    if not client:
        return jsonify({"error": "Client not found"}), 404
    # Add readable program names to the response
    client_info = client.copy()
    client_info['program_details'] = [programs[pid] for pid in client['enrolled_programs'] if pid in programs]
    return jsonify(client_info)

# ---------- RUN ----------
if __name__ == '__main__':
    app.run(debug=True)
