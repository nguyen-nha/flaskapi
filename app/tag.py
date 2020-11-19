import json
import uuid

from flask import Flask, request

from demo.app.models import Tag, db

app = Flask(__name__)


def create_tag():
    if request.method == ['POST']:
        tag_id = uuid.uuid4()
        name = request.json['Name']
        update_at = request.json['Update_at']
        category = request.json['Category']
        label = request.json['label']
        new_tag = Tag(tag_id,name, update_at, category, label)
        db.session.add(new_tag)
        db.session.commit()
    return (
         json.dumps(
             {
                 "message": "tao tag thanh cong"
             }
         )
     )
def update_tag():
    tag = Tag.query.get(id)
    if request.method == ['POST']:
        name = request.json['Name']
        update_at = request.json['Update_at']
        category = request.json['Category']
        label = request.json['label']
        new_tag = Tag(tag,name, update_at, category, label)
        db.session.add(new_tag)
        db.session.commit()
    return (
         json.dumps(
             {
                 "message": "update thanh cong"
             }
         )
     )
def delete_tag(id):
    tag = Tag.query.get(id)
    if request.method == 'DELETE':
        db.session.delete(tag)
        db.session.commit()
    return (
        json.dumps(
            {
                "message": "xoa thanh cong"
            }
        )
    )
