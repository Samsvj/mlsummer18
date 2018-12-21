#!/usr/bin/python2

import cv2
import numpy as np
import os
from sklearn import tree
from sklearn.metrics import accuracy_score

'''
''
img_list=os.listdir('/root/Desktop/foootbal')
x=cv2.imread('/root/Desktop/foootbal/1.jpg',0)

#loop to store all the images in numpy array x
for i in img_list:
	#skiping first image as it is stored earlier
	if i=='1.jpg':
		continue
	#loading the left over images in the numpy array
	else:

		y=cv2.imread('/root/Desktop/foootbal/'+i,0)
		
		#appending the other images data in numpy array x
		z=np.concatenate((x,y))
		x=z
		img_data=x

'''
features=np.loadtxt("tryfootball.txt")
print (features)

kn=features.reshape(10,160000)
print(features.shape)
print(kn.shape)

label=[]
for i in range(1,11):
	label.append([i])
print (label)

# importing a clasifier

clf=tree.DecisionTreeClassifier()
algo=clf.fit(kn,label)

# training data
remove=kn[8]

train_target=np.delete(kn,remove)
train_data=np.delete(kn,remove,axis=0)
'''
# testing data

test_target=new_list[0]
test_img=new_data[0]
'''

# predicting


predict=algo.predict([remove])

print (predict)





