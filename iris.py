#!/usr/bin/python
import 
from  sklearn.datasets  import  load_iris
from   sklearn   import  tree
import  numpy  as  np
ir_data=load_iris()

df=[0,50,100]

training_target=np.delete(ir_data.target,df)
training_data=np.delete(ir_data.data,df,axis=0)


testing_target=ir_data.target[df]
testing_data=ir_data.data[df]

clf=tree.DecisionTreeClassifier()
check=clf.fit(training_data,training_target)
print (  check.predict(testing_data) )




