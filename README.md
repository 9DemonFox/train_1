#### 目录说明
    - train
          - environment
          |
          - LSTM
          |  -LSTM.py 长短期记忆模型      
          |  
          - LSTM_MNIST [LSTM实现MNIST手写数字的识别]:(https://blog.csdn.net/Jaster_wisdom/article/details/79919319)
          |  -mnist
          |  |  -
          |  |  -lstm_mnist.py 
          |  |  -dataLoader.py 封装数据集便于读取,并且把数据按照词向量长度排序，存入文件
          - others
          |
          - textProcess 语料库预处理
          |  - word2vec_model
          |  |  - model 存储产生的词向量 model   
          |  |  - test.py 测试添加短语进词向量是否成功
          |  - vecs 词向量 以list形式存储
          |  |  - wordVecs.pickel 由pickel保存的序列化文件 包括词向量和情感
          |  |  - 
          |  |  - test.py 测试能否读取词向量和情感词
          |  - cut_clean_corpus.txt 保存去除标点符号的数据
          |  - stop_words.txt 停用词
          |  - weibo_corpus_use_for_get_word2vec.txt 是未分词的语料库
          |  - cut_clean_corpus 是处理好了的语料库 包括分词、去停用词、去标点
          |  - corpus_word2vec 是存储词向量的
          |  - xml_parser.py 
              * 解析xml为纯文本
              * 解析xml为字典 Apr.1 修改为 解析微博情绪语料为矩阵的形式
          |  - word2vec.py 训练词向量
          - ./ 根目录 
          - README.md     
                  
#### 其它说明
#### 时间戳
     * Mar 30 
       * 完成分词处理，不能用for循环处理
     * Apr 1
       * 使用 微博情绪标注语料做训练和测试
       * 程序流程：读取句子和句子的情感标注->对句子进行分词->去标点->统计最长的句子
         ->以最长词数为维度->
       * 最长维度为164，与最小维度差距过大，会不会影响结果
       * 统计显示超过100的句子有20个，考虑删除100
       * LSTM并没有句子长度的需求，统一句子长度是为了并行计算的需求
       * 【在已有的model上添加语料】https://blog.csdn.net/u011010851/article/details/84313688
        # TODO 无法添加新词
       * 句子长度问题，每个batch中句子长度一致即可【统计句子长度】
       * 如何设计数据集，可以每次读入一批相同长度的数据，并且知道它们的标签
       * 一个数据集包含3个信息 词向量 情感 大小
       * python序列化对象进行存储 pickel
       * 文件顺序 cut_clean_corpus 对数据进行清洗-》word2vec 转化为词向量-》xmlParser 读取训练集和测试集
       * 通常用深度学习需要用padding的方法来处理词汇 https://zhuanlan.zhihu.com/p/34418001
       * 