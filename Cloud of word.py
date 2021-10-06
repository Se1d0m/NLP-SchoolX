import re
from collections import Counter
import pymorphy2
from wordcloud import WordCloud
import matplotlib.pyplot as plt

doc = open('F:\sketch\poem.txt', 'r', encoding='utf-8')
outputList = [line.strip() for line in doc]
outputStr = ' '.join(outputList).lower()
resultList = re.findall(r'\w+',outputStr)
resultStr = ' '.join(resultList)
morph = pymorphy2.MorphAnalyzer()
words = []
for word1 in resultList:
    p = morph.parse(word1)[0]
    words.append(p.normal_form)
stopWords = ['это', 'как', 'так', 'и', 'в', 'над', 'к', 'до', 'не', 'на', 'но', 'за', 'то', 'с', 'ли', 'а', 'во', 'от', 'со', 'для', 'о', 'же', 'ну', 'вы', 'бы', 'что', 'кто', 'он', 'она', 'по', 'или', 'из', 'мы', 'они', 'этот', 'я', 'у', 'вы', 'только', 'чтобы', 'можно', 'при', 'если', 'после', 'он', 'т','такой', 'есть', 'когда']
result = []
for word2 in words:
    if word2 not in stopWords:
        result.append(word2)
resultCoW = ' '.join(result)
cnt = Counter()
for word3 in result:
    cnt[word3] += 1
print(cnt)

wordcloud = WordCloud(background_color = 'white').generate(resultCoW)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()