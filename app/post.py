import uuid
import json

from flask import app, request

from demo.app.models import Post, db


def create_post():
        if request.method == ['POST']:
            Post_id = uuid.uuid4()
            Title = request.json['Title']
            Content = request.json['Content']
            Update_at = request.json['Update_at']
            Ranking = request.json['Ranking']
            new_post = Post(Post_id, Title, Content, Update_at, Ranking)
            db.session.add(new_post)
            db.session.commit()
        return (
             json.dumps(
            {
            "message" : "thanh cong"
             }
         )
    )

def repair_post():
        if request.method == ['PUT']:
            Title = request.json['Title']
            Content = request.json['Content']
            Update_at = request.json['Update_at']
            Ranking = request.json['Ranking']
            new_post = Post( Title,Content,Update_at, Ranking)
            db.session.add(new_post)
            db.session.commit()
            return (
            json.dumps(
                {
                    "message": "chinh sua thanh cong"
                }
                    )
                )
        return (
            json.dumps(
                    {
                    "message": "chinh sua thanh cong"
                    }
                    )
                )


def delete_post():
        if request.method == ['DELETE']:
            Post_id = uuid.uuid4()
            Title = request.json['Title']
            Content = request.json['Content']
            Update_at = request.json['Update_at']
            Ranking = request.json['Ranking']
            new_post = Post(Post_id, Title,Content,Update_at, Ranking)
            db.session.add(new_post)
            db.session.commit()
        return (
            json.dumps(
                {
                    "message": "xoa thanh cong"
                }
            )
        )
