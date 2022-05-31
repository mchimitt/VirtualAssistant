import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import csv


# some explanation stuff to better my own understanding (skip if you want haha):
# OVERALL USES NAIVE BAYES CLASSIFIER
# tf-idf stands for term frequency-inverse document frequency
# it is a statistical measure that evaluates how relevant a word is to a document
# in a collection of documents
# so in this case, we use tf-idf on the text to determine topic of the text based
# on the key words using this relevancy scoring system
# cool stuff


# Class that identifies intents
class IntentClassifier:
    def __init__(self):
        # read the csv file with the data
        self.data = pd.read_csv('.\intent_classification\intents.csv')  # WHEN TESTING MAKE THIS '.\intents.csv
        # BUT WHEN RUNNING THE ACTUAL PROGRAM MAKE THIS .\intent_classification\intents.csv
        self.train()  # trains everytime an instant of IntentClassifier is made

    def train(self):
        # defining x_train and y_train to be the text and intent data respectively
        x_train, y_train = self.data['text'], self.data['intent']

        # a CountVectorizer() transforms given text (x_train) into a vector based
        # on frequency of each word that occurs in the entire text (x_train)
        self.count_vect = CountVectorizer()
        x_train_counts = self.count_vect.fit_transform(x_train)

        # TfidfTransformer() computes word counts using a CountVectorizer and then
        # computes inverse document frequency (idf) to then compute tf-idf scores.
        tfidf_transformer = TfidfTransformer()
        # Calculates the tf-idf for the text
        x_train_tfidf = tfidf_transformer.fit_transform(x_train_counts)

        self.clf = MultinomialNB().fit(x_train_tfidf, y_train)

    def predict(self, text):
        return self.clf.predict(self.count_vect.transform([text]))[0]



