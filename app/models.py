from app import db, login_manager  # Импорт ГЛОБАЛЬНЫХ объектов из __init__
from flask_login import UserMixin

@login_manager.user_loader  # Теперь login_manager готов из app!
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    clicks = db.Column(db.Integer, default=0)