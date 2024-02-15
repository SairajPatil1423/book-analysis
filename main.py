import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

with open("miracle_in_the_andes.txt","r",encoding="UTF-8") as file:
    book = file.read()


analyzer= SentimentIntensityAnalyzer()

analyzer.polarity_scores("i am too happy to anouce my package and excited about results of my exam")

