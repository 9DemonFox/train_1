from gensim.models import word2vec
import pickle
import torch
from torch import nn
from torch.autograd import Variable
import numpy as np

torch.manual_seed(1)
EPOCH = 1
BATCH_SIZE = 32
TIME_STEP = 24
INPUT_SIZE = range(50)  # 输入大小不固定
LR = 0.01

model = word2vec.Word2Vec.load('../textProcess/word2vec_model/model')
print(model)
print(model.wv.get_vector('微博'))
sims = model.most_similar('关注', topn=10)
for key in sims:
    print(key)

dataPath = '../textProcess/vecs/wordVecs.pickel'  # 存储词向量和标签的list

with open(dataPath, 'rb') as f:
    wordVecs, emotionList = pickle.load(f)

print(len(wordVecs), len(emotionList))


class RNN(nn.Module):

    def __init__(self):
        super(RNN, self).__init__()
