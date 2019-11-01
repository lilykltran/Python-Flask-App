"""
A simple bubbletea flask app.
"""
import flask
from flask.views import MethodView
from index import Index
from sign import Sign

app = flask.Flask(__name__)       # our Flask app


app.add_url_rule('/',
                 view_func=Index.as_view('index'),
                 methods=["GET"])

app.add_url_rule('/sign/',
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])

"""
@app.route('/')
def index():
    return layout.html
"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
