from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/users', methods=['GET'])
def getUsers():
    if request.method == 'GET':
        return jsonify({'payload': 'success'})

@app.route('/user', methods=['POST'])
def PostUser():
    if request.method == 'POST':
        return jsonify({'payload': 'success'})

@app.route('/user', methods=['DELETE'])
def deleteUser():
    if request.method == 'DELETE':
        return jsonify({'payload': 'success'})

@app.route('/user', methods=['PUT'])
def putUsers():
    if request.method == 'PUT':
        return jsonify({'error': False,'payload': 'success'})

@app.route('/api/v1/users', methods=['GET'])
def getUsersH5():
    if request.method == 'GET':
        return jsonify({'payload':[]})
    
@app.route('/api/v1/user', methods=['POST'])
def PostUser2():
        if request.method == 'POST':
            email = request.args.get('email')
            name = request.args.get('name')
            respuesta = {
                'payload': {
                    'email':email,
                    'name':name,
                } 
            }    
        return respuesta


@app.route('/api/v1/user/add', methods=['POST'])
def PostUser3():
        email = request.form.get('email')
        name = request.form.get('name')
        id = request.form.get('id')
        respuesta = {
            'payload': {
                'email':email,
                'name':name,
                'id':id,
            } 
        }    
        return respuesta

@app.route('/api/v1/user/create', methods=['POST'])
def PostUser4():
        data = request.get_json()

        email = data.get('email')
        name = data.get('name')
        id = data.get('id')

        respuesta = {
            'payload': {
                'email':email,
                'name':name,
                'id':id,
            } 
        }    
        return respuesta



if __name__ == "__main__":
    app.run(debug=True)