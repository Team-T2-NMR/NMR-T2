from sklearn import svm


example = [['H2O',2,3,4,2,1,8.7],['H3C2',2,3,4,2,1,7.6],['H3H1C2',2,3,3,2,1,6.5],['H3C2J3',2,3,3,2,1,4.3],['H2O3',2,3,4,2,1,8.7]]
example_name = list(x[0] for x in example)
example_feature = list(x[1:-1] for x in example)
example_ppm = list(x[-1:] for x in example)
example_ppm1 = list(x[-1:] for x in example)
#print example_ppm1
size = len(example)
for x in range(size):
    for y in range(size):
        if (example_feature[x] == example_feature[y]):
            if(example_ppm1[y][0] not in example_ppm[x] ):
                example_ppm[x].append(example_ppm1[y][0])
#for x in range(size):                
#    print 'ATOM: '+ str(example_name[x])+' FEATURES : '+ str(example_feature[x])+ ' PPM: '+str(example_ppm[x])
        
#@print example_feature
#print example[:][1]


#X = [[0, 0, 0], [1, 3,2],[2,5,3]]
#y = ['3.2', '2','4']
for x in range(size):
    example_ppm[x] = 'similer to atom: '+str(example_name[x]) +' with ppm: '+ str(example_ppm[x])

#print example_feature
#print example_ppm
clf = svm.SVC()
#clf.fit(example_feature, example_ppm)  
clf.fit(example_feature, example_ppm) 


new_atom_features = [2,3,4,2,1]
print clf.predict(new_atom_features)
