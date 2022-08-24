from flask import Flask, request, jsonify

app = Flask(__name__)

humans = []

#decoradores 
@app.route('/')
def hello_world():
    return '<h1>Welcome</h1>'


@app.route('/humans', methods=['GET'])
@app.route('/humans/<int:user_id>', methods=['GET'])
def handle_humans(user_id = None):
    if request.method == 'GET':
        if user_id is None:
            return humans , 200
        else:
            human = list(filter(lambda item: item["id"] == user_id, humans))
            return human, 200
    return humans, 405


@app.route('/humans', methods=['POST'])
def add_new_human():
    if request.method == 'POST':
        body = request.json
        if  body.get("name") is None:
            return {"message":"error propertie bad "} ,400
        if body.get("lastname") is None:
            return jsonify({"message":"error propertie bad "} ,400)
        
        body.update({"id": len(humans)+1})

        humans.append(body)
        return humans, 201


if __name__=="__main__":
    app.run(host='0.0.0.0', port="8000", debug=True)
# app.run(host="0.0.0.0", debug=True)