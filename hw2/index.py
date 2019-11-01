from flask import render_template
from flask.views import MethodView
import gbmodel

class Index(MethodView):
    def get(self):
        model = gbmodel.get_model()
        entries = [dict(name=row[0], address=row[1], special=row[2]) for row in model.select()]
        return render_template('index.html',entries=entries)
