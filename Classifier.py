import pickle
from nltk.util import ngrams

classifier = pickle.load(open("C:\Users\Melwin/nltk_data/classifiers/NFL_sklearn.MultinomialNB.pickle"))
words = ['@JaredGoff16 ','@YasielPuig  ','bay  ','area ',' disowns  ','you']
feats = dict([(word, True) for word in words + ngrams(words, 2)])
print classifier.classify(feats)