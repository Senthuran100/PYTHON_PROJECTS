from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob
import nltk
import csv

File = open("D:\IFS\input\source.txt")  # open file
lines = File.read()  # read all lines
sentences = nltk.sent_tokenize(lines)  # tokenize sentences
nouns = []  # empty to array to hold all nouns

for sentence in sentences:
    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if ( pos == 'NNP'):
            nouns.append(word)
print("Nouns")
print nouns

f = open('D:\IFS\python_train\Names.csv')
csv_f = csv.reader(f)


dataset = []

for row in csv_f:
      dataset.append(({'entities': row[0]}, row[1]))

# print (dataset)

classifier = nltk.NaiveBayesClassifier.train(dataset)


for i in range(len(nouns)):

    mydata = {'entities':'nouns[i]'}
    print (i,nouns[i], classifier.classify(mydata))
    