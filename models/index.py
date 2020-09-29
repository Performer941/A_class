from models import db


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)  # 用户id
    nick_name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    email = db.Column(db.String(128), nullable=False)  # 邮箱
    qq = db.Column(db.String(11), unique=True, nullable=False)  # qq号
    move_mobile = db.Column(db.String(11), unique=True)  # 移动电话
    fixed_mobile = db.Column(db.String(15), unique=True)  # 固定电话
    gender = db.Column(  # 性别
        db.Enum(
            "MAN",  # 男
            "WOMAN"  # 女
        ),
        default="MAN"
    )
