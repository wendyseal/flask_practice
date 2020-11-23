from common.ma import ma
from marshmallow import validate

#建立一個UserSchema來定義我們接收到使用者的請求參數所包含的元素
class UserSchema(ma.Schema):
    email = ma.Email(required=True)
    password = ma.Str(required=True, validate=[
                    validate.Length(min=6, max=36)],)
