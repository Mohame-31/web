from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# نموذج البيانات
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

# إنشاء قاعدة البيانات
with app.app_context():
    db.create_all()

# واجهة إضافة منشور
@app.route('/add', methods=['POST'])
def add_post():
    data = request.get_json()
    new_post = Post(user=data['user'], content=data['content'])
    db.session.add(new_post)
    db.session.commit()
    return jsonify({'message': 'تمت الإضافة بنجاح!'})

# واجهة جلب المنشورات
@app.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    posts_list = [{'user': post.user, 'content': post.content} for post in posts]
    return jsonify(posts_list)

if __name__ == '__main__':
    app.run(debug=True)
