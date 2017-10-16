from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent = """JOHN JONES
MARKETING DEPARTMENT
10-123 1/2 MAIN STREET NW
MONTREAL QC  H3Z 2Y7
Canada"""

stop_words = set(stopwords.words('english'))

word_tokens = word_tokenize(example_sent)

filtered_sentence = [w for w in word_tokens if not w in stop_words]

filtered_sentence = []

for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)

print(word_tokens)
print(filtered_sentence)
