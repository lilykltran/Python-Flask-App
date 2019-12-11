"""sign presenter for inserting a new bubble tea store"""
from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types

# Instantiates a client
# [START language_python_migration_client]
client = language.LanguageServiceClient()
# [END language_python_migration_client]

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')

    def post(self):
        """
        Accepts POST requests, and processes the form. Returns sentiment analysis of the review.
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
 
        text = request.form['review']
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        sentiment = client.analyze_sentiment(document=document).document_sentiment

        """
        Score of the sentiment ranges between -1.0 (negative) and 1.0 (positive) and corresponds to the overall emotional leaning of the text.
        Magnitude indicates the overall strength of emotion (both positive and negative) within the given text, between 0.0 and +inf."""

        analysis = ''
        if(sentiment.score > 0.30 and sentiment.magnitude > 0):
            analysis = 'positive'
        elif(sentiment.score < -.30 and sentiment.magnitude > 0):
            analysis = 'negative'
        elif(sentiment.score > -.30 and sentiment.score < 0.30 and sentiment.magnitude < 1.5):
            analysis = 'neutral'
        elif(sentiment.magnitude > 1.5):
            analysis = 'mixed'
            
        print('Text: {}'.format(text))
        print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
       
        model.insert(request.form['name'], request.form['streetAddress'],
                request.form['city'], request.form['state'],
                request.form['zipCode'], request.form['hours'],
                request.form['phone'], request.form['rating'],
                request.form['review'], request.form['drink'], analysis)
        return redirect(url_for('index'))
