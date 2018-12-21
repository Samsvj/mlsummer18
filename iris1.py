

#!/usr/bin/env python3

#import the dataset

import numpy as np
from sklearn import tree
from sklearn.datasets import load_iris
iris=load_iris()

# now trian the data that is need to be 
data_test=[0,50,100]

train_data=np.delete(iris.data,data_test,axis=0)
train_target=np.delete(iris.target,data_test)

#now write the test data that will be used in prediction...

#testing data...

test_data=iris.data[data_test]
test_target=iris.target[data_test]

#calling the classifier....

clf=tree.DecisionTreeClassifier()
pp=clf.fit(iris.data,iris.target)

#prediction of datasets

output = pp.predict(test_data)

print (output)

print ( test_data[2],test_target[2])
