

#!/usr/bin/env python3

#import the dataset
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
from sklearn.datasets import load_iris
iris=load_iris()

# now trian the data that is need to be 
data_test=[24,44,56,77,69,101,124]

train_data=np.delete(iris.data,data_test,axis=0)
train_target=np.delete(iris.target,data_test)

#now write the test data that will be used in prediction...

#testing data...

test_data=iris.data[data_test]
test_target=iris.target[data_test]

#calling the classifier....

clf=KNeighborsClassifier(n_neighbors=4)
pp=clf.fit(train_data,train_target)

#prediction of datasets
print (pp.predict(test_data))

'''
print ( test_data[2],test_target[2])

'''
