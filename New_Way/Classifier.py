import csv
import nltk
import NaiveBayesClassifier
lines = """
Donate Diore			    Email: donato@example.com
Chief Executive Officer		Office 800-555-5555
Broadlook Technoplogies		Cell : 414-555-5555
21140 Capitol Drive		    Fax   : 262-754-8081
Pewaukee WI 53072		    Blog www.idanato.com
http://www.broadlook.com
"""
sentences = nltk.sent_tokenize(lines)  # tokenize sentences
nouns = []  # empty to array to hold all nouns

for sentence in sentences:
    for word, pos in nltk.pos_tag(nltk.word_tokenize(str(sentence))):
        if (pos == 'NN'):
            nouns.append(word)


    file = open('D:\IFS\python_train\Position.csv', 'r')
    reader = csv.reader(file)
    feature_set = []

    for word, label in reader:
        feature_set.append((word, label))

    print(feature_set)

    cl = NaiveBayesClassifier(feature_set)
    print(nouns,"and entity is :")
    entity=cl.classify(nouns)
    print(entity)
    t=entity