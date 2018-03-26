# coding: utf-8

from tgrocery import Grocery

grocery = Grocery('models')
#加载模型
grocery.load()

labels_right = []
texts = []
labels_predict = []
with open("data/test/tgrocery_test.txt") as fr:
    for line in fr:
        line = line.decode("utf-8").rstrip()
        label_right=line.split("\t")[0]
        labels_right.append(label_right)
        text=line.split("\t")[1]
        texts.append(text)
        label_predict=grocery.predict(text)
        labels_predict.append(label_predict)
        print ("文本: ")
        print (line)
        print ("真实label: ")
        print (label_right)
        print ("预测label: ")
        print (label_predict)
predict_labels=[]
for predict_label in labels_predict:
    predict_labels.append(str(predict_label))

A = dict.fromkeys(labels_right,0)  #预测正确的各个类的数目
B = dict.fromkeys(labels_right,0)   #测试数据集中各个类的数目
C = dict.fromkeys(predict_labels,0) #预测结果中各个类的数目
for i in range(0,len(labels_right)):
    B[labels_right[i]] += 1
    C[predict_labels[i]] += 1
    if labels_right[i] == predict_labels[i]:
        A[labels_right[i]] += 1
print A
print B
print C
#计算准确率，召回率，F值
for key in B:
    try:
        r = float(A[key]) / float(B[key])
        p = float(A[key]) / float(C[key])
        f = p * r * 2 / (p + r)
        print "%s:\t precision:%f\t recall:%f\t f:%f" % (key,p,r,f)
    except:
        print "error:", key, "right:", A.get(key,0), "real:", B.get(key,0), "predict:",C.get(key,0)

