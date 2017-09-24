# -*- coding: utf-8 -*-
from flask import Flask, render_template
from app.exts import db, mako
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__,static_url_path='')
app.debug = True

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123@127.0.0.1:3306/movie"
import os

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///{}".format(os.path.join(os.path.dirname(__file__), 'movie.sqlite'))
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

import os
app.config["SECRET_KEY"] = os.urandom(24)
app.config["UP_DIR"] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")

mako.init_app(app)
db.init_app(app)

manage = Manager(app)

migrate = Migrate(app, db)

manage.add_command('db', MigrateCommand)

from app.home import home as home_blueprint
from app.admin import admin as admin_blueprint

app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix="/admin")


# 404页面
@app.errorhandler(404)
def page_not_found(error):
    return render_template("home/404.html"), 404


if __name__ == '__main__':
    manage.run()
