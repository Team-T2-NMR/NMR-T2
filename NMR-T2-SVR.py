from sklearn.svm import SVR
import numpy as np


example = [['H2O',2,3,4,2,1,8.7],['H3C2',2,3,4,2,1,7.6],['H3H1C2',2,3,3,2,1,6.5],['H3C2J3',2,3,3,2,1,4.3],['H2O3',2,3,4,2,1,8.7]]
example_name = list(x[0] for x in example)
example_feature = list(x[1:-1] for x in example)
example_ppm = list(x[-1] for x in example)

size = len(example)

clf = SVR(C=1.0, epsilon=0.2)
clf.fit(example_feature,example_ppm)

new_atom_features = [2,3,4,2,1]

print  'the new atom ppm might be: '+ str(clf.predict(new_atom_features)[0])