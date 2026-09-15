# Note: install library by using command "python -m pip install textblob"

from textblob import TextBlob

text = input("Enter a Sentence: ")

analysis = TextBlob(text)

print("Polarity Score:", analysis.sentiment.polarity)

if analysis.sentiment.polarity > 0:
    print("Positive Sentiment")
elif analysis.sentiment.polarity < 0:
    print("Negative Sentiment")
else:
    print("Neutral Sentiment")