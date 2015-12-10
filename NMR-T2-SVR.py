from sklearn.svm import SVR
import numpy as np
import readinput as readin

filename = 'input_data_1.txt'
example = readin.open_file_init(filename)


#example = [['H2O',2,3,4,2,1,8.7],['H3C2',2,3,4,2,1,7.6],['H3H1C2',2,3,3,2,1,6.5],['H3C2J3',2,3,3,2,1,4.3],['H2O3',2,3,4,2,1,8.7]]
example_name = list(x[0] for x in example)
example_feature = list(x[1:-1] for x in example)
example_test = example_feature[1200:-1]
example_feature = example_feature[0:1200]
example_ppm = list(x[-1] for x in example)
example_ppm1 = list(x[-1] for x in example)
result_list = []
total_dif = 0

size = len(example)

clf = SVR(C=1.0, epsilon=0.2)
clf.fit(example_feature,example_ppm[0:1200])
test_size = len(example_test)
for k in range(test_size):
    new_atom_features = example_feature[k]
    result =  clf.predict(new_atom_features)
    res_size = len(result)
    total = 0
    for y in range(res_size):
        total = total + result[y]
    avage = total/res_size
    different = abs(example_ppm1[k] - avage)
    single_result = 'the predict item is: '+ example_name[k] +' real ppm: ' + str(example_ppm1[k]) + ' predict avage ppm : '+ str(avage) + ' diffrent: '+str(different)
    total_dif = total_dif + different
    result_list.append(single_result)    

f = open('SVR-OUT-PUT.txt','w')
#f.write('hi there\n') # python will convert \n to os.linesep
for i in range(len(result_list)):
    f.write(result_list[i]+'\n')
f.write('***********************************\n')
f.write('the total difference is: ' + str(total_dif)+' over '+ str(len(result_list))+' cases '+ ', the average is: ' + str(total_dif/len(result_list))+'\n')
f.write ('**************************************\n')
f.close()


#for i in range(len(result_list)):
#    print result_list[i]
#print '***********************************'
#print 'the total difference is: ' + str(total_dif)+' over '+ str(len(result_list))+' cases '+ ', the average is: ' + str(total_dif/len(result_list))
#print'**************************************'

