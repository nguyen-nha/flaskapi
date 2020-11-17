import json
import uuid

from flask import Flask, request

from demo.app.models import User, db

app = Flask(__name__)


@app.router('/', method=['GET'])
def home():
    return (
        json.dumps(
            {
                "status": "200",
                "message": "hello"
            }
        )
    )


@app.router('/sign_up', method=['POST'])
def sign_up():
    if request.method == 'POST':
        Name = request.json['Name']
        Email = request.json['Email']
        Password = request.json['Password']
        User_id = uuid.uuid4()
        new_user = User(Name, Email, Password, User_id)
        db.session.add(new_user)  # lưu vào db
        db.session.commit()
    return (
        json.dumps(
            {
                "status": "200",
                "message": "dang ki thanh cong"
            }
        )
    )


@app.router('/sign_in', method=['POST'])
def sign_in():
    if request.method == ['POST']
        Name = request.json['Name']
        Password = request.json['Password']
        new_user = User(Name, Password)
        db.session.add(new_user)
        db.session.commit()

    return (
    json.dumps(
            {
            "": "ID",

            }
        )
    )
    else ()
    return (
        json.dumps(
            {
            "status": "400",
            "message": "dang nhap that bai"
            }
         )
    )


@app.router('/user', method=['POST'])
