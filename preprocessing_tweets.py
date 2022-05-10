import re
import numpy as np
import csv
from spellchecker import SpellChecker
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
spell = SpellChecker()


def preprocess(tweet):
    stopwords = ["for", "on", "an", "a", "of", "and", "in", "the", "to", "from"]
    if type(tweet) is float:
        return ""
    temp = tweet.lower()
    temp = re.sub("'", "", temp)  # to avoid removing contractions in english
    temp = re.sub("@[A-Za-z0-9_]+", "", temp)
    temp = re.sub("#[A-Za-z0-9_]+", "", temp)
    temp = re.sub(r'http\S+', '', temp)
    temp = re.sub('[()!?]', ' ', temp)
    temp = re.sub('\[.*?\]', ' ', temp)
    temp = re.sub("[^a-z0-9]", " ", temp)
    temp = temp.split()
    temp = [w for w in temp if not w in stopwords]
    temp = " ".join(word for word in temp)
    return temp


def spellCheck(tweet):
    temp = tweet.split()
    temp = [spell.correction(word) for word in temp]
    temp = " ".join(word for word in temp)
    return temp


def lemmatize(tweet):
    temp = tweet.split()
    temp = [lemmatizer.lemmatize(word) for word in temp]
    temp = " ".join(word for word in temp)
    return temp


def main():
    with open('Twitter Political Corpus.txt', encoding='utf8') as file:
        tweets = file.read()
        tweets = tweets.split('\n')

    with open('politicalTweets.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['data', 'target'])
        for tweet in tweets:
            tweet = tweet.split('\t')
            x = preprocess(tweet[1])
            x = spellCheck(x)
            x = lemmatize(x)
            if tweet[0] == 'NOT':
                y = 0
            else:
                y = 1
            writer.writerow([x, y])


if __name__ == '__main__':
    main()
