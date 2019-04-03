from gensim.models import word2vec
import logging

sentences = word2vec.LineSentence('cut_clean_corpus.txt')

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.INFO)

# 可更改训练模型
model = word2vec.Word2Vec(sentences, window=5, size=256)

model.save('./word2vec_model/model')

# 对应的加载方式
# model2 = word2vec.Word2Vec.load('搜狗新闻.model')
# 以一种c语言可以解析的形式存储词向量# model.save_word2vec_format(u"书评.model.bin", binary=True)
# 对应的加载方式# model_3 =word2vec.Word2Vec.load_word2vec_format("text8.model.bin",binary=True)


# 如何训练新词 http://qiuqingyu.cn/2017/03/14/Word2vec训练好的模型中加入新词/?tdsourcetag=s_pctim_aiomsg
