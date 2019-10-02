from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'posts'

    post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    body =  db.Column(db.String(1000), nullable=False)
    author = db.Column(db.String(200), nullable=False)



    def to_dict(self):


        return {
                "postId": self.post_id,
                "body": self.body,
                "author": self.author,
                "comments": [comment.comment_id 
                             for comment in Comment.query.filter_by(post_id=self.post_id)]
                }


class Comment(db.Model):
    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))
    body =  db.Column(db.String(1000), nullable=False)
    author = db.Column(db.String(200), nullable=False)


    def to_dict(self):


        return {
                "commentId": self.comment_id,
                "body": self.body,
                "author": self.author
                }





#####################################################################
# Helper functions


def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///take-home'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == '__main__':

    from server import app
    connect_to_db(app)
    print("Connected to DB  here.")
