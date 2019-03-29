import xml
from xml import sax
import codecs


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
        self.str = ""  # 所有文本

    def startElement(self, tag, attributes):
        if tag == "sentence":
            self.currentTag = tag
            self.sentenceID = self.sentenceID + 1
            if 'emotion_tag' in attributes:
                if attributes['emotion_tag'] == 'N':
                    self.emotionTag = False
                else:
                    self.emotionTag = True
            if 'emotion-1-type' in attributes:  # 测试某个key在字典中吗
                self.emotion_1_type = attributes['emotion-1-type']
            if 'emotion-2-type' in attributes:
                self.emotion_2_type = attributes['emotion-2-type']
            # print(self.sentenceID)  # 测试用句子

    def endElement(self, tag):
        pass

    def characters(self, content):
        if self.currentTag == "sentence":
            self.sentence = content
            self.str = self.str + content + "\n"
            # print(self.sentence)

    def endDocument(self):  # 文档结束
        with codecs.open('weibo_corpus_use_for_get_word2vec.txt', 'a', encoding='utf-8') as f:
            f.write(self.str)

        print('数据已写入')
        print("解析完成")

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

    paser.parse("微博情绪分析测试数据.xml")

    paser.parse("微博情绪样例数据V5-13.xml")
