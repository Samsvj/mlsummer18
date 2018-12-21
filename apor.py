
#!/usr/bin/env python3


x='''
this program is about the dataset of apple and orange with thier comparison for a machine and its features

'''
print (x)

from sklearn import tree

# here smooth==1 and bumpy == 0

features=[[120,1],[130,1],[180,0],[190,0],[110,1],[170,0],[135,1],[150,1],[151,0]]

#assuming labels for apple as smooth and orange as bumpy

label=["apple","apple","orange","orange","apple","orange","apple","apple","orange",]

#loading decision tree and storing the variables

clf=tree.DecisionTreeClassifier()

train=clf.fit(features,label)

output = train.predict([[150.5,1],[165,0],[111,0],[123,1],])

print (output)


