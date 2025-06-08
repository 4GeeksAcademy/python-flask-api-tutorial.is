from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.get_json()
    if "label" not in todo or "done" not in todo:
        return jsonify({"error": "Datos inválidos"}), 400
    todos.append(todo)
    return jsonify(todos), 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < 0 or position >= len(todos):
        return jsonify({"error": "Posición inválida"}), 404
    todos.pop(position)
    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(debug=True)
