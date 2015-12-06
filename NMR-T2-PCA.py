import numpy as np
from sklearn.decomposition import PCA
from sklearn import svm

example = [['H2O',2,3,4,2,1,8.7],['H3C2',2,3,4,2,1,7.6],['H3H1C2',2,3,2,2,1,6.5],['H3C2J3',2,3,3,2,1,4.3],['H2O3',2,3,4,2,1,8.7],['H2O3',2,3,2,2,1,8.7]]
example_name = list(x[0] for x in example)
example_feature = list(x[1:-1] for x in example)
example_ppm = list(x[-1:] for x in example)
example_ppm1 = list(x[-1:] for x in example)

size = len(example)

#X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
pca = PCA(n_components=1)
pca.fit(example_feature)
pac_classif = pca.fit_transform(example_feature)
#print pac_classif


size = len(example)
for x in range(size):
    for y in range(size):
        if (format(pac_classif[x][0],'.5f') == format(pac_classif[y][0],'.5f')):
            if(example_ppm1[y][0] not in example_ppm[x] ):
                example_ppm[x].append(example_ppm1[y][0])
#print example_ppm
example_ppm_ans = example_ppm
#print example_ppm
#for x in range(size):
#    example_ppm_ans[x] = 'similer to atom: '+str(example_name[x]) +' with ppm: '+ str(example_ppm[x])
#print example_ppm    

new_atom_features = [2,3,4,2,1]

example_feature.append(new_atom_features)
pca = PCA(n_components=1)
pca.fit(example_feature)
new_feature_table = pca.fit_transform(example_feature)
for i in range(len(new_feature_table)):
    if(format(new_feature_table[-1][0],'.5f') == format(new_feature_table[i][0],'.5f')):
        result  = example_ppm[x]
        break
#print result 
#print example_ppm

#print '*----*'
name_list = []
for i in range(size):
    if (sorted(result) == sorted(example_ppm[i])):
        name_list.append(example_name[i])
        #print 'similer to atom: '+str(example_name[i]) +' with ppm: '+ str(example_ppm[i])
print 'similer to atom: '+str(name_list) +' with ppm: '+ str(example_ppm[i])        
