import pprint

message = 'It was an unexpected rain in the evening and the people were rushing to find shelter.'
count = {}

for char in message.lower():
    count.setdefault(char, 0)
    count[char] += 1

pprint.pprint(count)
