from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
    ('photographer', 'pos'),
    ('Chief Executives', 'pos'),
    ('Doctor', 'pos'),
    ('Engineer', 'pos'),
    ("Lawyers", 'pos'),
    ('Accountant', 'pos'),
    ('Programmer', 'pos'),
    ("Designer", 'pos'),
    ('Architect', 'pos'),
    ('plumber', 'pos')
]
test = [
    ('Senthuran', 'neg'),
    ('Clerk', 'pos'),
    ("I ain't feeling dandy today.", 'neg'),
    ("Managers", 'pos'),
    ('Colombo', 'neg'),
    ("Teacher", 'pos')
]

cl = NaiveBayesClassifier(train)

# Classify some text
print(cl.classify("Colombo"))
print(cl.classify("I don't like their pizza."))

# Classify a TextBlob
blob = TextBlob("The beer was amazing. But the hangover was horrible. "
                "My boss was not pleased.", classifier=cl)
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())

# Compute accuracy
print("Accuracy: {0}".format(cl.accuracy(test)))

# Show 5 most informative features
cl.show_informative_features(5)