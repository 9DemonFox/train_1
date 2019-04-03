import pickle
import matplotlib.pyplot as plt
import numpy

emotions = {'厌恶': 1, '悲伤': 2, '恐惧': 3, '惊讶': 4, '喜好': 5, '高兴': 6, '愤怒': 7, '无': 8}
dataPath = '../textProcess/vecs/wordVecs.pickel'  # 存储词向量和标签的list
sorted_dataPath = '../textProcess/vecs/sorted_wordVecs.pickel'


# with open(dataPath, 'rb') as f:
#     wordVecs, emotionList = pickle.load(f)
#
# print(len(wordVecs), len(emotionList))
#
# y = [0] * 180
# print(wordVecs[0].shape[0])
# count = 0
# total = len(wordVecs)


# 将情感排序
def sort_by_length(wvs, emogs):
    total = len(wvs)
    for i in range(total - 2):
        minimum = i  # 记录最小的位置
        for j in range(i + 1, total - 1):
            if wvs[j].shape[0] < wvs[minimum].shape[0]:
                minimum = j
        if i != minimum:
            temp1 = wvs[i]
            wvs[i] = wvs[minimum]
            wvs[minimum] = temp1
            temp2 = emogs[i]
            emogs[i] = emogs[minimum]
            emogs[minimum] = temp2
    return wvs, emogs


def dump_sorted_data(w, e):
    with open(sorted_dataPath, 'wb') as f:
        pickle.dump((w, e), f, 3)
    print("存入数据完成")


def load_sorted_data():
    with open(sorted_dataPath, 'rb') as f:
        w, e = pickle.load(f)
    return w, e


# 对 wordVecs.pickel进行排序并且存入

# w, e = sort_by_length(wordVecs, emotionList)  # APR 3
# dump_sorted_data(w, e)  # APR 3


# 99%的数据都是小于64的
w, e = load_sorted_data()
print(len(e))
for ii in range(len(w)):
    if w[ii].shape[0] > 64:
        print(ii)
        print(ii / len(w))
        break


# 获取少于某定长的数据 99%的数据短于64
def get_shorter_than_length_data(length, w, e):
    for ii in range(len(w)):
        if w[ii].shape[0] > length:
            break
    return w[:ii], e[:ii]  # 切片操作


w, e = get_shorter_than_length_data(64, w, e)
print(len(w))
