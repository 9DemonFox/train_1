import jieba


def makeStopWord():  # 读入停用词
    with open('stop_words.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    stopWord = []
    for line in lines:
        words = jieba.cut(line, cut_all=False)
        for word in words:
            stopWord.append(word)
    return stopWord


with open('weibo_corpus_use_for_get_word2vec.txt', 'r', encoding='utf-8') as f:
    str = f.read()  # 读入数据
stopwords = makeStopWord()
print("读入停用词结束")
cut_str = list(jieba.cut(str))
print("分词结束")
count = 0
for word in cut_str:
    if word in stopwords:
        cut_str.remove(word)  # 去掉标点符号

print('标点符号去除完毕')
f = open('cut_clean_corpus', 'w', encoding='utf-8')
for word in cut_str:
    f.write(word + " ")
f.close()
print('文件写入完毕')
