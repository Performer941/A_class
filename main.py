from flask import Flask
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from models import db

app = Flask(__name__)
app.config.from_pyfile('config.ini')
# 初始化，只在第一次迁移数据库用
db.init_app(app)

# 添加迁移工具
manager = Manager(app)
# 生成migrate对象，用来数据库迁移
migrate = Migrate(app, db)
# 添加db命令
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    # app.run()
    manager.run()
