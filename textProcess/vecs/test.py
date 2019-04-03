import pickle

filepath = 'wordVecs.pickel'
with open(filepath, 'rb') as f:
    wordVecs, emotionList = pickle.load(f)
print(len(wordVecs), len(emotionList))
print(wordVecs[100].shape, emotionList[100])
