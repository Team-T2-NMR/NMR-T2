from sklearn import svm
import readinput as readin
import numpy as np

filename = 'input_data_1.txt'
example = readin.open_file_init(filename)

#example = [['H2O',2,3,4,2,1,8.7],['H3C2',2,3,4,2,1,7.6],['H3H1C2',2,3,3,2,1,6.5],['H3C2J3',2,3,3,2,1,4.3],['H2O3',2,3,4,2,1,8.7]]
example_name = list(x[0] for x in example)
example_feature = list(x[1:-1] for x in example)
example_test = example_feature[1200:-1]
example_feature = example_feature[0:1200]
example_ppm = list(x[-1:] for x in example)
example_ppm1 = list(x[-1:] for x in example)

result_list = []
total_dif = 0

#print example_ppm1
size = len(example)
#for x in range(size):
#    for y in range(size):
#        if (example_feature[x] == example_feature[y]):
#            if(example_ppm1[y][0] not in example_ppm[x] ):
#                example_ppm[x].append(example_ppm1[y][0])
#for x in range(size):                
#    print 'ATOM: '+ str(example_name[x])+' FEATURES : '+ str(example_feature[x])+ ' PPM: '+str(example_ppm[x])
        
#@print example_feature
#print example[:][1]


#X = [[0, 0, 0], [1, 3,2],[2,5,3]]
#y = ['3.2', '2','4']
for x in range(size):
    example_ppm[x] = str(example_ppm[x][0])
    #print example_ppm[x]
    #example_ppm[x] = 'similer to atom: '+str(example_name[x]) +' with ppm: '+ #str(example_ppm[x])

#print example_feature
#print example_ppm
clf = svm.SVC()
#clf.fit(example_feature, example_ppm)  
clf.fit(example_feature, example_ppm[0:1200]) 
print '*****************'
print example_test
print '*****************'
size_test = len(example_test)
for k in range(size_test):
    new_atom_features = example_test[k]
    result =  clf.predict(new_atom_features)
    #print result
    res_size = len(result)
    #print res_size
    total = 0
    for y in range(res_size):
        #print result[y]
        total = total + float(result[y])
    avage = total/res_size
    different = abs(example_ppm1[k][0] - avage)
    single_result = 'the predict item is: '+ example_name[k] +' real ppm: ' + str(example_ppm1[k]) + ' predict avage ppm : '+ str(avage) + ' diffrent: '+str(different)
    total_dif = total_dif + different
    result_list.append(single_result)    

f = open('SVC-OUT-PUT.txt','w')
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
#es = [ 0.028592715669199673, -0.0321820632248, -0.0321820632248, -0.0321820632248, -0.039130159099, 0.0425171702781, 0.0106599089495, -0.256130206755, 0.0515943483686, -0.0174291272836, -0.039130159099, 0.0425171702781, -5.05840941125e-05, -0.256130206755, 0.0515943483686, -0.0104777100078, -0.330472333456, 0.176926861864, -0.0123729950081, -0.49679513073, 0.176926861864, -0.0234305499443, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]



