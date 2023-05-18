from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import pre_load


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User

    @pre_load
    def hash_password(self, in_data, **kwargs):
        in_data['password'] = generate_password_hash(in_data['password'], method='sha256')

        return in_data
