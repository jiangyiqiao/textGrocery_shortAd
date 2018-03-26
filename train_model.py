# coding: utf-8

from tgrocery import Grocery


grocery = Grocery('models')

train_src = 'data/train/tgrocery_train.txt'
grocery.train(train_src)
print grocery.get_load_status()
grocery.save()

