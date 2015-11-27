from flask import Flask
from resources.CommentResources import comment_route
from resources.FollowerResources import follower_route
from resources.IndexResources import index_route
from resources.ProblemResources import problem_route
from resources.TestResource import test_route
from resources.UserResouces import user_route

app = Flask(__name__)
app.register_blueprint(index_route)
app.register_blueprint(user_route)
app.register_blueprint(problem_route)
app.register_blueprint(comment_route)
app.register_blueprint(follower_route)
app.register_blueprint(test_route)

if __name__ == '__main__':
    app.run()
