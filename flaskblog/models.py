from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    
    # backref 는 Post class에 Column을 새로 추가(아래 코드에서는 author라는 Column)하는것과 비슷한 역할. 
    # backref를 사용함으로써 Post가 생성되었을 때 We can simply use this 'author' attribute to get the user who created the post.
    # lazy argument just defines when SQLalchemy loads the data from database. So 'True' means that SQLalchemy will load the data
    # as necessary in one go. This is conveninet because with this relationship we'll be able to simply use this post attribute
    # to get all of the post created by an individual user. Notice that this is a relationship not a column. If we would actually
    # look at our actual database structure in some kind of SQL client, we wouldn't see this 'posts' column here. This is actually ust running an
    # additional query at the background that will get all of the posts this user has created.

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # ForeignKey에 들어가는 attiribute가 소문자로 user임에 주의.
    # In the user model, we are referencing the actual post class, and in the foreign key we are actually referecing the table and the column name.
    # So it's a lower case. So the user model automatically has this table name set to lower case 'user', and the post model will have a table name
    # automatically set to lower case 'post'. If you want to set your own table names, then you can set a specific table name atttribute.
    # but since our models are pretty simple, we'll just leave those as the default lower case value.

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"