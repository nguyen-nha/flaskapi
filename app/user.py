import json
import uuid

from flask import Flask, request

from demo.app.models import User, db

app = Flask(__name__)

def sign_up():
    if request.method == 'POST':
        name = request.json['Name']
        email = request.json['Email']
        password = request.json['Password']
        user_id = uuid.uuid4() # sinh ID
        new_user = User(name, email, password, user_id) # lưu vào db
        db.session.add(new_user)
        db.session.commit()
    return (
        json.dumps(
            {
                "message": "dang ki thanh cong"
            }
        )
    )

def sign_in():
    if request.method == ['POST']:
        name = request.json['Name']
        password = request.json['Password']
        registered_user = User.query.filter_by(Name=name,Password=password).first()
        if registered_user is None:
            return (
                json.dumps(
                    {
                        "status": "500",
                        "message": "Sai ten dang nhap hoac mat khau"
                    }
                )
            )
        return (
            json.dumps(
                {
                    "status": "200",
                    "message": "dang nhap thanh cong"
                }
            )
        )

def update_user():
    user = user.query.get(id)
    if request.method == 'POST':
        name = request.json['Name']
        email = request.json['Email']
        password = request.json['Password']

        new_user = User(name, email, password) # lưu vào db
        db.session.add(new_user)
        db.session.commit()
    return (
        json.dumps(
            {
                "message": "update thanh cong"
            }
        )
    )



