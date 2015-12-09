import numpy
import scipy

import sklearn

#filename = 'input_data_1.txt'
#matrix = []
#input_matrix = []
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
    matrix = []
    f = open(filename,'r')
    text1 = f.readlines()
    filesize = len(text1)
    
    #print len(text1)

    for i in range(filesize):
            matrix.append(text1[i].split())
    #print(matrix)
    proton_size = len(matrix[i])
    
    for i in range(filesize):
        #print matrix[i]
        for k in range(proton_size):
            if (k+1 == proton_size):
                break
                #print matrix[i][k+1]
            matrix[i][k+1] = float(matrix[i][k+1])
            #matrix[i][k+1] = format(matrix[i][k+1],'.8f')
        print matrix[i]
    #print matrix
    return matrix
#open_file_init(filename)
  #  for i in range(20):
  #      temp = []
        #print matrix[i][5]
  #      temp.append(int(matrix[i][5]))
  #      temp.append(int(matrix[i][7]))
  #      train_matrix.append(temp)
  #      #train_matrix.append(temp)
  #  print train_matrix
  #  print len(train_matrix)
        
#def classify():
#    k =1
#