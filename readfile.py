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
    print train_matrix
    print len(train_matrix)
        
def classify():
    k =1
    
open_file_init(filename)