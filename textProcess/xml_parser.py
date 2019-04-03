import xml
from xml import sax
import codecs
import numpy as np
import jieba
import matplotlib.pyplot as plt
from gensim.models import word2vec
import pickle

emotions = {'厌恶': 1, '悲伤': 2, '恐惧': 3, '惊讶': 4, '喜好': 5, '高兴': 6, '愤怒': 7, '无': 8}


# 时间 Mar 28th 10点22分
class WeiboSampleParser(sax.ContentHandler):
    def __init__(self):
        sax.ContentHandler.__init__(self)
        self.sentenceID = ""  # 句子编号递增
        self.emotionTag = False  # 是否有情感
        self.emotion_1_type = ""
        self.emotion_2_type = ""
        self.sentence = ""
        self.currentTag = ""
        self.sentenceID = 0
        self.maxSize = 0  # 最大尺寸
        self.str = ""  # 所有文本
        self.count = 0
        self.countALL = 0
        self.list = [0] * 180
        self.model = word2vec.Word2Vec.load('./word2vec_model/model')
        self.ALLVECS = []  # 存储所有向量
        self.emotionList = []
        self.emotionCount = [0] * 10  # 统计情感分布

    def startElement(self, tag, attributes):
        if tag == "sentence":  # 句子级文本情感分析
            self.currentTag = tag
            self.sentenceID = self.sentenceID + 1  # 从1开始计数
            # if 'emotion_tag' in attributes:
            #     if attributes['emotion_tag'] == 'N':
            #         self.emotionTag = False
            #     else:
            #         self.emotionTag = True
            if attributes['opinionated'] == 'N':
                self.emotion_1_type = '无'
            if 'emotion-1-type' in attributes:  # 测试某个key在字典中吗
                self.emotion_1_type = attributes['emotion-1-type']
            print(self.emotion_1_type)
            try:
                i = emotions[self.emotion_1_type]
                self.emotionList.append(i)
            except:
                i = 8
                self.emotionList.append(8)
            else:
                pass
            self.emotionCount[i] = self.emotionCount[i] + 1
        # if 'emotion-2-type' in attributes:
        #     self.emotion_2_type = attributes['emotion-2-type']
        # print(self.sentenceID)  # 测试用句子

    def endElement(self, tag):  # 将信息转化为矩阵
        if tag == 'sentence':
            # print(self.emotion_1_type)
            # print(self.sentence)
            cut = jieba.cut(self.sentence)
            str_out = ' '.join(cut).replace(',', '').replace('。', '').replace('？', '').replace('！', '') \
                .replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '') \
                .replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '') \
                .replace('’', '').replace('，', '').replace('\n', '').replace('/', '').replace('@', '').replace('?', '') \
                .replace('~', '').replace('(', '').replace(')', '').replace('=', '').replace('.', '').replace('／', '') \
                .replace('[', '').replace(']', '').replace('!', '').replace(':', '').replace('  ', ' ')
            # print(str_out)
            # print(str_out)
            str_list = list(str_out.split(' '))
            wordVec = []
            for word in str_list:
                try:
                    wordVec.append(self.model.wv.__getitem__(word))
                except:
                    wordVec.append(np.zeros(256))
                else:
                    pass
            # print(str_list, len(str_list))
            Vecs = np.asarray(wordVec)
            # print(Vecs)
            self.ALLVECS.append(Vecs)
            lenth = len(str_list)
            tempSize = lenth
            if (tempSize > 50):
                self.count = self.count + 1
            self.list[tempSize] = self.list[tempSize] + 1
            self.countALL = self.countALL + 1
            pass

    def characters(self, content):
        if self.currentTag == "sentence":
            self.sentence = content
            self.str = self.str + content + "\n"
            # print(self.sentence)

    def endDocument(self):  # 文档结束

        # with codecs.open('weibo_corpus_use_for_get_word2vec.txt', 'a', encoding='utf-8') as f:
        #     f.write(self.str)
        print(len(self.ALLVECS))
        print(len(self.emotionList))
        # 以2进制写入list
        filePath = './vecs/wordVecs.pickel'  # 存储序列化文件路径
        with open(filePath, 'wb') as f:
            pickle.dump((self.ALLVECS, self.emotionList), f, 3)
        # 读入 ALLVECS,emotionList=pickle.load(f)
        print(self.count)  # 统计超过的次数
        print('数据已写入')
        print("解析完成")
        print(self.countALL)
        print(self.list)
        # x = np.arange(0, 180)
        # y = np.array(self.list)
        x2 = np.arange(0, 10)
        y2 = np.array(self.emotionCount)
        # plt.plot(x, y)
        plt.plot(x2, y2)
        plt.show()

    def startDocument(self):
        print("开始解析")


def parse_xml():
    # 创建XmlReader
    paser = xml.sax.make_parser()

    # 关掉namespaces
    paser.setFeature(xml.sax.handler.feature_namespaces, 0)

    # 重写ContextHandler
    Handler = WeiboSampleParser()
    paser.setContentHandler(Handler)

    paser.parse("微博情绪标注语料.xml")

    # paser.parse("微博情绪分析测试数据.xml")
    #
    # paser.parse("微博情绪样例数据V5-13.xml")


# Mar 1 改写成为解析 微博情绪标注语料,xml
# 只保留情感 1
parse_xml()
