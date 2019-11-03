"""sign presenter for inserting a new bubble tea store"""
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['name'], request.form['streetAddress'], request.form['city'], request.form['state'], request.form['zipCode'], request.form['hours'], request.form['phone'], request.form['rating'], request.form['review'], request.form['drink'])
        return redirect(url_for('index'))
