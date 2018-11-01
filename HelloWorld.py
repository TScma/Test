import numpy as np
from functools import reduce

# from __future__ import absolute_import
list = np.arange(1,17)
list1 = [1,2,3,6,7,8,9,10,11,12,13,14,15,16]
list1 = np.array(list1)
np.random.shuffle(list)
np.random.shuffle(list1)
print(list)
print(list1)
# list1 = [[1,5],[4,8]]
# list2 = [[5,3],[1,2],[4,5]]
# print(np.dot(list1,list2))
# num = [1,2,3,4,7,9,12]
# print(list(map(lambda x:x**2,num)))
# pos_num = filter(lambda x:x < 5,num)
# x = list(pos_num)
# print(reduce(lambda x,y:x + y,x)/len(x))
# print(reduce(lambda x,y:x+y,pos_num)/len(list(pos_num)))
