from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from demo.app.user import sign_up, sign_in, update_user
from demo.app.post import create_post, repair_post,delete
from demo.app.tag import create_tag


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///apidb.db'

    app.add_url_rule("/sign_up", "sign_up", sign_up, methods=["POST"])
    app.add_url_rule("/sign_in", "sign_in", sign_in, methods=["POST"])
    app.add_url_rule("/update_user", "update_user", update_user, methods=["POST"])
    app.add_url_rule("/create_post", "create_post", create_post, methods=["POST"])
    app.add_url_rule("/repair_post", "repair_post", repair_post, methods=["POST"])
    app.add_url_rule("/delete_post", "delete", delete, methods=["DELETE"])
    app.add_url_rule("/create_tag", "create_tag", create_tag, methods=["POST"])


    db = SQLAlchemy(app)
    db.create_all()

    return app

server = create_app()

if __name__ == '__main__':
    server.run(debug=True)
