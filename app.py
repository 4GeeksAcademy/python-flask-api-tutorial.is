from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

# GET /todos
@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

# POST /todos
@app.route('/todos', methods=['POST'])
def add_todo():
    todo = request.get_json()
    todos.append(todo)
    return jsonify(todos), 200

# DELETE /todos/<int:position>
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position >= len(todos) or position < 0:
        return jsonify({"error": "Invalid position"}), 400
    todos.pop(position)
    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(debug=True)
