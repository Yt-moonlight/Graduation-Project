import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail


app = Flask(__name__)
app.config['SECRET_KEY'] = 'bGpjIGRlIHNlY3JldCBrZXk='
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
Bootstrap(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# 用户需登录时重定向的视图
login_manager.login_view = 'login'
# 设置message引导的bootstrap类型
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['SECURITY_EMAIL_SENDER'] = 'noreply@demo.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'yt952620701@gmail.com'
app.config['MAIL_PASSWORD'] = 'smbmchkdxnrezgfw'
mail = Mail(app)

from flaskblog import routes

