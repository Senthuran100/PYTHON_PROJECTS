import re
text = 'Hi id hello some random text that can be anything'
match = re.search(r'(\w+) id',text)
if match:
    print match.group(1)