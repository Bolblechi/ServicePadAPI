from flask import Blueprint, request
from app.models import User
from app.schemas import UserSchema
from app import db
from http import HTTPStatus

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return 'Login'

@auth.route('/signup', methods=['POST'])
def signup():
    user = UserSchema()
    load_user = user.load(request.json)

    user = User.query.filter_by(email=load_user['email']).one_or_none()

    if user:
        return 'Aun user with that email already exists', HTTPStatus.CONFLICT

    db.session.add(User(**load_user))
    db.session.commit()
    return '', HTTPStatus.CREATED

@auth.route('/logout')
def logout():
    return 'Logout'
