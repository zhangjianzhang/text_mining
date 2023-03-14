from nltk.corpus.reader import CategorizedTaggedCorpusReader

creader = CategorizedTaggedCorpusReader('./cn_news_tagged/', '.*',cat_pattern = r'(.+)/.+txt')

from nltk import FreqDist

it_words = creader.words(categories=['IT'])

fdist_it = FreqDist(it_words)

import re

zh_char = re.compile(r'[\u4e00-\u9fa5]')

with open('./stopwords.txt') as f:
    stopwords = f.read().strip().split()
    
domain_stopwords = ['记者', '报道']

cleaned_it_words = filter(lambda item: len(item) > 1 and zh_char.findall(item) and item not in stopwords + domain_stopwords, it_words)

fdist_it = FreqDist(cleaned_it_words)

import matplotlib.pyplot as plt
# 正确显示中文和负号
plt.rcParams["font.sans-serif"] = ["SimHei"] 
plt.rcParams["axes.unicode_minus"] = False
# fdist_it.plot(50, cumulative=True, percents=True)
fdist_it.plot(50)