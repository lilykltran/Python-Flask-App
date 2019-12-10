#Lily Tran.  Derived from Wuchang's Guestbook app v3
"""
A simple bubbletea flask app.  Modified to run on port 8000 instead of 5000. Labeling and routing requests.
"""
import flask
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
from index import Index #import presenter index
from sign import Sign #import presenter sign
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
 

app = flask.Flask(__name__)       # our Flask app

@app.route('/')
def home():
    return render_template('home.html')
 
app.add_url_rule('/index/',
                 view_func=Index.as_view('index'),
                 methods=["GET"]) #register methods viewer supports

#post handling for sign.
app.add_url_rule('/sign/', 
                 view_func=Sign.as_view('sign'),
                 methods=['GET', 'POST'])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8000, debug=True)
