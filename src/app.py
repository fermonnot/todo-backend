from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [{ "label": "Primera Tarea", "done": False }]

#decoradores 
@app.route("/todos", methods = ['GET'])
def get_todos():
    json_text = jsonify(todos)
    print('this are the pending task')
    return json_text

@app.route("/todos", methods = ['POST'])
def add_todos():
    request_body = request.get_json(force=True)
    print('New task added', request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route("/todos/<int:index>", methods = ["DELETE"])
def delete_todos(index):
    print('task eliminated', index)
    todos.pop(index)
    return jsonify(todos)


if __name__=="__main__":
    app.run(host='127.0.0.1', port="8000", debug=True)