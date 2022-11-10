import numpy as np

arr = ([ 

  [1, 0, 0], 

  [1, 1, 1], 

  [2, 2, 2] 

])
ilist=[]
jlist=[]
klist=[]
arr1 = np.array(arr)
for i in arr1:
  ilist.append(i[0])
  ilist2 = ilist.copy()
  jlist.append(i[1])
  jlist2 = jlist.copy()
  klist.append(i[2])
  klist2 = klist.copy()
  # print(i[0])
# ilist.sort()
# jlist.sort()
# klist.sort()
# print(ilist,jlist,klist)



set_i = list(set(ilist))
set_i.sort()
sttt1= str(set_i)

list_i = list(ilist)
lsttt1 = str(list_i)

set_j = list(set(jlist))
set_j.sort()
sttt2= str(set_j)

list_j = list(jlist)
lsttt2 = str(list_j)

set_k = list(set(klist))
set_k.sort()
sttt3= str(set_k)

list_k = list(klist)
lsttt3 = str(list_k)

# print(sttt1[1:len(sttt1)-1],"|",lsttt1[1:len(lsttt1)-1])
# print(sttt2[1:len(sttt2)-1],"|",lsttt2[1:len(lsttt2)-1])
# print(sttt3[1:len(sttt3)-1],"|",lsttt3[1:len(lsttt3)-1])

# print(set(ilist2))
# print(ilist)
if sttt1[1:len(sttt1)-1]==lsttt1[1:len(lsttt1)-1] and sttt2[1:len(sttt2)-1]==lsttt2[1:len(lsttt2)-1] and sttt3[1:len(sttt3)-1]==lsttt3[1:len(lsttt3)-1]:#:#and jlist[0:len(ilist)]==set(jlist2)[0:len(ilist)] and klist[0:len(ilist)]==set(klist2)[0:len(ilist)]
  print("true")
else:
  print("false")  