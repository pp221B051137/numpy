import numpy

lst = numpy.array([ 

  ["-", "-", "-", "-", "-"], 

  ["-", "-", "-", "-", "-"], 

  ["-", "-", "#", "-", "-"], 

  ["-", "-", "-", "-", "-"], 

  ["-", "-", "-", "-", "-"] 

])

n , m = lst.shape

for i in range(n):
  for j in range(m):
    cnt = 0
    # print(j)
    if lst[i][j] == '#': 
      continue
    if i == 0 and j == 0:
      if lst[i][j+1] == '#':
        cnt += 1
      if lst[i+1][j] == '#':
        cnt+=1
      if lst[i+1][j+1] == '#':
        cnt+=1
    elif i == 0 and j == m-1:
      if lst[i+1][j] == '#':
        cnt+=1
      if lst[i+1][j-1] == '#':
        cnt+=1
      if lst[i][j-1] == '#':
        cnt+=1
    elif i == n-1 and j == 0:
      if lst[i-1][j] == '#':
        cnt+=1
      if lst[i-1][j+1] == '#':
        cnt+=1
      if lst[i][j+1] == '#':
        cnt+=1
    elif i == n-1 and j == m-1:
      if lst[i-1][j] == '#':
        cnt+=1
      if lst[i-1][j-1] == '#':
        cnt+=1
      if lst[i][j-1] == '#':
        cnt+=1


    elif i == 0 and 0 < j < m-1:
      if lst[i+1][j] == '#':
        cnt+=1
      if lst[i][j-1] == '#':
        cnt+=1
      if lst[i][j+1] == '#':
        cnt+=1
      if lst[i+1][j-1] == '#':
        cnt+=1
      if lst[i+1][i+1] == '#':
        cnt+=1
    elif i == n-1 and 0 < j < m-1:
      if lst[i-1][j] == '#':
        cnt+=1
      if lst[i][j-1] == '#':
        cnt+=1
      if lst[i][j+1] == '#':
        cnt+=1
      if lst[i-1][j-1] == '#':
        cnt+=1
      if lst[i-1][j+1] == '#':
        cnt+=1
    elif 0 < i < n-1 and j ==0:
      if lst[i][j+1] == '#':
        cnt+=1
      if lst[i-1][j] == '#':
        cnt+=1
      if lst[i+1][j] == '#':
        cnt+=1
      if lst[i-1][j+1] == '#':
        cnt+=1
      if lst[i+1][i+1] == '#':
        cnt+=1
    elif 0 < i < n-1 and j == m-1:
      if lst[i][j-1] == '#':
        cnt+=1
      if lst[i-1][j] == '#':
        cnt+=1
      if lst[i+1][j] == '#':
        cnt+=1
      if lst[i-1][j-1] == '#':
        cnt+=1
      if lst[i+1][i-1] == '#':
        cnt+=1
    elif 0 < i < n-1 and 0< j < m-1:
      if lst[i-1][j-1] == '#':
        cnt+=1
      if lst[i-1][j] == '#':
        cnt+=1
      if lst[i-1][j+1] == '#':
        cnt+=1
      if lst[i][j-1] == '#':
        cnt+=1
      if lst[i][i+1] == '#':
        cnt+=1
      if lst[i+1][j-1] == '#':
        cnt+=1
      if lst[i+1][j] == '#':
        cnt+=1
      if lst[i+1][j+1] == '#':
        cnt+=1
    lst[i][j] = cnt
print(lst)

      





# arr = np.array([lst])
# result = np.where(lst == "#")
# print(result)