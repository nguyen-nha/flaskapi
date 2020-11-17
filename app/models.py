from hashlib import md5

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    User_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(128), nullable=False)
    Email = db.Column(db.String(128), unique=True, nullable=False)
    Password = db.Column(db.String(128), nullable=True)
    Created_at = db.Column(db.DateTime)
    Post = db.relationship('Post', back_populates='user')

    def set_password(self, password):
        self.password = md5(password.encode('utf-8')).hexdigest()


class Post(db.Model):
    __tablename__ = 'post'

    Post_id = db.Column(db.Integer, primary_key=True)
    Title = db.Column(db.Char)
    Content = db.Column(db.String)
    Creat_at = db.Column(db.String)
    Update_at = db.Column(db.String)
    Ranking = db.Column(db.String)
    View_number = db.Column(db.String)
    user = db.relationship('User', back_populates='post')
    Tag = db.relationship('Tag', back_populates='post')


class Tag(db.Model):
    __tablename__ = 'tag'

    tag_id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(100))
    Created_at = db.Column(db.DateTime)
    Category = db.Column(db.String)
    Label = db.Colum(db.String)
    post = db.relationship('Post', back_populates='tag')

