import nltk
from pymystem3 import Mystem
from stop_words import get_stop_words
import re
import json

zul = open("zuleikha", "r")
my_string = zul.read()
m = Mystem()
output = [word.strip() for word in m.lemmatize(my_string)]
output_new = [word for word in output if re.search ('[А-ЯЁа-яёA-Za-z]', word) != None]

stop_words = get_stop_words('russian')

filtered_text = [word for word in output_new if not word in stop_words]


word_fd = nltk.FreqDist(filtered_text)
# print(word_fd.most_common(20))

bigrams = list(nltk.bigrams(filtered_text))
fdist = nltk.FreqDist(bigrams)
print(fdist.most_common(10))

rustoday_1_data = []
with open("russia_today_1.jsonlines", "r") as read_file:
    for line in read_file:
        rustoday_1_data.append(json.loads(line))

manual_keywords = []
full_texts = []
for item in rustoday_1_data:
    manual_keywords.append(item['keywords'])
    full_texts.append(item['content'])
texts = str(full_texts)
m = Mystem()
# output = [word.strip() for word in m.lemmatize(texts)]
# output_new = [word for word in output if re.search ('[А-ЯЁа-яёA-Za-z]', word) != None]
#
# stop_words = get_stop_words('russian')
#
# filtered_text = [word for word in output_new if not word in stop_words]
#
#
# word_fd = nltk.FreqDist(filtered_text)
# print(word_fd.most_common(20))
#
# bigrams = list(nltk.bigrams(filtered_text))
# fdist = nltk.FreqDist(bigrams)
# print(fdist.most_common(10))
