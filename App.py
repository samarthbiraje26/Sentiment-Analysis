from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    blob = TextBlob(text)

    sentiment = blob.sentiment
    polarity = sentiment.polarity #determines how politely a person is speaking . positive sentiment if value > 0, negative sentiment if value < 0.

    if polarity > 0:
        sentiment_category = 'Positive Sentiment'
    elif polarity < 0:
        sentiment_category = 'Negative Sentiment'
    else:
        sentiment_category = 'Neutral Sentiment'

    return sentiment_category

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None

    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_sentiment(text)

    return render_template('index.html', sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)