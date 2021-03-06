from sentistrength import PySentiStr

# Define sentistrength and the jar and text files that make up Sentistrength
senti = PySentiStr()
senti.setSentiStrengthPath("../SentiStrengthCom.jar")
senti.setSentiStrengthLanguageFolderPath("../Senti")


def get_sentiment_score(text):
    text = text.lower()
    result = senti.getSentiment(text, score='scale')
    return result[0]
