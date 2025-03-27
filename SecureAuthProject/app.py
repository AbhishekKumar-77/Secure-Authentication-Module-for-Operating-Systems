from flask import Flask, render_template, request, jsonify
import Secure_Auth_Module as auth

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    if auth.save_user(data['username'], auth.hash_password(data['password'])):
        return jsonify({'message': 'Registration Successful'}), 200
    return jsonify({'message': 'Registration Failed'}), 400

@app.route('/otp-login', methods=['POST'])
def otp_login():
    data = request.json
    if auth.validate_user(data['username'], data['password']):
        otp = auth.generate_otp()
        return jsonify({'message': f'OTP sent: {otp}'}), 200
    return jsonify({'message': 'Invalid Credentials'}), 400

@app.route('/face-login', methods=['POST'])
def face_login():
    data = request.json
    if auth.validate_user(data['username'], data['password']):
        if auth.face_recognition():
            return jsonify({'message': 'Face Recognition Successful'}), 200
        return jsonify({'message': 'Face Recognition Failed'}), 400
    return jsonify({'message': 'Invalid Credentials'}), 400

if __name__ == '__main__':
    app.run(debug=True)
