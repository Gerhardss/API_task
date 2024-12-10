import requests
from flask import Flask, render_template, jsonify

app = Flask(__name__)
BASE_URL = "https://rvkg-api-ogzj.shuttle.app"

@app.route('/')
def index():
    response = requests.get(BASE_URL + "/posts")
    if response.status_code == 200:
        all_posts = response.json()
        return render_template("index.html", posts=all_posts)
    else:
        print("There is an ERROR!", response.status_code)
        return "Error!", response.status_code

@app.route('/users', methods=['GET'])
def users():
    response = requests.get(BASE_URL + "/users")
    if response.status_code == 200:
        users = response.json()
        return render_template("users.html", users=users)
    else:
        print("There is an ERROR!", response.status_code)
        return "Error!", response.status_code
    
@app.route('/posts', methods=['GET'])
def all_posts():
    response = requests.get(BASE_URL + "/posts")
    if response.status_code == 200:
        all_posts = response.json()
        return render_template("posts.html", posts=all_posts)
    else:
        print("There is an ERROR!", response.status_code)
        return "Error!", response.status_code

@app.route('/posts/<int:post_id>', methods=['GET'])
def get_post_by_id(post_id):
    response = requests.get(f"{BASE_URL}/posts/{post_id}")
    if response.status_code == 200:
        post = response.json()
        return render_template("post.html", post=post)
    else:
        return jsonify({"ERROR": "Post not found", "details": f"Post with id {post_id} not found"}), 404

@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Resource not found"}), 404

@app.errorhandler(500)
def server_error(e):
    return jsonify({"error": "Server error"}), 500

if __name__ == "__main__":
    app.run(debug=True)
