from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db
from views import index_blu, user_blu

app = Flask(__name__)
app.config.from_pyfile('config.ini')
app.register_blueprint(index_blu)
app.register_blueprint(user_blu)

# 初始化，只在第一次迁移数据库用
db.init_app(app)

# 添加迁移工具
manager = Manager(app)
# 生成migrate对象，用来数据库迁移
migrate = Migrate(app, db)
# 添加db命令
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    # app.run()
    manager.run()
