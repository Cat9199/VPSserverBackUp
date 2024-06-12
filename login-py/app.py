from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a random secret key in production
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)
CORS(app, resources={r"/*": {"origins": "*"}})

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

@app.route('/api/register', methods=['POST'])
def register():
      data = request.json
      hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
      new_user = User(name=data['name'], email=data['email'], phone=data['phone'], password=hashed_password)
      db.session.add(new_user)
      db.session.commit()
      return jsonify({'message': 'User registered successfully'}), 201

@app.route('/api/login', methods=['POST'])
def login():
      data = request.json
      user = User.query.filter_by(email=data['email']).first()
      if user and bcrypt.check_password_hash(user.password, data['password']):
            access_token = create_access_token(identity=user.id)
            return jsonify({'message': 'Login successful', 'access_token': access_token}), 200
      else:
            return jsonify({'message': 'Invalid email or password'}), 401

@app.route('/api/user', methods=['GET'])
@jwt_required()
def get_user_details():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    if user:
        return jsonify({'user': {'id': user.id, 'name': user.name, 'email': user.email, 'phone': user.phone, 'created_at': user.created_at, 'updated_at': user.updated_at}})
    else:
        return jsonify({'message': 'User not found'}), 404
if __name__ == '__main__':
    with app.app_context():
        db.drop_all()  # Drop existing tables
        db.create_all()  # Recreate the database tables
    app.run(debug=True)
