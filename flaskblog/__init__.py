# 여기에서 실행되는 모든 것을 flaskblog 라는 package가 된다.
# 하위 폴더에 존재하는 Module은 flaskblog.forms (= forms.py)
                            # flaskblog.models (= models.py) 
                            # flaskblog.routes (= routes.py) 
# 따라서 import 할 때 from 패키지명 import 컴포넌트의 형식을 사용한다.
# 예) from flaskblog import app

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '66cd7386a263e5d12cf3acb3c7d2a257'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskblog import routes