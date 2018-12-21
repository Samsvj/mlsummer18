#!/usr/bin/env python3

from  sklearn  import  tree

#  training our model with features

#  assume  smooth == 0 and  bumpy == 1
features=[[130,0],[140,0],[150,1],[160,1]]

# assigning labels according to features 

label=["apple","apple","orange","orange"]

#  loading decision tree and storing into a variable 
clf=tree.DecisionTreeClassifier()

trained=clf.fit(features,label)

print(trained.predict([[135,1]]))
