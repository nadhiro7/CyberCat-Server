from flask import Flask,jsonify,request
from extensions import db,jwt
from auth import auth_bp
from users.users import user_bp
from predict.router import predict_bp
from models.models import User,TokenBlocklist
import os
# from dataPreprocessing.Generating_dataset import generating_dataset
app = Flask(__name__)

app.config.from_prefixed_env()
# Database configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cyberCat2.db'  # SQLite database
app.config['SQLALCHEMY_ECHO'] = True
app.config['JWT_SECRET_KEY'] = "e6e8d46caa2bd47b8ff0b7aa"
db.init_app(app)
jwt.init_app(app)
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/users")
app.register_blueprint(predict_bp, url_prefix="/predict")

# load user
@jwt.user_lookup_loader
def user_lookup_callback(_jwt_headers, jwt_data):
    identity = jwt_data["sub"]

    return User.query.filter_by(username=identity).one_or_none()

@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_data):
    return jsonify({"message": "Token has expired", "error": "token_expired"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return (
        jsonify(
            {"message": "Signature verification failed", "error": "invalid_token"}
        ),
        401,
    )


@jwt.unauthorized_loader
def missing_token_callback(error):
    return (
        jsonify(
            {
                "message": "Request doesnt contain valid token",
                "error": "authorization_header",
            }
        ),
        401,
    )
@jwt.token_in_blocklist_loader
def token_in_blocklist_callback(jwt_header,jwt_data):
    jti = jwt_data['jti']

    token = db.session.query(TokenBlocklist).filter(TokenBlocklist.jti == jti).scalar()

    return token is not None

if __name__ == '__main__':

    app.run()
