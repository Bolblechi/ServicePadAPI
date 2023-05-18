class UserSchema(ma.Schema):
    class Meta:
        fields = ("email", "fullname", "photo")