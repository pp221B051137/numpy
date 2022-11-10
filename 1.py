import numpy as np
lst = [ 

  [1, 2, 3, 7 ], 

  [4, 5, 6, 15], 

  [7, 8, 9, 24], 

  [12,15,18,45] 

] 
s1 = np.sum(lst,axis=1)
s2 = np.sum(lst,axis=0)

for i in range(len(s1)):
    for j in range(len(s1)):
        if s1[i]!=(lst[i][len(s1)-1])*2 and s2[j]!=(lst[len(s1)-1][j])*2:       
            print(lst[i][j])
