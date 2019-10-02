from flask import Flask, jsonify, render_template, request
from model import connect_to_db, db, Post


app = Flask(__name__)

app.secret_key = "mama"


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/api/posts',  methods=["GET"])
def get_posts():


    return jsonify([
        post.to_dict()
        for post in Post.query.all()
    ])
                    

@app.route('/api/posts',  methods=["POST"])
def post_posts():


    body = request.form.get("body")
    author = request.form.get("author")


    new_post = Post(body=body,
                    author=author)

    db.session.add(new_post)
    db.session.commit()

 

    return jsonify(body=body,
                 author=author)


@app.route('/api/comment/<comment_id>',  methods=["GET"])
def get_comment(comment_id):
    comment = Comment.query.filter_by(comment_id=comment_id).first()
    return jsonify(comment.to_dict())
 
 

@app.route('/api/post/<post_id>', methods=["DELETE"])
def delete_posts(post_id):


    post_to_delete = Post.query.filter_by(post_id=post_id).first()
    db.session.delete(post_to_delete)
    db.session.commit()

    return("Done")






if __name__ == "__main__":


    app.debug = True

    connect_to_db(app)
 
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")