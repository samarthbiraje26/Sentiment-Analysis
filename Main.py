from textblob import TextBlob

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

text = input("Enter your text : ")
result = analyze_sentiment(text)
print(f"Sentiment : {result}")