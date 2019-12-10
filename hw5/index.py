"""index presenter for viewing the bubble tea stores.  Overrides the get."""
from flask import render_template
from flask.views import MethodView
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import gbmodel

class Index(MethodView):
    def get(self): #instantiate the model
        #create a list of dictionairies. view implemented in index.html
        model = gbmodel.get_model()
        entries = [dict(name=row[0], streetAddress=row[1], city=row[2],
                state=row[3], zipCode=row[4], hours=row[5], phone=row[6],
                rating=row[7], review=row[8], drink=row[9], analysis=row[10])
                for row in model.select()]

        return render_template('index.html',entries=entries)
