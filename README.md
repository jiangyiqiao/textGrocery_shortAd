# TextGrocery_shortAd_Classification
## 微信广告正负样本分类
参考https://github.com/2shou/TextGrocery.git
## Dependencies
Only test under Unix-based System

    $ pip install tgrocery

正样本：

* xx,xxx,xxxxxxxxx

负样本：

* 微信公众号 AppSo，回复「钱包」看看微信钱包这 6 个秘密使用技巧
 
* 微信号：wszs1981
 
* 长按二维码关注
 
其中，训练集正负样本各1W+，测试集样本各5K+

训练数据集：data/train/tgrocery_train.txt

测试数据集：data/test/tgrocery_test.txt


输入数据为未分词的带标签数据，数据预处理:

    python data/train/pre_processing.py
    python data/test/pre_progressing.py

训练模型：
   
    python train_model.py

    Building prefix dict from the default dictionary ...
    Loading model from cache /tmp/jieba.cache
    Loading model cost 0.192 seconds.
    Prefix dict has been built succesfully.
    ***.**
    optimization finished, #iter = 18
    Objective value = -554.355654
    nSV = 9239
    True



测试模型：
   
    python test_model.py

## result

    # 0 : ad     1 : not_ad 

    {u'1': 4973, u'0': 4115}
    {u'1': 5021, u'0': 4160}
    {'1': 5018, '0': 4163}
    1:	 precision:0.991032	 recall:0.990440	 f:0.990736
    0:	 precision:0.988470	 recall:0.989183	 f:0.988826


