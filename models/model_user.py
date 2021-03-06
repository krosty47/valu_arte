class UserModel():

    def toJson(user):
        return {"id": user.id, "email": user.email}

    def toJsonArray(items):
        list = []
        for item in items:
            list.append(UserModel.toJson(item))
        return list

    def jsonSchema():
        schema = {
            "type": "object",
            "properties": {
                "email": {"type": "string", "maxLength": 100},
                "password": {"type": "string"},
                "user_name": {"type": "string"},
                "hour_price": {"type": "integer"},
                "profit": {"type": "integer"},
                "mage_url": {"type": "string"}
            },
            "required": ["email"]
        }
        return schema
