import re
line = "senthuran.manoharan@gmail.com"
match = re.search(r'[\w\.-]+@[\w\.-]+', line)
print match.group(0)