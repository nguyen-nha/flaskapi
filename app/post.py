import uuid
import json

from flask import app, request

from demo.app.models import Post, db


@app.router('/post', method=['POST'])
def creat():
        if request.method == ['POST']
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
            "Post_id",
            "Title"
             }
         )
    )
@app.router('/repair_post', method=['PUT'])
def repair():
        if request.method == ['PUT']
            Post_id = uuid.uuid4()
            Title = request.json['Title']
            Content = request.json['Content']
            Update_at = request.json['Update_at']
            Ranking = request.json['Ranking']
            new_post = Post(Post_id, Title,Content,Update_at, Ranking)
            db.session.add(new_post)
            db.session.commit()
        if 
        return (
            json.dumps(
                {
                    "Post_id",
                    "message": "chinh sua thanh cong"
                }
            )
        )
@app.router('/delete_post', method=['PUT'])
def delete():
        if request.method == ['PUT']
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
                    "Post_id",
                    "message": "xoa thanh cong"
                }
            )
        )
