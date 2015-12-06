# Logistic Regression
from sklearn import datasets
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
from matplotlib import style
style.use("ggplot")
import numpy
import scipy

import sklearn

filename = 'nmr_training_examples.txt'
matrix = []
train_matrix = []
#----------------------------------------
#matrix[i] is the different spectrum    |
#matrix[i][0] is Spectrum ID            |
#matrix[i][1] is Database ID            |
#matrix[i][2] is InChi Key              |
#matrix[i][3] is Solvent Sample         |
#matrix[i][4] is pH                     |
#matrix[i][5] is Frequency              |
#matrix[i][7] is Atom number            |
#matrix[i][8] is Shift                  |
#----------------------------------------
def open_file_init(filename):
    f = open(filename,'r')
    text1 = f.readlines()
    x = [1,2]

    for i in range(20):
        if (i < 20):
            matrix.append(text1[i+1].split())
    #print(matrix)
    for i in range(20):
        temp = []
        #print matrix[i][5]
        temp.append(int(matrix[i][5]))
        temp.append(int(matrix[i][7]))
        train_matrix.append(temp)
        #train_matrix.append(temp)
    #print train_matrix
    print len(train_matrix)
    
    # load the iris datasets
    print '***********************************'
    print '***********************************'
    dataset = train_matrix
    # fit a logistic regression model to the data
    model = LogisticRegression()
    
    
    print 'dataset.target-----------------------'
    target = [1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9,0]
    #print dataset.target
    print len(target)
    print 'model--------------------------'
    model.fit(dataset, target)
    print(model)
    print '--------------------------'
    # make predictions
    expected = target
    predicted = model.predict(dataset)
    print 'predicted***********************************'
    print predicted
    print '***********************************'
    # summarize the fit of the model
    print 'classification_report--------------------------'
    print(metrics.classification_report(expected, predicted))
    print expected
    predicted
    print 'confusion_matrix--------------------------'
    print(metrics.confusion_matrix(expected, predicted))   
    
    
    
        
def classify():
    k =1
    
open_file_init(filename)



