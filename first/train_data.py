train = {
    ('Colombo', 'location'),
    ('Kandy', 'location'),
    ('Kalutura', 'location'),
    ('Senthuran', 'person'),
    ("Manoharan", 'person'),
    ('Paris', 'location'),
    ('Shankar', 'person'),
    ("New York", 'location'),
    ('Gautam', 'person'),
    ('Raja', 'person'),
    ("Gampaha", 'location'),
    ("Wellawatte", 'location'),
    ("Kollupitiya", 'location'),
    ("Sunil", 'person'),
    ('Dhoni', 'person'),
    ('Ashwin', 'person'),
    ("Ranasinghe ", 'person'),
    ('Karunarathna', 'person'),
    ('Kamburadeniya', 'location'),
    ("California ", 'location'),
    ("Hong Kong", 'location'),
    ("MALAYSIA", 'location'),

}
test = [
     ('JOHN ', 'person'),
    ('JOSEPH', 'person'),
     ("CHRISTOPHER", 'person'),
    ("PAUL", 'person'),
    ("Fredrik ", 'person'),
    ("Michael", 'person'),
    ("SELANGOR", 'location'),
    ("AUSTRALIA", 'location'),
    ("HUNGARY", 'location'),
    ("AMERICA", 'location'),
    ("Sweden", 'location'),
    ("Munich", 'location'),
 ]

from textblob.classifiers import NaiveBayesClassifier
cl = NaiveBayesClassifier(train)
from textblob import TextBlob

blob = TextBlob("Gautam", classifier=cl)

blob.classify()

for s in blob.sentences:
    print(s)
    print(s.classify())
print("Accuracy: {0}".format(cl.accuracy(test)))